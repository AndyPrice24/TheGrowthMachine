"""
Final cut-outs and backlit layers for the machine sequence.

Run from the repo root, after cutout-machine.py has written
brand/machine/machine-<art>-cutout.png:

    python3 brand/tools/machine-glows.py

Writes to src/assets/machine/:

  machine-<art>.png      the final cut-out, on a canvas padded so no glow is
                         clipped by the image edge
  glow-<art>-<phase>.png one full-canvas backlit layer per phase
                           in     every slab and every piece of rubble
                           s1-s4  each of the four stage panels
  seq-<art>-<item>.png   the result sequence, each cropped to its own glow:
                           arrow        the chart's arrow, revealed by a wipe
                           bar1-bar4    the chart's bars, lit as the arrow
                                        passes each one
                           block1-5     the result blocks, each lit with its
                                        bar; the fifth with the arrow's tip
  manifest.json          canvas sizes, the padding, and every sequence item's
                         box and timing, for MachineRun.astro

Each backlit layer is a torch-red glow hugging the object's outline, with the
object redrawn on top, so the glow reads as light from behind it even where
it sits inside the machine body.

The cut-out is also finished here: the last trapped studio backdrop between
the rubble and the cables is removed so nothing light shows on a dark page;
on desktop, where the rubble ran off the left edge of the render, the pile is
mirrored outward and thinned piece by piece so it crumbles away instead of
stopping at a straight line; and the tank hub that ran off the right edge
fades out.

Every outline (slabs, stage panels, result blocks, bars) is measured by hand
from the originals. Slabs and result blocks are light objects on a light
backdrop, so no edge test separates them reliably, and the four stage panels
must be identical so each highlight looks the same as the last.
"""
import json

import cv2
import numpy as np

TORCH = (21, 39, 255)  # BGR of #FF2715
OUT = "src/assets/machine"


