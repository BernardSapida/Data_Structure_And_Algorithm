import main    # The code to test
import unittest   # The test framework


class Test(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(main.displayLineOfSight([3, 2, 1]), [0, 1, 1])

    def test_2(self):
        self.assertListEqual(main.displayLineOfSight([1, 2, 3]), [0, 1, 2])

    def test_3(self):
        self.assertListEqual(main.displayLineOfSight(
            [5, 1, 2, 1, 3]), [0, 1, 2, 1, 4])

    def test_4(self):
        self.assertListEqual(main.displayLineOfSight(
            [10, 3, 2, 10, 2, 1, 7]), [0, 1, 1, 3, 1, 1, 6])

    def test_4(self):
        self.assertListEqual(main.displayLineOfSight(
            [10, 3, 2, 8, 2, 1, 7]), [0, 1, 1, 3, 1, 1, 3])

    def test_6(self):
        self.assertListEqual(main.displayLineOfSight(
            [192, 163, 185, 165, 165, 170, 180]), [0, 1, 2, 1, 1, 3, 4])
        # self.assertListEqual(main.displayLineOfSight([192, 163, 185, 165, 165, 170, 180]), [0, 1, 2, 1, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()
