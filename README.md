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
- uncompressed RV24 AVI fallback support for files that OpenCV cannot decode
- OCR-timestamped AVI to FITS conversion for external photometry workflows
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

## Installation

PyMovie requires Python 3.7+ according to the application code. The dependency stack is fairly pinned, so a clean virtual environment is strongly recommended.

### Conda setup (macOS / Apple Silicon)

From the repository root:

```bash
conda env create -f environment.yml
conda activate pymovie
python scripts/build_advcore_macos.py  # Apple Silicon only
python -m pymovie.main
```

This environment uses Python 3.10, NumPy 1.23.1, and Numba 0.56 to
keep the older application dependencies compatible. Qt and the scientific
libraries come from conda-forge; PyMovie is installed in editable mode.
The environment file uses the Prefix.dev conda-forge mirror because the
primary conda-forge host was unreachable during setup.
On Apple Silicon, the build script replaces Adv2's bundled Intel-only library
with an ARM64 build from the official ADVCore source at a pinned revision.
It requires Git and Xcode Command Line Tools (`xcode-select --install`) and
keeps a backup of the original library. Rerun it if Adv2 is reinstalled.
Do not install the legacy `requirements.txt` over this environment: it
includes Windows-only `winshell` and conflicting NumPy/Numba constraints.

### Alternative: virtual environment

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

When default placeholder detector values are still in use, the CSV header includes a `signal_err note` line so downstream analysis can treat those uncertainty values as approximate.

## AVI / AAV To FITS Conversion

This fork adds a conversion tool for AVI/MOV and AAV files with OCR-readable timestamps.

After opening a video and selecting or defining the OCR timestamp profile, use `Timestamp -> Convert AVI/AAV to FITS`. The converter can write either:

- full-frame FITS files to `fits_converted`
- chronological upper/lower field FITS files to `fits_converted_fields`

Field mode is intended for higher time resolution work. It writes each AVI frame as two FITS images in timestamp order, preserving the upper and lower OCR-derived timestamps in `DATE-OBS`. A progress dialog shows conversion status and allows cancellation.

AAV conversion preserves the reader's 16-bit pixel values and uses OCR for
`DATE-OBS`. Full-frame exposure comes from the AAV frame metadata when available,
with the effective frame rate as a fallback. Integrated AAV recordings (or those
with unknown integration) use full-frame output only; splitting them into fields
would not provide independent shorter exposures.

## Tests

Run the regression suite from the repository root in the configured PyMovie
environment:

```bash
conda activate pymovie
python -m pip install -r requirements-test.txt
python -m unittest discover -s tests -v
```

On Apple Silicon, complete the ADVCore build described in the installation
instructions first. The tests import the application module, which loads Adv2.
PyAV is required by the video tests; missing dependencies fail test discovery
rather than silently skipping those checks.

The suite covers:

- OCR pickle compatibility across the NumPy module rename
- RV24 frame pixels, RIFF padding, seeking, truncated input, and reader fallback
- lossless FFV1 video decoding through PyAV, including forward and backward seeking
- FITS pixel values, OCR validity, field order, timestamps, and exposure headers
- AAV conversion completion, cancellation, decode errors, and declined confirmation
- numerical limiting cases for the photometry uncertainty and SNR calculation

Video fixtures and FITS outputs are generated in temporary directories. No
observation files are required. AAV decoding and OCR recognition are simulated
in the conversion tests; these tests do not establish recognition accuracy on
real recordings. The midnight test checks the interval between fields, not
calendar-date rollover across a recording. The noise tests check the implemented
calculation, not the physical calibration of the detector or an empirical
validation of the noise model. The suite does not exercise the interactive GUI.

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
