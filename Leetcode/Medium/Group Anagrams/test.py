import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(main.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        
    def test_2(self):
        self.assertListEqual(main.groupAnagrams([""]), [[""]])
        
    def test_3(self):
        self.assertListEqual(main.groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()