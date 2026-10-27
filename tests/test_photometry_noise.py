"""Numerical limiting cases; not an empirical validation of the noise model."""

import math
from types import SimpleNamespace
import unittest

from pymovie.main import PyMovie


class PhotometryNoiseTests(unittest.TestCase):
    def calculate(self, signal, background, aperture=1, samples=100, gain=1, read_noise=0):
        state = SimpleNamespace(getPhotometryNoiseSettings=lambda: (gain, read_noise))
        return PyMovie.calcSignalErrorAndSnr(state, signal, background, aperture, samples)

    def test_poisson_only_limit(self):
        error, snr = self.calculate(100, 0)
        self.assertEqual(error, 10)
        self.assertEqual(snr, 10)

    def test_gain_converts_shot_noise_to_adu(self):
        error, snr = self.calculate(200, 0, gain=2)
        self.assertEqual(error, 10)
        self.assertEqual(snr, 20)

    def test_background_estimation_uncertainty(self):
        error, snr = self.calculate(0, 2, aperture=4, samples=16)
        # Four aperture pixels contribute 16 ADU^2; estimating the mean
        # from 16 background pixels contributes a further 4 ADU^2.
        self.assertAlmostEqual(error, math.sqrt(20))
        self.assertEqual(snr, 0)

    def test_negative_signal_has_no_negative_shot_variance(self):
        error, snr = self.calculate(-10, 0, read_noise=2)
        self.assertEqual(error, 2)
        self.assertEqual(snr, -5)

    def test_missing_measurement_or_empty_mask_returns_nan(self):
        for signal, aperture in ((None, 1), (100, 0)):
            with self.subTest(signal=signal, aperture=aperture):
                error, snr = self.calculate(signal, 1, aperture=aperture)
                self.assertTrue(math.isnan(error))
                self.assertTrue(math.isnan(snr))

    def test_zero_noise_has_undefined_snr(self):
        error, snr = self.calculate(0, 0)
        self.assertEqual(error, 0)
        self.assertTrue(math.isnan(snr))


if __name__ == '__main__':
    unittest.main()
