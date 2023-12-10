import unittest
from day10 import day10_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day10(unittest.TestCase):
    data = [
        ".....\n",
        ".S-7.\n",
        ".|.|.\n",
        ".L-J.\n",
        ".....\n",
    ]

    data2 = [
        "..F7.\n",
        ".FJ|.\n",
        "SJ.L7\n",
        "|F--J\n",
        "LJ...\n",
    ]

    def test_day10_part1(self):
        result = day10_part1(remove_line_breaks(self.data))
        result2 = day10_part1(remove_line_breaks(self.data2))
        expected_result = 4
        expected_result2 = 8
        self.assertEqual(result, expected_result)
        self.assertEqual(result2, expected_result2)

    # def test_day9_part2(self):
    #     result = day9_part2(remove_line_breaks(self.data))
    #     expected_result = 2
    #     self.assertEqual(result, expected_result)
