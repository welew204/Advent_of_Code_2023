import unittest
from day18 import day18_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day18(unittest.TestCase):
    data = [
        "R 6 (#70c710)\n",
        "D 5 (#0dc571)\n",
        "L 2 (#5713f0)\n",
        "D 2 (#d2c081)\n",
        "R 2 (#59c680)\n",
        "D 2 (#411b91)\n",
        "L 5 (#8ceee2)\n",
        "U 2 (#caa173)\n",
        "L 1 (#1b58a2)\n",
        "U 2 (#caa171)\n",
        "R 2 (#7807d2)\n",
        "U 3 (#a77fa3)\n",
        "L 2 (#015232)\n",
        "U 2 (#7a21e3)\n",
    ]

    def test_day18_part1(self):
        result = day18_part1(remove_line_breaks(self.data))
        expected_result = 62
        self.assertEqual(result, expected_result)
