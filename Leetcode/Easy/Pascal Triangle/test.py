import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        
    def test_2(self):
        self.assertEqual(main.generate(1), [1])

if __name__ == '__main__':
    unittest.main()