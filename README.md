# PyMovie

Personal fork of **PyMovie**, a desktop application for extracting lightcurves from astronomical video data.

This repository exists for my own workflow and experiments. The original project and the core application belong to **Bob Anderson**, and this fork is maintained with respect for that work.

## Credit

- Original project: [bob-anderson-ok/pymovie](https://github.com/bob-anderson-ok/pymovie)
- Original author: **Bob Anderson**
- This fork is a personal customization branch, not the official upstream project

If you are looking for the canonical project, upstream should always be your first reference.

## What PyMovie Does

PyMovie is built for occultation and related astronomical video work. It focuses on practical frame-by-frame measurement and lightcurve extraction, with strong support for shaky or imperfect data.

Main capabilities in this fork include:

- lightcurve extraction from video/image sequences
- aperture photometry with static and dynamic masks
- timestamp extraction and export
- support for AVI, MOV, SER, ADV, AAV, FITS-folder workflows, and related calibration utilities
- CSV export for downstream analysis
- bundled PDF help inside the application

## Fork Notes

This repository is intentionally personal in scope. I customize it to fit my own observing and reduction workflow, while preserving clear credit to the upstream project.

That means:

- features may be added here before they exist upstream
- behavior may diverge from the official release
- support expectations should stay modest; this is primarily my own working fork

## Recent Custom Changes

Recent changes in this fork are tracked in [CHANGELOG.md](CHANGELOG.md).

Highlights:

- fixed repeated `timeInfo` values caused by stale timestamp reuse during CSV export
- added optional `signal_err-*` and `snr-*` CSV columns for per-aperture uncertainty export
- added `Photometry Noise` controls in the GUI for detector gain and read noise
- moved the photometry error formula explanation into a cleaner info dialog

## Installation

PyMovie requires Python 3.7+ according to the application code. The dependency stack is fairly pinned, so a clean virtual environment is strongly recommended.

### 1. Clone the repository

```bash
git clone git@github.com:yucelkilic/pymovie.git
cd pymovie
```

### 2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
py -3 -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## Running PyMovie

After installation:

```bash
python -m pymovie.main
```

## Typical Workflow

1. Open the observation file or working folder.
2. Select aperture size and mask settings.
3. Add the target and reference apertures.
4. Run analysis across the desired frame range.
5. Export the measurements with `Write CSV`.
6. If needed, enable `signal_err/snr` export from the `Photometry Noise` section before writing the CSV.

## Photometry Error Export

This fork adds optional uncertainty output for CSV exports.

When enabled in `Median/Misc -> Photometry Noise`, PyMovie can append:

- `signal_err-<aperture>`
- `snr-<aperture>`

The calculation combines:

- local background scatter
- source shot noise
- detector read noise

The detailed formula is available from the small info button next to the `write signal_err/snr columns` option inside the GUI.

## Documentation

The application already ships with two bundled PDF documents:

- `src/pymovie/PyMovie-info.pdf`
- `src/pymovie/PyMovie-doc.pdf`

Inside the GUI:

- `Version Info` opens the version-history PDF
- `Documentation` opens the main documentation PDF

Note: those PDFs come from the upstream project history. Fork-specific changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## Upstream Sync

This repository is set up in standard fork form:

- `origin` -> this personal fork
- `upstream` -> the original `bob-anderson-ok/pymovie` repository

So normal `git push` operations go to this fork, while upstream stays available for comparison or future merges.

## License

This repository keeps the upstream MIT license. See [LICENSE](LICENSE).
