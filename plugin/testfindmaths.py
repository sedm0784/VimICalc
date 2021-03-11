import unittest

from vimicalc import find_maths

class TestFindMaths(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            list(find_maths("2 + 2")),
            ["2 + 2"])

    def test_two(self):
        self.assertEqual(
            list(find_maths("The 2nd: 8 * 8")),
            ["2", "8 * 8"])

