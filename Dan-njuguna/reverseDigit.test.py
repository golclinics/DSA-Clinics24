import unittest
from reverseDigit import reverseDigit

class TestReverseDigit(unittest.TestCase):
    def test_single_digit(self):
        # Single digit numbers should remain the same
        self.assertEqual(reverseDigit(5), 5)
        self.assertEqual(reverseDigit(-5), -5)
        # Special case for zero
        self.assertEqual(reverseDigit(0), 0)

    def test_multiple_digits_positive(self):
        # Test reversing multiple-digit positive numbers
        self.assertEqual(reverseDigit(123), 321)
        # Leading zeros should be removed
        self.assertEqual(reverseDigit(90), 9)
        # Leading zeros removed after reversing
        self.assertEqual(reverseDigit(100), 1)

    def test_multiple_digits_negative(self):
        # Test reversing multiple-digit negative numbers
        self.assertEqual(reverseDigit(-123), -321)
        # Handling trailing zeros after reversing
        self.assertEqual(reverseDigit(-90), -9)
        # Negative numbers with trailing zeros
        self.assertEqual(reverseDigit(-100), -1)

    def test_large_numbers(self):
        # Test large numbers
        self.assertEqual(reverseDigit(987654321), 123456789)
        self.assertEqual(reverseDigit(-987654321), -123456789)

    def test_edge_cases(self):
        # Test zero as edge case
        self.assertEqual(reverseDigit(0), 0)

if __name__ == '__main__':
    unittest.main()