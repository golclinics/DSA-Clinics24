import unittest
from Power_of_two import is_power_of_two

# test_Power_of_two.py

class TestPowerOfTwo(unittest.TestCase):
    def test_positive_cases(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertTrue(is_power_of_two(4))
        self.assertTrue(is_power_of_two(8))
        self.assertTrue(is_power_of_two(16))

    def test_negative_cases(self):
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(3))
        self.assertFalse(is_power_of_two(5))
        self.assertFalse(is_power_of_two(6))
        self.assertFalse(is_power_of_two(-2))

if __name__ == '__main__':
    unittest.main()