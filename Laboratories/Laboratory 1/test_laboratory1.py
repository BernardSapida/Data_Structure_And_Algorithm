import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 3, 4, 5, 6, 7], 3, 5), 0) # 0
        
    def test_2(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 4, 5, 6, 7], 3, 5), 1) # 1
        
    def test_3(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 3, 4, 6, 7], 3, 5), 1) # 1
        
    def test_4(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 4, 6, 7], 3, 5), 2) # 2
        
    def test_5(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 4, 6, 7], -1, 0), 2) # 2
        
    def test_6(self):
        self.assertEqual(main.get_number_of_missing([1, 2, 4, 6, 7], 20, 28), 9) # 9
        
    def test_7(self):
        self.assertEqual(main.get_number_of_missing([15, 21, 4, 8, 9, 7, 11, 30, 1, 17], -1, 3), 4) # 5

if __name__ == '__main__':
    unittest.main()