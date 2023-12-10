import unittest
from day9 import day9_part1, day9_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day9(unittest.TestCase):
    data = [
        "0 3 6 9 12 15    \n",
        "1 3 6 10 15 21   \n",
        "10 13 16 21 30 45\n",
    ]

    def test_day9_part1(self):
        result = day9_part1(remove_line_breaks(self.data))
        expected_result = 114
        self.assertEqual(result, expected_result)

    def test_day9_part2(self):
        result = day9_part2(remove_line_breaks(self.data))
        expected_result = 2
        self.assertEqual(result, expected_result)
