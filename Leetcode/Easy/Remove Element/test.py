import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.removeElement([3,2,2,3], 3), 2)
        
    def test_2(self):
        self.assertEqual(main.removeElement([0,1,2,2,3,0,4,2], 2), 5)
        
    def test_3(self):
        self.assertEqual(main.removeElement([3,3], 2), 2)

if __name__ == '__main__':
    unittest.main()