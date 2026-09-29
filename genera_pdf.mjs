#!/usr/bin/env node
/*
 * Genera i PDF di slide e dispense con Chrome headless (puppeteer-core).
 *
 * presentazioni/T07_xxx.html  -> presentazioni/T07_xxx.pdf   (16:9, una pagina per slide)
 * dispense/<dir>/T07_xxx.html -> dispense/<dir>/T07_xxx.pdf  (A4)
 *
 * Viene eseguito dalla GitHub Action sulla copia del sito, dopo la potatura,
 * quindi produce solo i PDF del materiale gia' pubblicato.
 *
 * Uso:
 *   npm install --no-save puppeteer-core
 *   node genera_pdf.mjs            # tutti i PDF
 *   node genera_pdf.mjs T01 T02    # solo le lezioni indicate
 *
 * Chrome: variabile CHROME, altrimenti i percorsi standard di Linux e macOS.
 */

import fs from "node:fs";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";
import puppeteer from "puppeteer-core";

const BASE = path.dirname(fileURLToPath(import.meta.url));
const CHROME = [
  process.env.CHROME,
  "/usr/bin/google-chrome",
  "/usr/bin/google-chrome-stable",
  "/usr/bin/chromium",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
].find((p) => p && fs.existsSync(p));

if (!CHROME) {
  console.error("ERRORE: Chrome non trovato (impostare la variabile CHROME).");
  process.exit(1);
}

const filtro = new Set(process.argv.slice(2));
const RE_LEZIONE = /^[TL]\d{2}_.*\.html$/;
const scelto = (f) => RE_LEZIONE.test(f) && (filtro.size === 0 || filtro.has(f.slice(0, 3)));

const presentazioni = fs.readdirSync(path.join(BASE, "presentazioni"))
  .filter(scelto).sort().map((f) => path.join(BASE, "presentazioni", f));
const dispense = ["frontali", "laboratori"].flatMap((d) => {
  const dir = path.join(BASE, "dispense", d);
  return fs.existsSync(dir)
    ? fs.readdirSync(dir).filter(scelto).sort().map((f) => path.join(dir, f))
    : [];
});

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ["--no-sandbox", "--disable-gpu"],
});

let ok = 0;
const totale = presentazioni.length + dispense.length;

async function stampa(url, pdf, opzioni, viewport = { width: 1280, height: 720 }) {
  const page = await browser.newPage();
  try {
    await page.setViewport(viewport);
    await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: pdf, printBackground: true, ...opzioni });
    ok++;
    console.log(`  ✓ ${path.relative(BASE, pdf)}`);
  } catch (e) {
    console.error(`  ✗ ${path.relative(BASE, pdf)}: ${e.message}`);
  } finally {
    await page.close();
  }
}

// Slide: reveal.js impagina per la stampa con ?print-pdf. Si stampa una copia
// temporanea nella stessa cartella (percorsi relativi a vendor/) con i
// frammenti mostrati tutti insieme: una pagina per slide.
for (const html of presentazioni) {
  const tmp = path.join(path.dirname(html), "_stampa_" + path.basename(html));
  const testo = fs.readFileSync(html, "utf8")
    .replace("Reveal.initialize({", "Reveal.initialize({\n            pdfSeparateFragments: false,")
    // la vecchia regola di stampa rimpicciolisce il testo a 14px: in PDF vale la dimensione a schermo
    .replace(/(@media print\s*{\s*)\.reveal \.slides\s*{\s*font-size:\s*14px;\s*}/, "$1");
  fs.writeFileSync(tmp, testo);
  try {
    await stampa(pathToFileURL(tmp).href + "?print-pdf", html.replace(/\.html$/, ".pdf"),
      { preferCSSPageSize: true });
  } finally {
    fs.rmSync(tmp, { force: true });
  }
}

for (const html of dispense) {
  await stampa(pathToFileURL(html).href, html.replace(/\.html$/, ".pdf"), {
    format: "A4",
    margin: { top: "18mm", bottom: "18mm", left: "16mm", right: "16mm" },
  });
}

await browser.close();
console.log(`  PDF generati: ${ok}/${totale}`);
process.exit(ok === totale ? 0 : 1);
