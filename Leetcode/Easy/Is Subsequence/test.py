import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(main.isSubsequence("abc", "ahbgdc"))
        
    def test_2(self):
        self.assertFalse(main.isSubsequence("axc", "ahbgdc"))

if __name__ == '__main__':
    unittest.main()