import main    # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.lengthOfLastWord("Hello World"), 5)
        
    def test_2(self):
        self.assertEqual(main.lengthOfLastWord("   fly me   to   the moon  "), 4)
        
    def test_3(self):
        self.assertEqual(main.lengthOfLastWord("luffy is still joyboy"), 6)

if __name__ == '__main__':
    unittest.main()