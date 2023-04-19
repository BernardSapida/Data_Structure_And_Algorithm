import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.findMedianSortedArrays([4,5,6], [4,5,6]), 5)
        
    def test_2(self):
        self.assertEqual(main.findMedianSortedArrays([1,3], [2]), 2)
        
    def test_3(self):
        self.assertEqual(main.findMedianSortedArrays([1,2], [3,4]), 2.5)

if __name__ == '__main__':
    unittest.main()