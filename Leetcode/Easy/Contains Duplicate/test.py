import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(main.containsDuplicate([1,2,3,1]))
        
    def test_2(self):
        self.assertFalse(main.containsDuplicate([1,2,3,4]))

if __name__ == '__main__':
    unittest.main()