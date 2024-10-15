import unittest
from reverse_int import reverse

class TestReverse(unittest.TestCase):

    def test_positive_numbers(self):
        """Test reversing positive integers"""
        self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse(500), 5) 
        self.assertEqual(reverse(91), 19)

    def test_negative_numbers(self):
        """Test reversing negative integers"""
        self.assertEqual(reverse(-56), -65)
        self.assertEqual(reverse(-90), -9) 
        self.assertEqual(reverse(-123), -321)

    def test_single_digit(self):
        """Test reversing single-digit integers"""
        self.assertEqual(reverse(9), 9)
        self.assertEqual(reverse(-7), -7)

    def test_zero(self):
        """Test reversing zero"""
        self.assertEqual(reverse(0), 0)

    def test_large_numbers(self):
        """Test reversing large numbers"""
        self.assertEqual(reverse(987654321), 123456789)
        self.assertEqual(reverse(-987654321), -123456789)

# To run the tests
if __name__ == '__main__':
    unittest.main()