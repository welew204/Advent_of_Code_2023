import unittest
from .day3 import day3


class TestDay3(unittest.TestCase):
    def test_day3_part1(self):
        """
        Test that a method sorts a list in place
        """
        data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        result = day3(data)
        expected_result = 4361
        self.assertEqual(result, expected_result)