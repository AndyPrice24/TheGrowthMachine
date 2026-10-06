import cv2, numpy as np, sys
cfg = {'desktop': 952, 'mobile': 1588}
POCKET_DIFF, POCKET_STD = 6, 6
# Two plates at the very top touch the backdrop along their whole light edge, so
# the edge-reachability test cannot separate them. Their outlines, inset a few
# pixels, are declared solid by hand.
SOLID = {
    'desktop': [[(1166, 99), (1411, 99), (1419, 107), (1419, 168), (1411, 176), (1166, 176), (1158, 168), (1158, 107)]],
    'mobile': [[(188, 78), (438, 139), (446, 179), (434, 195), (191, 181), (171, 126)]],
}
for name, floor_y in cfg.items():
    img = cv2.imread(f'brand/machine/machine-{name}-original.png', cv2.IMREAD_COLOR)
    H, W = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    s, v = hsv[..., 1].astype(int), hsv[..., 2].astype(int)
    b, g, r = [img[..., i].astype(int) for i in range(3)]
    lum = (0.299 * r + 0.587 * g + 0.114 * b)

    # backdrop candidates: light and close to neutral
    cand = ((v > 140) & (s < 60)).astype(np.uint8)
    cand = cv2.morphologyEx(cand, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    er = cv2.erode(cand, np.ones((5, 5), np.uint8))
    n, lab = cv2.connectedComponents(er, connectivity=4)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    backdrop = np.isin(lab, list(border)).astype(np.uint8)
    backdrop = cv2.dilate(backdrop, np.ones((3, 3), np.uint8)) & cand

    mask = np.full((H, W), cv2.GC_PR_BGD, np.uint8)
    mask[(cand == 0)] = cv2.GC_PR_FGD
    mask[backdrop == 1] = cv2.GC_BGD
    sure_fg = ((lum < 70) | ((r > 190) & (g < 100) & (b < 100)))
    sure_fg = cv2.erode(sure_fg.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    mask[sure_fg & (backdrop == 0)] = cv2.GC_FGD
    mask[floor_y:, :] = cv2.GC_BGD

    bgd = np.zeros((1, 65), np.float64); fgd = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
    fg = ((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD)).astype(np.uint8)
    fg[floor_y:, :] = 0

    # Background is only the backdrop that reaches the image edge. Light parts of
    # the machine (panels, slabs, plates) are enclosed by its dark frames, so they
    # are not background however light they are. Erode first so a thin light rim
    # cannot bridge a plate to the backdrop, then grow back within the original.
    bg = (1 - fg).astype(np.uint8)
    # Outlines act as walls: a plate's rim is an edge even where both sides are light.
    gray = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (0, 0), 1.2)
    walls = cv2.dilate(cv2.Canny(gray, 35, 100), np.ones((3, 3), np.uint8), iterations=2)
    k = 5
    bge = cv2.erode(bg & (1 - (walls > 0)).astype(np.uint8), np.ones((k, k), np.uint8))
    n, lab = cv2.connectedComponents(bge, connectivity=8)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    reach = np.isin(lab, list(edge)).astype(np.uint8)
    # grow back geodesically inside the original background
    for _ in range(k + 4):
        reach = cv2.dilate(reach, np.ones((3, 3), np.uint8)) & bg
    fg = (1 - reach).astype(np.uint8)

    # Pockets: GrabCut background that does not reach the edge. Some are plates
    # (keep), some are backdrop trapped between rubble or cables (make clear).
    # Judge each pocket against the backdrop expected at that spot.
    Wq, Hq = W // 4, H // 4
    known = cv2.resize(reach * 255, (Wq, Hq), interpolation=cv2.INTER_NEAREST)
    est = cv2.inpaint(cv2.resize(img, (Wq, Hq), interpolation=cv2.INTER_AREA), 255 - known, 8, cv2.INPAINT_TELEA)
    est = cv2.resize(cv2.GaussianBlur(est, (0, 0), 2), (W, H), interpolation=cv2.INTER_LINEAR).astype(np.float32)
    diff = np.abs(img.astype(np.float32) - est).mean(2)
    pockets = (bg & (1 - reach) & (1 - (walls > 0))).astype(np.uint8)
    for poly in SOLID[name]:
        cv2.fillPoly(pockets, [np.array(poly, np.int32)], 0)
    n, lab, stats, cents = cv2.connectedComponentsWithStats(pockets, connectivity=8)
    lumf = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    clear = np.zeros((H, W), bool)
    report = []
    for i in range(1, n):
        m = lab == i
        area = int(stats[i, cv2.CC_STAT_AREA])
        md, sd = float(diff[m].mean()), float(lumf[m].std())
        is_backdrop = md < POCKET_DIFF and sd < POCKET_STD
        if is_backdrop:
            clear |= m
        if area > 100000000:
            report.append((area, round(md, 1), round(sd, 1), tuple(int(c) for c in cents[i]), is_backdrop))
    for r in sorted(report, reverse=True)[:40]:
        print('  pocket', r)
    near = cv2.dilate(clear.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
    clear |= near & (bg > 0) & (diff < POCKET_DIFF + 6)
    fg[clear] = 0
    for poly in SOLID[name]:
        cv2.fillPoly(fg, [np.array(poly, np.int32)], 1)
    fg[floor_y:, :] = 0

    # drop specks too small to be rubble
    n, lab, stats, _ = cv2.connectedComponentsWithStats(fg, connectivity=8)
    keep = np.zeros(n, bool); keep[1:] = stats[1:, cv2.CC_STAT_AREA] >= 14
    fg = keep[lab].astype(np.uint8)

    # soft edges guided by the image
    a = cv2.ximgproc.guidedFilter(img, (fg * 255).astype(np.uint8), 2, 1e-2 * 255 * 255).astype(np.float32) / 255
    a = np.clip((a - 0.12) / 0.76, 0, 1)
    a[floor_y:, :] = 0

    # remove the light backdrop bleeding into edge pixels: estimate the backdrop behind them
    small = cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
    hole = cv2.resize(((a > 0.02) * 255).astype(np.uint8), (W // 4, H // 4), interpolation=cv2.INTER_NEAREST)
    hole = cv2.dilate(hole, np.ones((5, 5), np.uint8))
    bgest = cv2.inpaint(small, hole, 6, cv2.INPAINT_TELEA)
    bgest = cv2.resize(cv2.GaussianBlur(bgest, (0, 0), 3), (W, H), interpolation=cv2.INTER_LINEAR).astype(np.float32)
    A = a[..., None]
    F = (img.astype(np.float32) - (1 - A) * bgest) / np.maximum(A, 0.05)
    F = np.where(A > 0.98, img.astype(np.float32), F)
    F = np.clip(F, 0, 255)

    out = np.dstack([F.astype(np.uint8), (a * 255).astype(np.uint8)])
    cv2.imwrite(f'src/assets/machine/machine-{name}.png', out)
    print(name, 'foreground share', round(float(a.mean()), 3))
