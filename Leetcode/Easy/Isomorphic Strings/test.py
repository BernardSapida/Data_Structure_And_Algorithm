import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(main.isIsomorphic("egg", "add"))
        
    def test_2(self):
        self.assertFalse(main.isIsomorphic("foo", "bar"))
        
    def test_3(self):
        self.assertTrue(main.isIsomorphic("paper", "title"))
        
    def test_4(self):
        self.assertFalse(main.isIsomorphic("badc", "baba"))
        
    def test_5(self):
        self.assertFalse(main.isIsomorphic("egcd", "adfd"))

if __name__ == '__main__':
    unittest.main()