import unittest
from day6 import day6_part1, day6_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day6(unittest.TestCase):
    data = ["Time:      7  15   30\n", "Distance:  9  40  200\n"]

    def test_day6_part1(self):
        result = day6_part1(remove_line_breaks(self.data))
        expected_result = 288
        self.assertEqual(result, expected_result)

    def test_day6_part2(self):
        result = day6_part2(remove_line_breaks(self.data))
        expected_result = 71503
        self.assertEqual(result, expected_result)
