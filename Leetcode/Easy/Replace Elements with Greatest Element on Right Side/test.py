import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])
        
    def test_2(self):
        self.assertEqual(main.getConcatenation([1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()