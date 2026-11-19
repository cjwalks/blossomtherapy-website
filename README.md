# Blossom Therapy & Supports website

A static site hosted on Netlify. Every push to `main` deploys automatically.

- `site/` is the published website (Netlify serves only this folder; see `netlify.toml`)
- `tools/build.py` generates the pages. Edit the text there, run `python3 tools/build.py`, and commit.
- `tools/assets.py` lists every image and PDF from the old GoDaddy site

## Photos and files: how to get them in

**Option 1: GitHub website (no software needed)**
1. Open github.com/cjwalks/blossomtherapy-website, go into `site/assets/img/`, then **Add file > Upload files**.
2. Drag the photos in, then click **Commit changes**.
3. Tell Claude what each photo is (or name them as below). Claude rebuilds the pages to use them.

**Option 2: send them in chat.** Attach the photos to a Claude message. Claude adds them and pushes.

### Naming
- Keep the old file names for photos already on the site (list in `tools/assets.py`, e.g. `IMG_8918.jpeg` = Emma). The site switches to the local copy automatically.
- New photos: `caite.jpg` (team photo), `physio.jpg` (services), `wattle-calendar.png`, `banksia-calendar.png` (current term).
- Size: anything up to 2–3 MB is fine. Landscape for services, square or portrait for team photos.

### Before GoDaddy is cancelled
Until a file is uploaded here, the site loads it from GoDaddy's servers, and those links die when GoDaddy is cancelled. Upload every image and the 5 PDFs listed in `tools/assets.py` first (gallery photos go in as gallery-01.png to gallery-11.png). PDFs go in `site/assets/files/` with the names listed there.

## Markers in the HTML
- `HALAXY EMBED`: paste the Halaxy form embed code (5 spots)
- `CONFIRM`: facts to check
- `TODO`: waiting on photos or information
- `LATER`: where the online-booking link goes when booking is switched on

## Netlify credits
Each production deploy uses 15 of 300 free monthly credits, so batch your changes (about 20 deploys a month).
