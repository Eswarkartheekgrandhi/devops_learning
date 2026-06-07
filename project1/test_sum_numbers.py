import unittest
from sum_numbers import add


class TestAdd(unittest.TestCase):

    def test_two_numbers(self):
        self.assertEqual(add(10, 20), 30)

    def test_three_numbers(self):
        self.assertEqual(add(10, 20, 30), 60)

    def test_multiple_numbers(self):
        self.assertEqual(add(1, 2, 3, 4, 5), 15)


if __name__ == "__main__":
    unittest.main()