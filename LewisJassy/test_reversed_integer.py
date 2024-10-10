import unittest
from Reverse_Integer import reverse_integer


class TestReverseInteger(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(reverse_integer(123), 321)  # add assertion here

    def test_negative_integer(self):
        self.assertEqual(reverse_integer(-456), -654)

    def test_single_digit(self):
        self.assertEqual(reverse_integer(8), 8)

    def test_zero(self):
        self.assertEqual(reverse_integer(0), 0)

    def test_large_number(self):
        self.assertEqual(reverse_integer(987654321), 123456789)

    def test_negative_large_number(self):
        self.assertEqual(reverse_integer(-10000), -1)


if __name__ == '__main__':
    unittest.main()
