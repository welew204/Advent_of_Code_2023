import unittest
from .day3 import day3


class TestDay3(unittest.TestCase):
    def test_day3_part1(self):
        """
        Test that a method sorts a list in place
        """
        data = [6, 21, 3, 0, -1]
        result = day3()
        self.assertEqual(result, sorted(data))