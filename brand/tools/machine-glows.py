"""
Backlights for the machine sequence, and a clean-up of the cut-outs.

Run from the repo root, after cutout-machine.py has written
brand/machine/machine-<art>-cutout.png:

    python3 brand/tools/machine-glows.py

For each render it outlines the objects each phase of the sequence lights:
  in     every slab and every piece of rubble
  s1-s4  each of the four stage panels
  out    each result block
and writes src/assets/machine/glow-<art>-<phase>.png: a torch-red glow hugging
those outlines, with the objects redrawn on top so the glow reads as light from
behind them, even where they sit inside the machine body.

It also writes the final cut-out, src/assets/machine/machine-<art>.png, with
the last specks of studio backdrop removed from between the rubble and the
cables, so nothing light is left to show on a dark page.

Every outline (slabs, stage panels, result blocks) is measured by hand from the
originals. Slabs and result blocks are light objects on a light backdrop, so
no edge test separates them reliably, and the four stage panels must be
identical in shape so each highlight looks the same as the last.
"""
import cv2
import numpy as np

TORCH = (21, 39, 255)  # BGR of #FF2715


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
        "clean_zones": [[(1040, 30), (1154, 30), (1154, 690), (1040, 690)], [(1154, 544), (1440, 544), (1440, 566), (1210, 566), (1210, 624), (1154, 624)]],
        "glow": (9, 2.2),
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
        "clean_zones": [],
        "glow": (14, 3.4),
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


def glow_layer(objects, cut, sigma_outer, sigma_rim):
    """Torch glow around the objects, with the objects redrawn on top."""
    obj = objects.astype(np.uint8)
    outer = cv2.GaussianBlur(cv2.dilate(obj, np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), sigma_outer)
    rim = cv2.GaussianBlur(cv2.dilate(obj, np.ones((3, 3), np.uint8)).astype(np.float32), (0, 0), sigma_rim)
    g = 1 - (1 - np.clip(outer * 1.7, 0, 1) * 0.85) * (1 - np.clip(rim * 1.5, 0, 1) * 0.95)
    oa = (cut[..., 3].astype(np.float32) / 255) * soft(objects, 0.7)
    a = oa + g * (1 - oa)
    torch = np.array(TORCH, np.float32)
    rgb = (cut[..., :3].astype(np.float32) * oa[..., None] + torch * (g * (1 - oa))[..., None]) / np.maximum(a[..., None], 1e-4)
    return np.dstack([np.clip(rgb, 0, 255), np.clip(a * 255, 0, 255)]).astype(np.uint8)


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


if __name__ == "__main__":
    for art, c in ART.items():
        img = cv2.imread(f"brand/machine/machine-{art}-original.png", cv2.IMREAD_COLOR)
        cut = cv2.imread(f"brand/machine/machine-{art}-cutout.png", cv2.IMREAD_UNCHANGED)
        H, W = img.shape[:2]
        shape = (H, W)
        alpha = cut[..., 3].astype(np.float32) / 255

        slabs = np.zeros(shape, bool)
        for p in c["slabs"]:
            slabs |= rounded_mask(shape, p, 4)

        outs = np.zeros(shape, bool)
        for p in c["outputs"]:
            outs |= rounded_mask(shape, p, 9)

        # ---- clean the cut-out: drop trapped backdrop around the rubble and cables
        zone = poly_mask(shape, c["in_zone"])
        if "in_exclude" in c:
            zone &= ~poly_mask(shape, c["in_exclude"])
        cleaning = zone.copy()
        for z in c["clean_zones"]:
            cleaning |= poly_mask(shape, z)
        back = backdrop(img, cleaning & ~outs, slabs)
        alpha = alpha * (1 - soft(back, 0.7))
        solid = (alpha > 0.3).astype(np.uint8)
        n, lab, stats, _ = cv2.connectedComponentsWithStats(solid, connectivity=8)
        crumbs = np.isin(lab, [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] < 10]) & cleaning
        alpha[crumbs] = 0
        cut[..., 3] = np.clip(alpha * 255, 0, 255).astype(np.uint8)
        cv2.imwrite(f"src/assets/machine/machine-{art}.png", cut)

        # ---- the objects each phase lights
        rubble = zone & (alpha > 0.35) & ~slabs
        in_objects = slabs | rubble
        stages = [cv2.dilate(rounded_mask(shape, p, 0).astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool) for p in c["stages"]]

        phases = {"in": in_objects, "s1": stages[0], "s2": stages[1], "s3": stages[2], "s4": stages[3], "out": outs}
        so, sr = c["glow"]
        for ph, m in phases.items():
            cv2.imwrite(f"src/assets/machine/glow-{art}-{ph}.png", glow_layer(m, cut, so, sr))
        print(art, "backdrop px removed", int(back.sum()), "| in px", int(in_objects.sum()), "| stage px", [int(s.sum()) for s in stages], "| out px", int(outs.sum()))
