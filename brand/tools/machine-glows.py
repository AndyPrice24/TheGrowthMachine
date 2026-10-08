"""
Final cut-outs and backlit layers for the machine sequence.

Run from the repo root, after cutout-machine.py has written
brand/machine/machine-<art>-cutout.png:

    python3 brand/tools/machine-glows.py

Writes to src/assets/machine/:

  machine-<art>.png      the final cut-out, on a canvas padded so no glow is
                         clipped by the image edge
  glow-<art>-<phase>.png one full-canvas backlit layer per phase
                           in     the six problem slabs (not the rubble)
                           s1-s4  each of the four stage panels
  seq-<art>-<item>.png   the result sequence, each cropped to its own glow:
                           arrow        the chart's arrow, revealed by a wipe
                           bar1-bar4    the chart's bars, lit as the arrow
                                        passes each one
                           block1-5     the result blocks, each lit with its
                                        bar; the fifth with the arrow's tip
  manifest.json          canvas sizes, the padding, and every sequence item's
                         box and timing, for MachineRun.astro

Slabs, stage panels and result boards are kept fully solid, and on desktop
each result board's icon and text are recentred between its rivets (the
render drew most of them off-centre).

Each backlit layer is a glow hugging the object's outline, with the object
redrawn on top, so the glow reads as light from behind it even where it sits
inside the machine body. Problems going in and results coming out are lit
warm white, like the nameplate; the stages and the chart's arrow and bars are
lit torch red, so red means the machine at work.

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
import os

import cv2
import numpy as np

TORCH = (21, 39, 255)  # BGR of #FF2715
OUT = os.environ.get("TGM_OUT", "src/assets/machine")
# Warm white, the nameplate's light. The problem slabs going in and the result
# blocks coming out are lit with it; red is kept for the machine's own work
# (the four stages) and the chart's arrow and bars (decided 8 October 2026,
# after a red blaze of rubble read as alarm rather than as the brand).
WARM = (170, 215, 255)  # BGR of #FFD7AA
WARM_STRENGTH = 0.55
# The "in" phase, overridable to try variants: which objects light ("slabs"
# = the problem slabs only, "all" = slabs and rubble), how strongly, in what
# colour (BGR), and how much the lit objects brighten.
IN_LIGHT = os.environ.get("TGM_IN", "slabs")
IN_STRENGTH = float(os.environ.get("TGM_IN_STRENGTH", str(WARM_STRENGTH)))
IN_LIFT = float(os.environ.get("TGM_IN_LIFT", "1"))
IN_COLOUR = tuple(int(v) for v in os.environ.get("TGM_IN_COLOUR", ",".join(map(str, WARM))).split(","))


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
            [(40, 592), (266, 580), (270, 664), (52, 708)],
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
        # Genuinely white parts the pocket sweep must leave alone (original
        # render coordinates): the pressure gauge face, and the small white
        # indicator arrow beside stage 4. The nameplate is covered separately.
        "keep_light": {"circles": [(522, 480, 40)], "boxes": [(1074, 758, 26, 26)]},
        "nameplate": (545, 515, 364, 143),
        # where rubble meets the frame, backdrop is too small and too tinted
        # for the pocket test; only here, take anything near-white
        "sliver_zones": [[(250, 560), (330, 560), (330, 790), (200, 790), (200, 700), (250, 660)]],
        # Result boards: the render drew most of them off-centre. Their rivets
        # sit symmetrically about x=1291, so each board's icon-and-text is
        # recentred on that line, and shrunk only if wider than the room
        # between the rivets.
        "recentre": {"centre": 1291, "room": 224, "x": (1177, 1420)},
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
        "keep_light": {"circles": [(238, 647, 38)], "boxes": []},
        "nameplate": (272, 652, 390, 158),
        "sliver_zones": [],
        "recentre": None,
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


def glow_layer(objects, rgb, alpha, sigma_outer, sigma_rim, lift=1.0, strength=1.0, colour=None):
    """Torch glow around the objects, with the objects redrawn on top.

    `lift` brightens the redrawn objects, for parts that switch on rather
    than simply being lit from behind.
    """
    obj = objects.astype(np.uint8)
    outer = cv2.GaussianBlur(cv2.dilate(obj, np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), sigma_outer)
    rim = cv2.GaussianBlur(cv2.dilate(obj, np.ones((3, 3), np.uint8)).astype(np.float32), (0, 0), sigma_rim)
    g = (1 - (1 - np.clip(outer * 1.7, 0, 1) * 0.85) * (1 - np.clip(rim * 1.5, 0, 1) * 0.95)) * strength
    oa = alpha * soft(objects, 0.7)
    a = oa + g * (1 - oa)
    torch = np.array(colour or TORCH, np.float32)
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


def recentre_boards(rgb, src, boards, cfg):
    """Centre each result board's icon and text between its rivets.

    Content is everything dark (lettering) or red (icon) on the board. It is
    lifted off with its soft edges, the plate behind it is rebuilt from a
    smooth fit of the plate around it, and the content is put back centred,
    scaled down only if it would not fit the room between the rivets.
    Rivets are left untouched. Everything is read from the original render
    (`src`): outside the cut-out the cut-out's colours are undefined, and the
    lettering on two boards runs right up to the board's edge.
    """
    img = rgb.copy()
    src = src.astype(np.float32)
    lum = cv2.cvtColor(np.clip(src, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
    redness = src[..., 2] - src[..., 1]
    x0, x1 = cfg["x"]
    for (bx, by, bw, bh) in boards:
        dark = lum < 110
        red = redness > 60
        n, lab, st, _ = cv2.connectedComponentsWithStats((dark | red).astype(np.uint8)[by:by + bh, x0:x1], connectivity=8)
        content = np.zeros(lum.shape, bool)
        rivets = np.zeros(lum.shape, bool)
        for i in range(1, n):
            cx, cy, cw, ch, area = st[i]
            if cw <= 11 and ch <= 11 and (cx + x0 > x1 - 20 or cx + x0 < x0 + 4):
                rivets[by:by + bh, x0:x1] |= lab == i  # a rivet at the board's corners
            elif ch >= 9 and area >= 40 and cw < 120 and ch < bh - 10:
                content[by:by + bh, x0:x1] |= lab == i
        ys, xs = np.where(content)
        cy0, cy1, cxa, cxb = ys.min() - 4, ys.max() + 5, xs.min(), xs.max() + 1
        rivets = cv2.dilate(rivets.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
        sl = (slice(cy0, cy1), slice(x0, x1))
        R, L, C, V = src[sl], lum[sl], content[sl], rivets[sl]
        keep = img[sl]
        near = cv2.dilate(C.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)

        # the plate behind: a smooth surface fitted to the plate around the content
        yy, xx = np.mgrid[0:R.shape[0], 0:R.shape[1]].astype(np.float32)
        u, v = xx / R.shape[1], yy / R.shape[0]
        basis = np.stack([np.ones_like(u), u, v, u * u, v * v, u * v], -1)
        sample = ~near & ~V & (L > 150)
        plate = np.zeros_like(R)
        for ch in range(3):
            coef, *_ = np.linalg.lstsq(basis[sample], R[..., ch][sample], rcond=None)
            plate[..., ch] = basis @ coef
        plate_l = cv2.cvtColor(np.clip(plate, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)

        # the content with its soft edges, unmixed from the plate
        grow = cv2.dilate(C.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
        a_dark = np.clip((plate_l - L) / np.maximum(plate_l - 25, 1), 0, 1)
        a_red = np.clip((R[..., 2] - R[..., 1] - 25) / 140, 0, 1)
        a = np.maximum(a_dark, a_red) * grow
        # The lettering and icons are flat colours: ink, and the icon red.
        # Using those (rather than unmixing every soft edge pixel) keeps the
        # edges clean when the content moves.
        ink = np.median(R[(a_dark > 0.85) & C], axis=0)
        is_red = (a_red > 0.6) & C
        red_ink = np.median(R[is_red], axis=0) if is_red.any() else ink
        red_w = cv2.dilate((a_red > a_dark).astype(np.uint8) * grow.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(np.float32)
        F = ink[None, None, :] * (1 - red_w[..., None]) + red_ink[None, None, :] * red_w[..., None]

        # clean plate: content areas rebuilt from the scratched plate around
        # them (inpainting keeps the local tone a smooth fit would lose)
        hole = (cv2.dilate(grow.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool) & ~V).astype(np.uint8)
        clean = cv2.inpaint(np.clip(R, 0, 255).astype(np.uint8), hole, 9, cv2.INPAINT_TELEA).astype(np.float32)
        rng = np.random.default_rng(by)
        grain = cv2.GaussianBlur(rng.normal(0, 3.0, hole.shape).astype(np.float32), (0, 0), 0.7)
        clean = np.where(hole[..., None] > 0, clean + grain[..., None], clean)

        # move it: centre on the rivet axis, scale down only if too wide
        width = cxb - cxa
        s = min(1.0, cfg["room"] / width)
        mid_src = (cxa + cxb) / 2 - x0
        mid_dst = cfg["centre"] - x0
        cy = R.shape[0] / 2
        M = np.float32([[s, 0, mid_dst - s * mid_src], [0, s, cy - s * cy]])
        size = (R.shape[1], R.shape[0])
        a2 = cv2.warpAffine(a.astype(np.float32), M, size, flags=cv2.INTER_LINEAR)
        F2 = cv2.warpAffine(F.astype(np.float32), M, size, flags=cv2.INTER_LINEAR)
        a2 *= ~V
        moved = clean * (1 - a2[..., None]) + F2 * a2[..., None]
        touched = hole.astype(bool) | (a2 > 0.01)
        img[sl] = np.where(touched[..., None], moved, keep)
        print(f"  board at y={by}: content {cxa}-{cxb}, centre {((cxa + cxb) / 2):.1f} -> {cfg['centre']}, scale {s:.3f}")
    return img


def pockets(rgb, alpha, protect):
    """Studio backdrop trapped inside the machine, between pipes.

    The cut-out only removed backdrop it could reach from the image edge, so
    pockets enclosed by pipework stayed. Invisible on cream, obvious on black.
    A pocket seeds where the render is light, unsaturated and smooth over 5px,
    after an opening wide enough to discard the thin bright streaks on chrome;
    it then grows a few pixels into its own soft shadowed rim.
    """
    bgr = np.clip(rgb, 0, 255).astype(np.uint8)
    lum = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    sat = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)[..., 1].astype(np.float32)
    m5 = cv2.blur(lum, (5, 5))
    s5 = np.sqrt(np.maximum(cv2.blur(lum * lum, (5, 5)) - m5 * m5, 0))
    seed = ((alpha > 0.5) & (lum > 185) & (sat < 45) & (s5 < 5) & ~protect).astype(np.uint8)
    seed = cv2.morphologyEx(seed, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(seed, connectivity=8)
    big = np.zeros(n, bool)
    big[1:] = st[1:, cv2.CC_STAT_AREA] >= 40
    region = big[lab].astype(np.uint8)
    m3 = cv2.blur(lum, (3, 3))
    s3 = np.sqrt(np.maximum(cv2.blur(lum * lum, (3, 3)) - m3 * m3, 0))
    rim = ((alpha > 0.05) & (lum > 140) & (sat < 60) & (s3 < 14) & ~protect).astype(np.uint8)
    for _ in range(4):
        region = cv2.dilate(region, np.ones((3, 3), np.uint8)) & rim
    return region.astype(bool)


def white_slivers(rgb, alpha, protect_tight, zone):
    """Near-white backdrop squeezed between rubble and the machine's frame.

    Too small or too tinted by the rubble's glow to pass the smoothness test
    in `pockets`, but whiter than anything the machine itself contains outside
    its plates and panels, which `protect_tight` covers.
    """
    bgr = np.clip(rgb, 0, 255).astype(np.uint8)
    lum = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    sat = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)[..., 1].astype(np.float32)
    white = ((alpha > 0.3) & (lum > 228) & (sat < 40) & ~protect_tight & zone).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(white, connectivity=8)
    keep = np.zeros(n, bool)
    keep[1:] = st[1:, cv2.CC_STAT_AREA] >= 12
    region = keep[lab].astype(np.uint8)
    rim = ((alpha > 0.05) & (lum > 175) & (sat < 70) & ~protect_tight & zone).astype(np.uint8)
    for _ in range(2):
        region = cv2.dilate(region, np.ones((3, 3), np.uint8)) & rim
    return region.astype(bool)


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
    stage_masks = [rounded_mask(shape, p, 0) for p in c["stages"]]

    # Slabs, stage panels and result boards are solid. The cut-out treated a
    # few light patches inside them (the counter of a C) as backdrop and
    # punched holes the glow showed through; inside them, take the render as is.
    objects = slabs | out_all | np.any(stage_masks, axis=0)
    opaque = (alpha > 0.5).astype(np.uint8)
    reach = np.zeros((H + 2, W + 2), np.uint8)
    outside = opaque.copy()
    cv2.floodFill(outside, reach, (0, 0), 2)
    holes = (outside == 0) & objects  # transparent, but enclosed by the object
    solid_objects = holes | (objects & (alpha > 0.5))
    rgb[holes] = img[holes]
    alpha[solid_objects] = 1.0

    if c["recentre"]:
        boards = [(p[0][0], p[0][1], p[1][0] - p[0][0], p[2][1] - p[0][1]) for p in c["outputs"]]
        # Each board is whole: where the old lettering ran into the bevel the
        # cut-out bit into the board's edge, so take each board's outline as
        # the hull of its opaque pixels and fill it from the render. Done
        # before recentring, so the lettering restored here moves with the rest.
        left = c["recentre"]["x"][0] - 22
        for k, (bx, by, bw, bh) in enumerate(boards):
            band = np.zeros(shape, bool)
            band[by + 1:by + bh - 1, left:bx + bw + 4] = True
            pts = cv2.findNonZero(((alpha > 0.5) & band).astype(np.uint8))
            hull = np.zeros(shape, np.uint8)
            cv2.fillPoly(hull, [cv2.convexHull(pts)], 1)
            fill = (hull > 0) & (alpha < 0.5)
            rgb[fill] = img[fill]
            alpha[hull > 0] = 1.0
            # the light gap below each board (to the next) is backdrop
            if k + 1 < len(boards):
                gap_top, gap_bottom = by + bh + 1, boards[k + 1][1] - 1
                alpha[gap_top:gap_bottom, left + 8:bx + bw + 6] = 0
        rgb = recentre_boards(rgb, img, boards, c["recentre"])

    # ---- clean the cut-out: drop trapped backdrop around the rubble and cables
    zone = poly_mask(shape, c["in_zone"])
    if "in_exclude" in c:
        zone &= ~poly_mask(shape, c["in_exclude"])
    cleaning = zone.copy()
    for z in c["clean_zones"]:
        cleaning |= poly_mask(shape, z)
    back = backdrop(img, cleaning & ~out_all & ~solid_objects, slabs)
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
    # ---- trapped backdrop between the pipes, anywhere in the machine
    protect = slabsP.copy()
    for p in c["outputs"] + c["stages"]:
        protect |= pad(rounded_mask(shape, p, 0))
    nx, ny, nw, nh = c["nameplate"]
    protect[ny + pt - 6:ny + pt + nh + 6, nx + pl - 6:nx + pl + nw + 6] = True
    ax_, ay_, aw_, ah_ = c["arrow_box"]
    protect[ay_ + pt:ay_ + pt + ah_, ax_ + pl:ax_ + pl + aw_] = True
    for (cx, cy, r) in c["keep_light"]["circles"]:
        cv2.circle(protect.view(np.uint8), (cx + pl, cy + pt), r, 1, -1)
    for (bx, by, bw, bh) in c["keep_light"]["boxes"]:
        protect[by + pt:by + pt + bh, bx + pl:bx + pl + bw] = True
    protect_tight = cv2.dilate(protect.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    protect = cv2.dilate(protect.astype(np.uint8), np.ones((9, 9), np.uint8)).astype(bool)
    sliver_zone = np.zeros((PH, PW), bool)
    for z in c["sliver_zones"]:
        sliver_zone |= pad(poly_mask(shape, z))
    trapped = pockets(RGB, A, protect) | white_slivers(RGB, A, protect_tight, sliver_zone)
    A = A * (1 - soft(trapped, 0.8))

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
    phases = {"in": slabsP if IN_LIGHT == "slabs" else slabsP | rubble}
    for k, p in enumerate(c["stages"]):
        m = pad(stage_masks[k])
        phases[f"s{k + 1}"] = cv2.dilate(m.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    so, sr = c["glow"]
    for ph, m in phases.items():
        kw = {"strength": IN_STRENGTH, "colour": IN_COLOUR, "lift": IN_LIFT} if ph == "in" else {}
        cv2.imwrite(f"{OUT}/glow-{art}-{ph}.png", glow_layer(m, RGB, A, so, sr, **kw))

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
        lit = glow_layer(m, RGB, A, so, sr, strength=WARM_STRENGTH, colour=WARM)
        seq["items"].append({"name": f"block{k + 1}", "box": crop(lit, f"block{k + 1}"), "at": beats[k]})

    print(art, "canvas", (PW, PH), "| backdrop px removed", int(back.sum()), "| pocket px removed", int(trapped.sum()), "| beats", beats)
    return {"size": [PW, PH], "offset": [pl, pt], "seq": seq}


if __name__ == "__main__":
    manifest = {art: run(art, c) for art, c in ART.items()}
    with open(f"{OUT}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1)
