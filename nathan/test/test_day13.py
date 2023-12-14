import unittest
from day13 import day13_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day13(unittest.TestCase):
    data = [
        "#.##..##.\n",
        "..#.##.#.\n",
        "##......#\n",
        "##......#\n",
        "..#.##.#.\n",
        "..##..##.\n",
        "#.#.##.#.\n",
        "         \n",
        "#...##..#\n",
        "#....#..#\n",
        "..##..###\n",
        "#####.##.\n",
        "#####.##.\n",
        "..##..###\n",
        "#....#..#\n",
    ]

    def test_day13_part1(self):
        result = day13_part1(remove_line_breaks(self.data))
        expected_result = 405
        self.assertEqual(result, expected_result)

    # def test_day12_part2(self):
    #     result = day12_part2(remove_line_breaks(self.data))
    #     expected_result = 525152
    #     self.assertEqual(result, expected_result)
