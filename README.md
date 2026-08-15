# PDFzen — Private PDF & Image Tools (browser extension)

Open-source Chrome/Edge extension that launches PDFzen's free, private, **100% in-browser**
PDF and image tools. Your files are processed on your device and **never uploaded** to any server.

> No account. No upload. No watermark. Everything runs locally in the browser.

## Why this exists

Most "free" PDF sites upload your files to their servers. PDFzen does the opposite: every tool
(decoding, compression, conversion, signing) runs client-side with JavaScript. This extension is a
tiny, auditable launcher that deep-links to those tools — there is no tracking, no network call, and
nothing leaves your machine.

## Tools it opens

- **Merge & organize** — merge, split, rotate, reorder, delete pages, add page numbers
- **Convert** — PDF↔Word, PDF→Excel, PDF→JPG/PNG, PDF→text, JPG/PNG→PDF
- **Compress** — shrink PDFs for email / upload limits
- **Protect & sign** — password protect, unlock, sign, redact, watermark
- **Image tools** — HEIC→JPG, compress, resize, WebP→PNG, SVG→PNG, remove background

All tools live at **https://aitoolnavigation.top**.

## Install

### From source (unpacked)
1. Download / clone this repo.
2. Chrome → `chrome://extensions` → enable **Developer mode** (top-right).
3. **Load unpacked** → select the `extension/` folder.
4. Click the PDFzen icon, pick a tool.

### From the Chrome Web Store
Coming soon. (Publishing needs a one-time $5 developer fee — see `publish.ps1` / `publish.sh` for the zip step.)

## For developers

The extension is a static `manifest.json` + `popup.html` + `popup.js`. The popup only opens tabs to
the live tools; it requests **no permissions** and makes **no network requests**. Fork it, audit it,
rebrand it — it's MIT.

## Publish (maintainer)

```bash
# build the zip, then upload to the Chrome Web Store
cd extension && zip -r ../pdfzen-extension.zip . -x "*.py"
```

Or push this source to GitHub (one command):

```powershell
./publish.ps1      # Windows
./publish.sh       # macOS / Linux
```

## License

MIT — see [LICENSE](LICENSE).
