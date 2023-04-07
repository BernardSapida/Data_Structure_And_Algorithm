import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add_num(3, 4), 7)

    # This test is designed to fail for demonstration purposes.
    def test_subtract(self):
        self.assertEqual(main.sub_num(4, 10), -6)

if __name__ == '__main__':
    unittest.main()