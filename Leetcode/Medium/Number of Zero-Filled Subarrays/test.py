import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(main.isValid("(]"))
        
    def test_2(self):
        self.assertTrue(main.isValid("()"))
        
    def test_3(self):
        self.assertTrue(main.isValid("()[]{}"))
        
    def test_4(self):
        self.assertTrue(main.isValid("([]{})"))

if __name__ == '__main__':
    unittest.main()