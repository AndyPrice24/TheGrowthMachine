# The Growth Machine

Marketing site for The Growth Machine, a two-person fractional executive firm
(Andrew Price and Tarren Price). Domain: **thegrowthmachine.co**.

**Status: the brief is being reconciled.** Two source briefs exist and they
disagree on the core argument, the offer, the look and parts of the stack.
Until this file is replaced with the merged brief, build nothing that depends
on an unsettled decision: no page copy, no design tokens, no components.

## Source briefs

- `docs/briefs/build-handover.md`: the build handover. It has the revenue and
  margin positioning, strict rules and the technical spec.
- `docs/briefs/website-developer-handover-v1.pdf`: the developer handover v1.
  It has page-by-page copy, wireframes, art direction and the photography brief.

Neither one wins by default. Every conflict between them is decided by the
owners and recorded here.

## Settled

- **This repo is completely separate from Groove (MGN8).** Nothing here
  touches that repo, and nothing there touches this one.
- **The name is final:** The Growth Machine. The domain is `thegrowthmachine.co`,
  always written in full and in lowercase. `thegrowthmachine.com` belongs to
  an unrelated company.
- **Stack: Astro, static output, no CMS.** Andrew edits through Claude, so
  content lives as files in this repo.
- **Hosting: Cloudflare.** The domain is registered at GoDaddy. DNS moves to
  Cloudflare, so the site, email records and analytics are managed in one
  place.
- **Analytics: Cloudflare Web Analytics, page views only.** It sets no
  cookies, so the site needs no consent banner. Never add GA or a pixel
  without an explicit decision.
- **Market: based in South Africa, selling locally and internationally.**
  Use British/South African spelling. Write for an international reader;
  SEO targets South African search terms first.
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
  or both doing the work. Engagement names are not final.
- **Working method name: "Find the leak, then the lever."** Provisional
  until refined.
- **Set the client up not to need us.** A stated principle of the service,
  not a caveat.
- **Primary buyer: founders and CEOs.** Investors and boards are secondary
  and get no path of their own.
- **No photography exists.** Use designed placeholders until a shoot
  happens. Never use stock photos of other people standing in for Andrew and
  Tarren, and never use AI likenesses of them.
- **The logo contains a gear.** No other gear or cog imagery anywhere on the
  site.
- **Sales motion: Andrew sells outbound.** He contacts companies that are
  hiring a CRO, CMO, GTM lead or entrepreneur in residence and pitches this
  instead of a full-time hire. The site's first job is to back up that pitch
  for someone arriving from his email.

## Still open

Engagement names · launch scope · booking tool · the look (mockups pending)
· bios and career proof · Path B label.

## Rules both briefs agree on

- **Never invent proof.** No client names, logos, quotes, percentages or
  results, not even as placeholders. Fake proof that reaches production is
  the one failure this site cannot recover from.
- **Never invent credentials.** Bios, titles, companies, dates and outcomes
  come from Andrew and Tarren.
- **Two people. Say two.** Never imply a team, a roster or a network.
- **No pricing on the site.** The call is the qualifier.
- **No newsletter pop-up and no chat widget** at launch.
- **No stock language:** unlock, supercharge, 10x, secret weapon, bespoke,
  innovative solutions, holistic synergies, end-to-end.

## Working rules

- Astro is on v7, which is newer than most training data. Check
  `node_modules/astro/` and the dev server's warnings before relying on a
  convention from memory.
- Every page must build and pass `npm run check` before it is pushed.
