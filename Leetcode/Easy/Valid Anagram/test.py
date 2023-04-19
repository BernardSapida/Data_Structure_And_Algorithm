import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(main.isAnagram("anagram", "nagaram"))
        
    def test_2(self):
        self.assertFalse(main.isAnagram("rat", "car"))

if __name__ == '__main__':
    unittest.main()