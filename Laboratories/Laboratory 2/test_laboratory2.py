import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.add(3, 4), 7)
        
    def test_2(self):
        self.assertEqual(main.sub(3, 10), 7)

if __name__ == '__main__':
    unittest.main()