import unittest
from day15 import day15_part1, day15_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day15(unittest.TestCase):
    data = [
        "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n",
    ]

    def test_day15_part1(self):
        result = day15_part1(remove_line_breaks(self.data))
        expected_result = 1320
        self.assertEqual(result, expected_result)

    def test_day15_part2(self):
        result = day15_part2(remove_line_breaks(self.data))
        expected_result = 145
        self.assertEqual(result, expected_result)
