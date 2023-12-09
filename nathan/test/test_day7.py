import unittest
from day7 import day7_part1, day7_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day7(unittest.TestCase):
    data = [
        "32T3K 765\n",
        "T55J5 684\n",
        "KK677 28\n",
        "KTJJT 220\n",
        "QQQJA 483\n",
    ]

    def test_day7_part1(self):
        result = day7_part1(remove_line_breaks(self.data))
        expected_result = 6440
        self.assertEqual(result, expected_result)

    def test_day7_part2(self):
        result = day7_part2(remove_line_breaks(self.data))
        expected_result = 5905
        self.assertEqual(result, expected_result)
