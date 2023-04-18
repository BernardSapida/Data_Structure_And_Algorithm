import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.longestCommonPrefix(["flower","flow","flight"]), "fl")
        
    def test_2(self):
        self.assertEqual(main.longestCommonPrefix(["dog","racecar","car"]), "")
        
    def test_3(self):
        self.assertEqual(main.longestCommonPrefix(["ab","a"]), "a")

if __name__ == '__main__':
    unittest.main()