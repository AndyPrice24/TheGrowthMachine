// @ts-check
import { defineConfig, fontProviders } from "astro/config";

// Static output: the site is plain files, deployable to any static host.
// `site` is the canonical origin. Apex is canonical; www will redirect to it.
export default defineConfig({
  site: "https://thegrowthmachine.co",

  // Fonts are the open-licence files from Fontsource's npm packages, installed
  // with everything else and served from our own domain. The build never
  // downloads a font and a visitor's browser never asks Google for one. Astro
  // generates metric-matched fallbacks so text does not jump when a font lands.
  // Latin subset only: it covers English and Afrikaans, including accents.
  fonts: [
    {
      // Headlines. Heavy, like GROWTH in the logo.
      provider: fontProviders.local(),
      name: "Archivo Black",
      cssVariable: "--font-display",
      fallbacks: ["Arial Black", "sans-serif"],
      options: {
        variants: [
          {
            src: ["./node_modules/@fontsource/archivo-black/files/archivo-black-latin-400-normal.woff2"],
            weight: 400,
            style: "normal",
          },
        ],
      },
    },
    {
      // Running text and UI. Variable, so one file covers every weight.
      provider: fontProviders.local(),
      name: "Archivo",
      cssVariable: "--font-body",
      fallbacks: ["sans-serif"],
      options: {
        variants: [
          {
            src: ["./node_modules/@fontsource-variable/archivo/files/archivo-latin-wght-normal.woff2"],
            weight: "100 900",
            style: "normal",
          },
        ],
      },
    },
    {
      // Labels. Light and widely spaced, like THE and MACHINE in the logo.
      provider: fontProviders.local(),
      name: "Jost",
      cssVariable: "--font-label",
      fallbacks: ["sans-serif"],
      options: {
        variants: [
          {
            src: ["./node_modules/@fontsource/jost/files/jost-latin-400-normal.woff2"],
            weight: 400,
            style: "normal",
          },
        ],
      },
    },
  ],
});
