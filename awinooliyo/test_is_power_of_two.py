import unittest
from power_of_two import is_power_of_two


class TestIsPowerOfTwo(unittest.TestCase):
    def test_power_of_two(self):
        # Test cases where the result should be True
        self.assertTrue(is_power_of_two(1), "1 should be a power of two")
        self.assertTrue(is_power_of_two(2), "2 should be a power of two")
        self.assertTrue(is_power_of_two(16), "16 should be a power of two")
        self.assertTrue(is_power_of_two(64), "64 should be a power of two")
        self.assertTrue(is_power_of_two(1024), "1024 should be a power of two")

    def test_not_power_of_two(self):
        # Test cases where the result should be False
        self.assertFalse(is_power_of_two(0), "0 is not a power of two")
        self.assertFalse(is_power_of_two(-32),
                         "Negative numbers are not powers of two")
        self.assertFalse(is_power_of_two(3), "3 is not a power of two")
        self.assertFalse(is_power_of_two(18), "18 is not a power of two")
        self.assertFalse(is_power_of_two(100), "100 is not a power of two")

    def test_edge_cases(self):
        # Edge cases
        self.assertTrue(is_power_of_two(1),
                        "1 should be considered a power of two (2^0)")
        self.assertFalse(is_power_of_two(-1), "-1 is not a power of two")


if __name__ == '__main__':
    unittest.main()
