#!/usr/bin/env python3
import unittest

from tektronix import coord


class TestTektronix(unittest.TestCase):
    def test_coord_invalid(self):
        with self.assertRaises(ValueError):
            c = coord(-10, 0)


if __name__ == "__main__":
    unittest.main()
