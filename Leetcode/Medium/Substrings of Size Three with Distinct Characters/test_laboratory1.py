import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.countGoodSubstrings("xyzzaz"), 1)
        
    def test_2(self):
        self.assertEqual(main.countGoodSubstrings("aababcabc"), 4)
        
    def test_3(self):
        self.assertEqual(main.countGoodSubstrings("abcdefg"), 5)
        
if __name__ == '__main__':
    unittest.main()