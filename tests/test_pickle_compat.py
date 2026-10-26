import pickle
from pathlib import Path
import tempfile
import unittest

import numpy as np

from pymovie.pickle_compat import load_numpy_pickle


class NumpyPickleCompatibilityTests(unittest.TestCase):
    def load_payload(self, payload):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "digits.p"
            path.write_bytes(payload)
            result = load_numpy_pickle(path)
            self.assertEqual(path.read_bytes(), payload)
            return result

    def test_existing_arrays_and_missing_digits(self):
        digits = [np.arange(12, dtype=np.uint8).reshape(3, 4), None]
        for protocol in (0, 4, 5):
            with self.subTest(protocol=protocol):
                result = self.load_payload(pickle.dumps(digits, protocol=protocol))
                np.testing.assert_array_equal(result[0], digits[0])
                self.assertEqual(result[0].dtype, digits[0].dtype)
                self.assertIsNone(result[1])

    def test_numpy_2_module_path(self):
        digits = [np.arange(12, dtype=np.uint8).reshape(3, 4), None]
        # Protocol 0 uses newline-delimited names, so the rename does not
        # require adjusting binary string lengths or frame sizes.
        payload = pickle.dumps(digits, protocol=0).replace(
            b"cnumpy.core.multiarray\n", b"cnumpy._core.multiarray\n"
        )
        self.assertIn(b"cnumpy._core.multiarray\n", payload)
        result = self.load_payload(payload)
        np.testing.assert_array_equal(result[0], digits[0])
        self.assertEqual(result[0].dtype, digits[0].dtype)
        self.assertIsNone(result[1])

    def test_unrelated_missing_module_is_not_hidden(self):
        with self.assertRaises(ModuleNotFoundError):
            self.load_payload(b"cmissing_pymovie_test_module\nthing\n.")

    def test_corrupt_pickle_is_not_hidden(self):
        with self.assertRaises(pickle.UnpicklingError):
            self.load_payload(b"not a pickle")


if __name__ == "__main__":
    unittest.main()
