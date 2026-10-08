# The Growth Machine

Marketing site for The Growth Machine, a two-person fractional executive firm
(Andrew Price and Tarren Price). Domain: **thegrowthmachine.co**.

The site exists to get a qualified founder onto a 30-minute call. Everything is
subordinate to that.

## Source briefs

- `docs/briefs/build-handover.md`: the build handover. It has the revenue and
  margin positioning, strict rules and the technical spec.
- `docs/briefs/website-developer-handover-v1.pdf`: the developer handover v1.
  It has page-by-page copy, wireframes, art direction and the photography brief.

They conflicted in many places. Andrew decided each conflict, and this file
records the outcome. Where this file and a brief disagree, this file wins.

## Settled

- **This repo is completely separate from Groove (MGN8).** Nothing here
  touches that repo, and nothing there touches this one.
- **The name is final:** The Growth Machine. The domain is `thegrowthmachine.co`,
  always written in full and in lowercase. `thegrowthmachine.com` belongs to
  an unrelated company.
- **Stack: Astro 7, static output, no CMS.** Andrew edits through Claude, so
  content lives as files in this repo.
- **Hosting: Cloudflare.** The domain is registered at GoDaddy. DNS moves to
  Cloudflare, so the site, email records and analytics are managed in one
  place. Vercel's free plan does not allow commercial sites.
- **Analytics: Cloudflare Web Analytics, page views only.** It sets no
  cookies, so the site needs no consent banner. Never add GA or a pixel
  without an explicit decision.
- **Market: based in South Africa, selling locally and internationally.**
  Use British/South African spelling. Write for an international reader;
  SEO targets South African search terms first. `lang="en-ZA"`.
- **The framework is revenue and margin.** Margin includes money won back
  through processes and team structure, not only COGS and fees. The pairing
  is "two operators, both sides of the number"; never claim that each
  partner owns one side exclusively.
- **Offer shape: one way in, two ways to continue.** First a paid deep dive
  for a fixed fee agreed before starting; very large jobs are negotiated.
  Its output is a ranked view of what is holding the business back, with the
  reasoning behind it. After that, either a defined project with a handover
  (strategy, plan, system, AI tool) or ongoing embedded leadership and
  execution. Almost every client gets direction from both partners, with one
  or both doing the work.
- **Working engagement names:** the Machine Check (deep dive), the Build
  (project with a handover), the Growth Office (ongoing). Not final.
- **The method is four stages: Diagnose, Design, Execute, Embed** (Andrew's
  words, from his machine render). "Find the leak, then the lever." is the
  provisional name over them. The engagements are how the method is bought.
- **Set the client up not to need us.** A stated principle of the service,
  not a caveat. When a client is ready to hire permanently, we help them hire
  and hand over.
- **Primary buyer: founders and CEOs.** Investors and boards are secondary
  and get no path of their own.
- **Sales motion: Andrew sells outbound.** He contacts companies that are
  hiring a CRO, CMO, GTM lead or entrepreneur in residence and pitches this
  instead of a full-time hire. The site's first job is to back up that pitch
  for someone arriving from his email.
- **Positioning: founders, judged by profit (decided 8 October 2026).** Both
  Andrew and Tarren have founded and run companies on their own capital. A
  CMO owns the market and a CRO owns the revenue; a founder owns all of it.
  That is the lead claim, ahead of seniority or headcount. Never belittle the
  CRO or CMO role: those are the seats being sold. The line is "we fill the
  seat, and think like the person who owns all of it". The page also serves the healthy business that
  wants its next revenue, not only the one with leaks, so copy should not
  read purely as a repair job.
- **Launch scope:** Home, How we work and the three engagement pages, Who we
  are, Before you hire, and booking. The Ecommerce and Startups paths follow.
  No Insights section until four to six real articles exist.
- **Photography: AI likenesses of Andrew and Tarren, by their decision.** The
  homepage hero is an AI-synthesised photo of the two of them
  (`src/assets/hero/andrew-and-tarren.webp`, 8 October 2026). Andrew confirmed
  it is a faithful likeness, so a founder meeting them on a call meets the
  people in the picture. The rule that survives: never stock photos of other
  people standing in for them, and never a likeness they have not approved.
  The file is Andrew's 2000px upscale of the 1536px original, chosen over it
  after a side-by-side check (8 October 2026). A 3000px version would be
  fully sharp on a large retina screen; swap it in if one is made. It is
  encoded at quality 82: the source is already lossy, and the default
  quality visibly smeared skin and hair. Bios
  keep the monogram placeholder until portraits are supplied.

## Design system: direction C

Chosen 6 October 2026 from three mockups. Cream and near-black sections
alternate full-bleed down the page; one bright orange; type taken from the
logo itself.

- **Tokens live in `src/styles/tokens.css` and nowhere else.** No hex values
  in components. The one exception is `theme-color` in the base layout,
  because a meta tag cannot read a CSS variable.
