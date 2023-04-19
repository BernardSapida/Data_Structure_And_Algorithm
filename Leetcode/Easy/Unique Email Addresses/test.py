import main       # The code to test
import unittest   # The test framework

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]), 2)
        
    def test_2(self):
        self.assertEqual(main.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]), 3)
        
    def test_3(self):
        self.assertEqual(main.numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]), 2)

if __name__ == '__main__':
    unittest.main()