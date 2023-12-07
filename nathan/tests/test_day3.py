import unittest
from day3 import day3, day3_pt2


class TestDay3(unittest.TestCase):
    def test_day3(self):
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

    def test_day3_part1(self):
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
        result = day3_pt2(data)
        expected_result = 467835
        self.assertEqual(result, expected_result)