import unittest
from power_of_two import is_power_of_two

class TestIsPowerOfTwo(unittest.TestCase):
    # test positive cases
    def is_power_of_two_true(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertTrue(is_power_of_two(4))
        self.assertTrue(is_power_of_two(8))
        self.assertTrue(is_power_of_two(16))
        
    # test negative cases
    def is_power_of_two_negative(self):
        self.assertTrue(is_power_of_two(3))
        self.assertTrue(is_power_of_two(5))
        self.assertTrue(is_power_of_two(7))
        self.assertTrue(is_power_of_two(-8))
        self.assertTrue(is_power_of_two(-16))
        
if __name__ == "__main__":
    unittest.main()