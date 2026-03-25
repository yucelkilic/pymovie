# Changelog

This changelog tracks **fork-specific** changes in this repository.

It is not a replacement for the original PyMovie version history bundled in `src/pymovie/PyMovie-info.pdf`. That PDF reflects the upstream project history; this file records the custom work done in this personal fork.

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
