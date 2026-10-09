/*
 * The two audiences the homepage splits into after "The awkward stage".
 *
 * One page, three addresses (decided 9 October 2026): `/` shows the shared
 * opening and stops at the choice; `/b2b` and `/ecommerce` show the same
 * opening, then everything below the choice written for that audience.
 * Outbound emails link straight to a track, so a prospect never has to
 * answer a question Andrew already knows the answer to.
 *
 * Everything here that differs between the two is copy. The machine artwork
 * is shared; only the words beside it change.
 */
import type { StepCopy } from "../components/MachineRun.astro";

export type TrackId = "b2b" | "ecommerce";

export interface Track {
  id: TrackId;
  path: string;
  meta: { title: string; description: string };
  card: { kicker: string; title: string; text: string; cta: string; switchTo: string };
  machine: StepCopy[];
  inOut: { inward: string; outward: string };
  /* who is introduced first in "Who you actually get" */
  leads: "andrew" | "tarren";
}

export const tracks: Record<TrackId, Track> = {
  ecommerce: {
    id: "ecommerce",
    path: "/ecommerce",
    meta: {
      title: "Fractional CMO and Ecommerce Lead | The Growth Machine",
      description:
        "Fractional CMO and ecommerce leadership for consumer brands, from people who've founded and run their own. Sharper customer, stronger offer, data-led spend.",
    },
    card: {
      kicker: "Ecommerce and consumer brands",
      title: "You sell online, on Amazon or into retail.",
      text: "Sharper customer, stronger offer. Data-led decisions on channels, creative and budget, so you scale what pays.",
      cta: "For ecommerce brands",
      switchTo: "Switch to ecommerce",
    },
    machine: [
      { name: "What comes in", text: "Rising ad costs, a flat conversion rate, thin contribution margin, marketplace fees eating the profit, a founder still approving every ad." },
      { name: "Diagnose", text: "We pull the numbers apart order by order and channel by channel, and rank every problem by what it costs you." },
      { name: "Design", text: "Sharper customer, stronger offer, and a channel and budget plan built on what each order actually earns." },
      { name: "Execute", text: "We run it with your team: creative, campaigns, listings and retention. Tested, measured, and cut when it doesn't pay." },
      { name: "Embed", text: "Reporting, playbooks and owners, so the brand keeps growing profitably when we step back." },
      { name: "What comes out", text: "More orders that make money, customers who come back, and growth that runs on profit, not spend." },
    ],
    inOut: {
      inward:
        "Where margin slips between the ad and the doorstep: fees, returns, stock and fulfilment, and the processes and team behind them.",
      outward:
        "Who your customer really is, a sharper offer, the channels and creative that pay their way, and the budget to scale what works.",
    },
    leads: "tarren",
  },
  b2b: {
    id: "b2b",
    path: "/b2b",
    meta: {
      title: "Fractional CRO, CMO and GTM for B2B | The Growth Machine",
      description:
        "Fractional CRO, CMO and GTM leadership for B2B, SaaS and service businesses, from people who've founded and run their own. We judge growth by profit.",
    },
    card: {
      kicker: "B2B, SaaS and service businesses",
      title: "You need a CRO, CMO or GTM lead, but not full-time.",
      text: "Go-to-market, pipeline, sales process and pricing. With the numbers your board needs to see.",
      cta: "For B2B businesses",
      switchTo: "Switch to B2B",
    },
    machine: [
      { name: "What comes in", text: "A pipeline that won't grow, a go-to-market nobody owns, deals that stall, pricing set years ago, a founder still closing every big deal." },
      { name: "Diagnose", text: "We read the whole commercial engine, from first touch to renewal, and rank every problem by what it costs you." },
      { name: "Design", text: "A go-to-market plan with a few priorities: who you sell to, how you win them, what you charge, and who owns each number." },
      { name: "Execute", text: "We run it with your team: the sales process, pipeline reviews, campaigns and hires. In the business, not in a deck." },
      { name: "Embed", text: "Playbooks, dashboards and people who own them, so the engine keeps running when we step back." },
      { name: "What comes out", text: "A pipeline you can forecast, revenue that compounds, and margins that hold as you grow." },
    ],
    inOut: {
      inward:
        "Where margin slips between the sale and the delivery, which processes slow the team down, which decisions still wait for you, and whether the team is shaped for the next stage.",
      outward:
        "Who you should be selling to, the offer and the price, how you go to market, and a pipeline that turns it into revenue you can forecast.",
    },
    leads: "andrew",
  },
};

/* the order the cards appear in, on every version of the page */
export const trackOrder: TrackId[] = ["ecommerce", "b2b"];
