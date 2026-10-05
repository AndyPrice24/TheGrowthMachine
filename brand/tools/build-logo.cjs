const fs = require('fs');
const svgpath = require('svgpath');

const raw = fs.readFileSync('wordmark_raw.svg', 'utf8');
const ds = [...raw.matchAll(/ d="([^"]+)"/g)].map(m => m[1].replace(/\s+/g, ' '));
// potrace coords -> original 1600x720 pixel space
const toPx = d => svgpath(d).matrix([0.025, 0, 0, -0.025, 0, 720]).abs().round(2).toString();

// split every path into subpaths, bucket by row using each subpath's y-range
const rows = { the: [], growth: [], machine: [] };
for (const d of ds) {
  const abs = toPx(d);
  const subs = abs.split(/(?=M)/).filter(s => s.trim());
  for (const s of subs) {
    const ys = [];
    svgpath(s).iterate((seg) => {
      for (let i = 2; i < seg.length; i += 2) ys.push(seg[i]);
    });
    const ymid = (Math.min(...ys) + Math.max(...ys)) / 2;
    const row = ymid < 200 ? 'the' : ymid < 520 ? 'growth' : 'machine';
    rows[row].push(s.trim());
  }
}

// the gear, redrawn as exact geometry from measurements of the source
const C = { x: 622.6, y: 364.5 };
const Rt = 79.2, Rr = 66.4;          // tip and root radii
const halfTip = 9.85, halfRoot = 13.0; // half tooth width, linear, at tip and root
const teeth = 12, first = 12;          // degrees; tooth centres at 12 + 30k
const phT = Math.asin(halfTip / Rt), phR = Math.asin(halfRoot / Rr);
const pt = (r, a) => [C.x + r * Math.cos(a), C.y + r * Math.sin(a)].map(v => +v.toFixed(2));
let g = '';
for (let k = 0; k < teeth; k++) {
  const th = (first + 360 / teeth * k) * Math.PI / 180;
  const next = (first + 360 / teeth * (k + 1)) * Math.PI / 180;
  const a = pt(Rr, th - phR), b = pt(Rt, th - phT), c = pt(Rt, th + phT), d = pt(Rr, th + phR), e = pt(Rr, next - phR);
  if (k === 0) g += `M${a}`;
  g += `L${b}A${Rt} ${Rt} 0 0 1 ${c}L${d}A${Rr} ${Rr} 0 0 1 ${e}`;
}
g += 'Z';

const out = {
  the: rows.the.join(''),
  growth: rows.growth.join(''),
  machine: rows.machine.join(''),
  gear: g,
  gearCentre: C,
};
fs.writeFileSync('logo-paths.json', JSON.stringify(out));
console.log('subpaths', Object.fromEntries(Object.entries(rows).map(([k, v]) => [k, v.length])));

const viewBox = '96 92 1409 528';
const svg = (wm, gear) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}" role="img" aria-labelledby="tgm-title">
  <title id="tgm-title">The Growth Machine</title>
  <g id="wordmark" fill="${wm}">
    <path id="the" d="${out.the}"/>
    <path id="growth" d="${out.growth}"/>
    <path id="machine" d="${out.machine}"/>
  </g>
  <path id="gear" fill="${gear}" d="${out.gear}"/>
</svg>
`;
fs.writeFileSync('logo-black.svg', svg('#000000', '#000000'));
fs.writeFileSync('logo-white.svg', svg('#FFFFFF', '#FFFFFF'));
// full-canvas version for pixel comparison against the source
fs.writeFileSync('compare.svg', svg('#000000', '#000000').replace(viewBox, '0 0 1600 720').replace('<svg ', '<svg width="1600" height="720" '));
console.log('bytes', fs.statSync('logo-black.svg').size);
