// Pre-launch gate. Run with `npm run launch-check` (it builds first).
// Fails while the build contains anything that must not reach the live site:
//   - a <Placeholder> (content that does not exist yet)
//   - a noindex tag (LAUNCHED still false in src/site.ts)
//   - an internal link to a page that does not exist
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, relative } from "node:path";

const dist = new URL("../dist/", import.meta.url).pathname;
const redirectsFile = new URL("../public/_redirects", import.meta.url).pathname;

const htmlFiles = [];
(function walk(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p);
    else if (name.endsWith(".html")) htmlFiles.push(p);
  }
})(dist);

const redirected = new Set(
  existsSync(redirectsFile)
    ? readFileSync(redirectsFile, "utf8").split("\n").map((l) => l.trim().split(/\s+/)[0]).filter((s) => s && !s.startsWith("#"))
    : [],
);

const resolves = (path) => {
  if (redirected.has(path)) return true;
  const clean = path.replace(/\/$/, "");
  return [join(dist, clean, "index.html"), join(dist, clean + ".html"), join(dist, clean)].some(
    (p) => existsSync(p) && statSync(p).isFile(),
  ) || (clean === "" && existsSync(join(dist, "index.html")));
};

const problems = [];
for (const file of htmlFiles) {
  const page = "/" + relative(dist, file);
  const html = readFileSync(file, "utf8");
  for (const m of html.matchAll(/data-placeholder="([^"]*)"/g)) problems.push(`${page}: placeholder still in place: ${m[1]}`);
  if (/<meta name="robots" content="noindex/.test(html)) problems.push(`${page}: noindex is on (set LAUNCHED in src/site.ts)`);
  for (const m of html.matchAll(/href="(\/[^"#?]*)/g)) {
    const target = m[1];
    if (target.startsWith("//") || target.startsWith("/_astro/") || target.startsWith("/favicon")) continue;
    if (!resolves(target)) problems.push(`${page}: link to a page that does not exist: ${target}`);
  }
}

const unique = [...new Set(problems)];
if (unique.length) {
  console.error(`\nNot ready to launch. ${unique.length} problem(s):\n`);
  for (const p of unique) console.error("  - " + p);
  console.error("");
  process.exit(1);
}
console.log(`Launch check passed: ${htmlFiles.length} page(s), no placeholders, no broken internal links, indexable.`);
