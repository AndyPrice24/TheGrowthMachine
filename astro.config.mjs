// @ts-check
import { defineConfig } from "astro/config";

// Static output: the site is plain files, deployable to any static host.
// `site` is the canonical origin. Apex is canonical; www will redirect to it.
export default defineConfig({
  site: "https://thegrowthmachine.co",
});
