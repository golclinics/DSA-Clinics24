import unittest
from reverse_integar import Solution

class TestReverseInteger(unittest.TestCase):
    
    def test_positive(self):
        solution = Solution()
        self.assertEqual(solution.reverse(500), 5)
    
    def test_negative(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-123), -321)

    def test_overflow(self):
        solution = Solution()
        self.assertEqual(solution.reverse(1534236469), 0)

if __name__ == "__main__":
    unittest.main()
