#!/usr/bin/env python3
import unittest
from reverse import reverse_integer


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer(self):
        self.assertEqual(reverse_integer(500), 5)  # Output: 5
        self.assertEqual(reverse_integer(-56), -65)   # Output: -65
        self.assertEqual(reverse_integer(-90), -9)  # Output: -9
        self.assertEqual(reverse_integer(91), 19)    # Output: 19


if __name__ == "__main__":
    unittest.main()
