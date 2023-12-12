import unittest
from day12 import day12_part1, day12_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day12(unittest.TestCase):
    data = [
        "???.### 1,1,3\n",
        ".??..??...?##. 1,1,3\n",
        "?#?#?#?#?#?#?#? 1,3,1,6\n",
        "????.#...#... 4,1,1\n",
        "????.######..#####. 1,6,5\n",
        "?###???????? 3,2,1\n",
    ]

    def test_day12_part1(self):
        result = day12_part1(remove_line_breaks(self.data))
        expected_result = 21
        self.assertEqual(result, expected_result)

    def test_day12_part2(self):
        result = day12_part2(remove_line_breaks(self.data))
        expected_result = 525152
        self.assertEqual(result, expected_result)
