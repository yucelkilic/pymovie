# Changelog

This changelog tracks **fork-specific** changes in this repository.

It is not a replacement for the original PyMovie version history bundled in `src/pymovie/PyMovie-info.pdf`. That PDF reflects the upstream project history; this file records the custom work done in this personal fork.

## 2026-10-27

### Added

- regression tests using generated RV24 and lossless FFV1 AVI files for pixel
  preservation, seeking, truncated input, and reader fallback
- FITS timestamp, field ordering, invalid OCR, and exposure-header tests
- AAV cancellation, decode-failure, and declined-confirmation tests
- numerical limiting-case tests for photometry uncertainty and SNR
- test dependency file and instructions documenting coverage and limitations

## 2026-10-26

### Fixed

- load OCR digit templates saved with NumPy 2 in the NumPy 1.x environment
- enable OCR-based FITS conversion for AAV files, preserving 16-bit pixels and
  native frame exposure; restrict integrated AAV recordings to full-frame output

## 2026-08-09

### Added

- uncompressed RV24 AVI reader fallback for AVI files that OpenCV cannot open
- `Timestamp -> Convert AVI to FITS` tool for OCR-timestamped AVI exports
- full-frame FITS export to `fits_converted`
- chronological upper/lower field FITS export to `fits_converted_fields` for higher time resolution photometry
- FITS headers with OCR-derived `DATE-OBS`, source frame, field order, exposure metadata, and OCR validation flags
- progress dialog with cancellation while converting AVI files to FITS
- CSV header warning when `signal_err/snr` export still uses placeholder detector noise settings

### Changed

- `python main.py` can run directly from `src/pymovie` by adding the package parent to `sys.path` when needed

## 2026-03-25

### Added

- optional CSV export columns for per-aperture measurement uncertainty: `signal_err-*`
- optional CSV export columns for per-aperture signal-to-noise ratio: `snr-*`
- `Photometry Noise` controls in the `Median/Misc` tab for:
  - enabling uncertainty export
  - detector gain in `e-/ADU`
  - detector read noise in `e-`
- dedicated info button and help dialog for the photometry error model

### Changed

- improved the `Photometry Noise` UI by moving the formula explanation out of the main panel and into a cleaner info dialog

### Fixed

- corrected repeated `timeInfo` values during CSV export by preventing stale timestamp reuse across frames
- reset AVI per-frame timestamp state so failed reads do not repeat the previous frame timestamp
- reset OCR-derived `upperTimestamp` and `lowerTimestamp` values per frame when using AVI/WCS timestamp extraction
- unified current-frame timestamp selection through a shared helper path
- ensured ADV/AAV frame timestamps are captured from the current frame metadata before CSV export
- corrected CSV column alignment when centroid values are missing
