# Brand assets

- `logo-source.png`: the logo as supplied (raster, 1600×720). The reference.
- `logo-black.svg`, `logo-white.svg`: the vector logo, traced from the source.

## How the vector was made

There was no original vector, so this one is reconstructed:

- **The lettering** is traced from the source with potrace at 4× resolution.
- **The gear** is not traced. It is redrawn as exact geometry from measurements
  of the source: 12 teeth, 30° apart, the first centred at 12°, tip radius 79.2,
  root radius 66.4, and straight tapered sides. A traced gear would be slightly
  irregular, and an irregular gear wobbles when it spins.

Rendered at 1600×720 and compared pixel by pixel with the source, the two
differ only along edges, by no more than 1px anywhere.

The SVG keeps the gear as its own element (`#gear`), so it can be coloured and
rotated independently. Rotate it around (622.6, 364.5) in the SVG's coordinates.

`tools/build-logo.cjs` is the script that assembled the SVG, kept for reference.

## The machine render

`brand/machine/machine-desktop-original.png` (1448×1086) and
`machine-mobile-original.png` (941×1672) are the raster layers extracted from
Andrew's `growth-machine-desktop.svg` and `growth-machine-mobile.svg`.

`src/assets/machine/` holds the transparent cut-outs the site uses, made by
`tools/cutout-machine.py` (run from the repo root; needs `opencv-contrib-python`
and `numpy`). It takes the backdrop that reaches the image edge as background,
treats drawn outlines as walls so light plates stay solid, cuts everything
below the floor line, and removes the grey fringe from soft edges. Two plates
at the very top are declared solid by hand in that script. The rest of those
files (glow overlays, a spinning cog) was not used: `MachineRun` replaces it
with an aligned spotlight, a vector nameplate carrying the real logo, and live
text. To change the render, replace the PNG; the build regenerates the web
formats. If the composition moves, the plate, rivet and region coordinates at
the top of `MachineRun.astro` must move with it.
