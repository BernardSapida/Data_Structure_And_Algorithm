import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.get_pairs(1), ['()'])
        
    def test_2(self):
        self.assertEqual(main.get_pairs(2), ['(())', '()()'])
        
    def test_3(self):
        self.assertEqual(main.get_pairs(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])

if __name__ == '__main__':
    unittest.main()