- **Torch (#FF2715) on cream is 3.3:1: graphics only.** The gear, buttons
  (with ink text, 5.2:1), rules and the focus ring. Never text on cream. On
  ink it passes for text.
- **Type:** Archivo Black for headlines (heavy, like GROWTH), Archivo for
  running text, Jost for labels set uppercase and widely spaced (like THE and
  MACHINE). Self-hosted from Fontsource's npm packages through Astro's fonts
  feature with the `local` provider; Latin subset only.
- **The gear.** It is the only colour in the logo, and it moves: one turn on
  page load, two teeth on hover, and scroll-linked in the revenue/margin
  diagram. Never continuous. With reduced motion it does not move.
- **Gear imagery outside the logo: two approved exceptions, nothing else.**
  The `Machine` diagram uses the logo's own gear as the mechanism that revenue
  and margin feed. And `MachineRun` (below) is Andrew's own machine render.
- **The machine render is the page's centrepiece (decided 6 October 2026).**
  Andrew judged the typographic version of the process "too stale and too
  boring" and chose his photoreal machine instead, knowingly overriding the
  PDF's ban on gears, rockets and rising charts for this one element. Its
  costs were mitigated rather than ignored:
  - The 2.4MB PNGs live in `src/assets/machine/` and are built into AVIF and
    WebP at two widths each (70 to 260KB), loaded lazily, so the page does not
    pay for them until the reader is near.
  - The render's nameplate carried an AI approximation of the logo. A vector
    nameplate with the real logo is laid over it as a warm-lit lightbox: lit
    from the first moment the machine is seen, never faded with the rest of
    it. Its gear turns as the machine runs.
  - Text baked into the render is too small to read on a phone, so every step
    is also live text beside or beneath it. The image has full alt text.
  - It is cut out of its studio backdrop (`brand/tools/cutout-machine.py`,
    then `brand/tools/machine-glows.py`; originals in `brand/machine/`) so the
    machine and its rubble sit on the page rather than in a picture box. The
    rubble that ran off the render's left edge is mirrored outward and thinned
    so it crumbles away; the tank hub cut by the right edge fades out.
  - **How we work is an ink section (decided 7 October 2026).** Andrew chose
    black over cream: the red backlights read as real light.
  - As the reader scrolls, the machine fades back (to 60%, raised from 50% at
    Andrew's request) and one phase at a time is backlit in torch red: every
    slab and piece of rubble going in, then each stage panel. Each glow
    follows the object's own outline, and the four stage outlines are
    identical so every stage looks the same when it lights. No boxes.
  - What comes out is a timed sequence: the chart's arrow climbs at a steady
    rate, each bar lights as the arrow passes it, and each result block lights
    with its bar (bottom up on desktop, left to right on a phone), the fifth
    with the arrow's tip. All stay lit; scrolling back and in again replays it.
    Every time it plays, the page holds at the end of the section until it
    finishes; reaching the end mid-sequence locks scrolling outright, since
    trackpad and touch momentum carry past anything softer. Armed only by
    arriving from above; never with reduced motion. Positions and
    timings come from `src/assets/machine/manifest.json`.
  - On desktop the render drew most result boards' icon and text off-centre;
    `machine-glows.py` recentres each between its rivets.
  - The render itself never moves. Reduced motion, or no JavaScript: no
    pinning, no fading, every step listed.
- **The logo below 200px wide** loses its hairline THE and MACHINE. 200px is
  the default; the phone header goes to 156px, and 136px under 400px.
  `public/favicon.svg` is a simplified 8-tooth gear, because the full gear
  turns into a blob at 16px.

## Components

`src/components/`, twelve so far against a ceiling of fourteen. A page that
seems to need another one usually needs a variant of an existing one.

Logo · Header · Footer · Button · Section · Hero · Machine · MachineRun ·
Card (variants: path, symptom, engagement) · BioBlock · Placeholder · CtaBand

## Content that does not exist yet

- **`<Placeholder needs="…">`** marks anything missing: bios, career proof,
  portraits. It is visible, honest about being unfinished, and never filled
  with invented names, numbers or quotes.
- **`npm run launch-check`** builds the site and fails while any placeholder,
  any broken internal link, or the noindex tag remains. It is the to-do list
  for launch.
- **`src/site.ts` `LAUNCHED`** stays false until launch-check passes. While it
  is false, every page carries noindex, so a preview cannot be indexed with
  placeholders on it.

## Still open

Bios and career results (from Andrew and Tarren) · final engagement and method
names · booking tool (Cal.com recommended, not yet confirmed) · Path B label
(working: Startups) · email addresses on the domain.

## Rules both briefs agree on

- **Never invent proof.** No client names, logos, quotes, percentages or
  results, not even as placeholders. Fake proof that reaches production is
  the one failure this site cannot recover from.
- **Never invent credentials.** Bios, titles, companies, dates and outcomes
  come from Andrew and Tarren.
- **Two people. Never imply more.** No team, roster or network. But the
  count does not lead: the hero photo shows two people and the copy says
  "founders"; "two" is said where being small reads as a promise (Who you
  actually get, the closing call to action), not in the opening.
- **No pricing on the site.** The call is the qualifier.
- **No newsletter pop-up and no chat widget** at launch.
- **No stock language:** unlock, supercharge, 10x, secret weapon, bespoke,
  innovative solutions, holistic synergies, end-to-end.
- **No spatial metaphors** for the framework: never "inside-out", "outside-in"
  or similar. Revenue and margin need no help.
- **Never a 2x2.** Revenue and margin are two inputs to one machine, not four
  quadrants.

## Working rules

- Astro is on v7, which is newer than most training data. Check
  `node_modules/astro/` and the dev server's warnings before relying on a
  convention from memory.
- Every change must pass `npm run build` and `npm run check` before it is
  pushed.
- **Fonts:** Astro's `google` provider needs `fonts.google.com`, which the
  cloud build environment blocks, and the `npm` provider still fetches files
  from a CDN. The `local` provider pointing at files in `node_modules` needs no
  network at all, so builds are reproducible anywhere.