def rrect(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


def chamfer(x, y, w, h, c):
    """The stage panels' light face: a rectangle with 45-degree corners."""
    return [(x + c, y), (x + w - c, y), (x + w, y + c), (x + w, y + h - c), (x + w - c, y + h), (x + c, y + h), (x, y + h - c), (x, y + c)]


ART = {
    "desktop": {
        "in_zone": [(0, 0), (520, 0), (520, 300), (490, 395), (262, 462), (236, 560), (292, 612), (292, 664), (252, 700), (252, 742), (0, 742)],
        "slabs": [
            [(18, 86), (254, 146), (260, 232), (12, 180)],
            [(36, 186), (268, 244), (248, 336), (14, 280)],
            [(28, 296), (276, 344), (264, 432), (16, 384)],
            [(36, 400), (270, 420), (266, 512), (30, 494)],
            [(40, 504), (252, 508), (254, 606), (40, 604)],
            [(40, 592), (272, 580), (282, 668), (52, 708)],
        ],
        "outputs": [rrect(1154, 99 + round(90.75 * k), 268, 81) for k in range(5)],
        "stages": [chamfer(x, 688, 151, 210, 8) for x in (319, 516, 717, 914)],
        "bars": [(1210, 814, 29, 39), (1247, 798, 32, 55), (1286, 773, 33, 80), (1328, 740, 33, 113)],
        "arrow_box": (1196, 676, 175, 134),
        # blocks light bottom-up: the bottom block with the first bar
        "block_order": [4, 3, 2, 1, 0],
        "clean_zones": [[(1040, 30), (1154, 30), (1154, 690), (1040, 690)], [(1154, 544), (1440, 544), (1440, 566), (1210, 566), (1210, 624), (1154, 624)]],
        "glow": (9, 2.2),
        "bar_glow": (6, 1.6),
        # left: 44px of mirrored rubble, then room for its glow
        "pad": {"l": 74, "t": 0, "r": 30, "b": 0},
        "extend_left": 44,
        "fade_right": (720, 830, 18),
    },
    "mobile": {
        "slabs": [
            [(178, 66), (440, 133), (449, 186), (427, 214), (200, 180), (168, 166), (166, 84)],
            [(186, 194), (452, 230), (464, 250), (460, 320), (184, 302), (172, 290), (176, 208)],
            [(174, 296), (432, 310), (442, 330), (437, 404), (178, 404), (168, 390)],
            [(510, 130), (752, 80), (776, 93), (797, 190), (781, 207), (530, 242), (513, 226)],
            [(516, 230), (786, 198), (802, 213), (807, 294), (540, 328), (523, 316)],
            [(543, 326), (796, 306), (805, 320), (804, 404), (555, 420), (546, 406)],
        ],
        "in_zone": [(0, 0), (941, 0), (941, 522), (0, 522)],
        "in_exclude": [(282, 412), (656, 412), (640, 440), (560, 500), (520, 525), (380, 525), (330, 490), (290, 445)],
        "outputs": [rrect(x, 1430, 162, 156) for x in (61, 227, 390, 555, 721)],
        "stages": [chamfer(x, 839, 165, 236, 9) for x in (89, 290, 491, 686)],
        "bars": [(387, 1288, 38, 44), (443, 1270, 39, 62), (497, 1246, 39, 87), (552, 1213, 38, 119)],
        "arrow_box": (346, 1148, 256, 144),
        # blocks sit in a row under the tank: light them left to right, under their bars
        "block_order": [0, 1, 2, 3, 4],
        "clean_zones": [],
        "glow": (14, 3.4),
        "bar_glow": (9, 2.4),
        "pad": {"l": 0, "t": 0, "r": 0, "b": 0},
        "extend_left": 0,
        "fade_right": None,
    },
}


def poly_mask(shape, pts):
    m = np.zeros(shape, np.uint8)
    cv2.fillPoly(m, [np.array(pts, np.int32)], 1)
    return m.astype(bool)


def rounded_mask(shape, pts, r):
    """A polygon with its corners rounded off."""
    m = poly_mask(shape, pts).astype(np.uint8)
    if r:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
        m = cv2.dilate(cv2.erode(m, k), k)
    return m.astype(bool)


def soft(mask, r):
    return cv2.GaussianBlur(mask.astype(np.float32), (0, 0), r)


def glow_layer(objects, rgb, alpha, sigma_outer, sigma_rim, lift=1.0):
    """Torch glow around the objects, with the objects redrawn on top.

    `lift` brightens the redrawn objects, for parts that switch on rather
    than simply being lit from behind.
    """
    obj = objects.astype(np.uint8)
    outer = cv2.GaussianBlur(cv2.dilate(obj, np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), sigma_outer)
    rim = cv2.GaussianBlur(cv2.dilate(obj, np.ones((3, 3), np.uint8)).astype(np.float32), (0, 0), sigma_rim)
    g = 1 - (1 - np.clip(outer * 1.7, 0, 1) * 0.85) * (1 - np.clip(rim * 1.5, 0, 1) * 0.95)
    oa = alpha * soft(objects, 0.7)
    a = oa + g * (1 - oa)
    torch = np.array(TORCH, np.float32)
    col = np.clip(rgb * lift, 0, 255)
    out = (col * oa[..., None] + torch * (g * (1 - oa))[..., None]) / np.maximum(a[..., None], 1e-4)
    return np.dstack([np.clip(out, 0, 255), np.clip(a * 255, 0, 255)]).astype(np.uint8)


def backdrop(img, zone, slabs):
    """Studio backdrop the cut-out kept between rubble and cables.

    Two tests: light, unsaturated and flat at a 3px scale (catches the backdrop
    in narrow gaps, where a wider window would see the stones beside it), or
    simply near-white. Slab faces are light and flat too, so the first test
    skips their interiors and the second skips the slabs entirely.
    """
    lum = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    sat = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[..., 1].astype(np.float32)
    m3 = cv2.blur(lum, (3, 3))
    s3 = np.sqrt(np.maximum(cv2.blur(lum * lum, (3, 3)) - m3 * m3, 0))
    core = cv2.erode(slabs.astype(np.uint8), np.ones((9, 9), np.uint8)).astype(bool)
    near = cv2.dilate(slabs.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
    flat = (lum > 180) & (sat < 48) & (s3 < 10) & ~core
    white = (lum > 210) & (sat < 32) & ~near
    back = cv2.morphologyEx(((flat | white) & zone).astype(np.uint8), cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    halo = ((lum > 158) & (sat < 62) & zone & ~core).astype(np.uint8)
    for _ in range(2):
        back = cv2.dilate(back, np.ones((3, 3), np.uint8)) & halo
    return back.astype(bool)


def extend_rubble(rgb, alpha, slabs, band, seed=4, keep_pow=1.2):
    """Mirror the rubble at the left edge outward, then thin it piece by piece.

    The render's rubble ran off its left edge. Reflecting the first `band`
    columns continues the pile seamlessly (no line at the old edge), and
    keeping each mirrored stone with a chance that falls with distance makes
    the pile crumble away rather than stop. Slabs are never mirrored.
    """
    rng = np.random.default_rng(seed)
    src_a = alpha[:, :band][:, ::-1] * (~slabs[:, :band][:, ::-1])
    src_c = rgb[:, :band][:, ::-1]
    lum = cv2.cvtColor(np.clip(src_c, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY)
    walls = cv2.dilate(cv2.Canny(cv2.GaussianBlur(lum, (0, 0), 1.0), 40, 110), np.ones((2, 2), np.uint8)) > 0
    n, lab, stats, _ = cv2.connectedComponentsWithStats(((src_a > 0.3) & ~walls).astype(np.uint8), connectivity=4)
    keep = np.zeros(n, bool)
    for i in range(1, n):
        x = stats[i, cv2.CC_STAT_LEFT]
        if x <= 1:
            continue  # would reach the outer edge of the band
        d = (band - 1 - x) / band
        keep[i] = rng.random() < (1 - d) ** keep_pow
    kept = cv2.dilate(keep[lab].astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool) & (src_a > 0.05)
    return src_c, src_a * kept


def run(art, c):
    img = cv2.imread(f"brand/machine/machine-{art}-original.png", cv2.IMREAD_COLOR)
    cut = cv2.imread(f"brand/machine/machine-{art}-cutout.png", cv2.IMREAD_UNCHANGED)
    H, W = img.shape[:2]
    shape = (H, W)
    alpha = cut[..., 3].astype(np.float32) / 255
    rgb = cut[..., :3].astype(np.float32)

    slabs = np.zeros(shape, bool)
    for p in c["slabs"]:
        slabs |= rounded_mask(shape, p, 4)
    outs = [rounded_mask(shape, p, 9) for p in c["outputs"]]
    out_all = np.any(outs, axis=0)

    # ---- clean the cut-out: drop trapped backdrop around the rubble and cables
    zone = poly_mask(shape, c["in_zone"])
    if "in_exclude" in c:
        zone &= ~poly_mask(shape, c["in_exclude"])
    cleaning = zone.copy()
    for z in c["clean_zones"]:
        cleaning |= poly_mask(shape, z)
    back = backdrop(img, cleaning & ~out_all, slabs)
    alpha = alpha * (1 - soft(back, 0.7))
    solid = (alpha > 0.3).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(solid, connectivity=8)
    crumbs = np.isin(lab, [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] < 10]) & cleaning
    alpha[crumbs] = 0

    if c["fade_right"]:
        y0, y1, w = c["fade_right"]
        ramp = np.clip(np.arange(w)[::-1] / w, 0, 1)  # 1 inside, 0 at the edge
        ramp = ramp * ramp * (3 - 2 * ramp)
        alpha[y0:y1, W - w:] *= ramp[None, :]

    # ---- the padded canvas; every mask and box below is in its coordinates
    pl, pt, pr, pb = (c["pad"][k] for k in "ltrb")
    PH, PW = H + pt + pb, W + pl + pr

    def pad(a, fill=0):
        out = np.full((PH, PW) + a.shape[2:], fill, a.dtype)
        out[pt:pt + H, pl:pl + W] = a
        return out

    A, RGB = pad(alpha), pad(rgb)
    slabsP, zoneP = pad(slabs), pad(zone)
    if c["extend_left"]:
        b = c["extend_left"]
        ec, ea = extend_rubble(rgb, alpha, slabs, b)
        RGB[pt:pt + H, pl - b:pl] = ec
        A[pt:pt + H, pl - b:pl] = ea
        zoneP[pt:pt + H, :pl] = zoneP[pt:pt + H, pl:pl + 1]
    final = np.dstack([np.clip(RGB, 0, 255), np.clip(A * 255, 0, 255)]).astype(np.uint8)
    cv2.imwrite(f"{OUT}/machine-{art}.png", final)

    def shift_box(b):
        x, y, w, h = b
        return (x + pl, y + pt, w, h)

    def box_mask(b):
        m = np.zeros((PH, PW), bool)
        x, y, w, h = shift_box(b)
        m[y:y + h, x:x + w] = True
        return m

    # ---- full-canvas phases: what goes in, and the four stages
    rubble = zoneP & (A > 0.35) & ~slabsP
    phases = {"in": slabsP | rubble}
    for k, p in enumerate(c["stages"]):
        m = pad(rounded_mask(shape, p, 0))
        phases[f"s{k + 1}"] = cv2.dilate(m.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    so, sr = c["glow"]
    for ph, m in phases.items():
        cv2.imwrite(f"{OUT}/glow-{art}-{ph}.png", glow_layer(m, RGB, A, so, sr))

    # ---- the result sequence: arrow, bars, blocks, each cropped to its glow
    bars = [box_mask(b) for b in c["bars"]]
    bar_any = cv2.dilate(np.any(bars, axis=0).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
    lumP = cv2.cvtColor(np.clip(RGB, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
    satP = cv2.cvtColor(np.clip(RGB, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)[..., 1].astype(np.float32)
    arrow = (lumP > 200) & (satP < 110) & box_mask(c["arrow_box"]) & ~bar_any
    n, lab, stats, _ = cv2.connectedComponentsWithStats(arrow.astype(np.uint8), connectivity=8)
    arrow = lab == 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    arrow = cv2.dilate(arrow.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    ax = np.where(arrow.any(axis=0))[0]
    ax0, ax1 = int(ax.min()), int(ax.max())

    def crop(layer, name):
        ys, xs = np.where(layer[..., 3] > 3)
        x0, x1, y0, y1 = int(xs.min()), int(xs.max()) + 1, int(ys.min()), int(ys.max()) + 1
        cv2.imwrite(f"{OUT}/seq-{art}-{name}.png", layer[y0:y1, x0:x1])
        return [x0, y0, x1 - x0, y1 - y0]

    bo, br = c["bar_glow"]
    seq = {"arrow": {"name": "arrow", "box": crop(glow_layer(arrow, RGB, A, bo, br, 1.15), "arrow"), "span": [ax0, ax1]}, "items": []}
    beats = []
    for k, (m, b) in enumerate(zip(bars, c["bars"])):
        cx = shift_box(b)[0] + b[2] / 2
        at = round(float(np.clip((cx - ax0) / (ax1 - ax0), 0, 1)), 3)
        beats.append(at)
        seq["items"].append({"name": f"bar{k + 1}", "box": crop(glow_layer(m, RGB, A, bo, br, 1.15), f"bar{k + 1}"), "at": at})
    beats.append(1.0)  # the arrow's tip
    for k, idx in enumerate(c["block_order"]):
        m = pad(outs[idx])
        seq["items"].append({"name": f"block{k + 1}", "box": crop(glow_layer(m, RGB, A, so, sr), f"block{k + 1}"), "at": beats[k]})

    print(art, "canvas", (PW, PH), "| backdrop px removed", int(back.sum()), "| beats", beats)
    return {"size": [PW, PH], "offset": [pl, pt], "seq": seq}


if __name__ == "__main__":
    manifest = {art: run(art, c) for art, c in ART.items()}
    with open(f"{OUT}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1)
