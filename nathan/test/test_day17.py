import unittest
from day17 import day17_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day17(unittest.TestCase):
    data = [
        "2413432311323\n",
        "3215453535623\n",
        "3255245654254\n",
        "3446585845452\n",
        "4546657867536\n",
        "1438598798454\n",
        "4457876987766\n",
        "3637877979653\n",
        "4654967986887\n",
        "4564679986453\n",
        "1224686865563\n",
        "2546548887735\n",
        "4322674655533\n",
    ]

    def test_day17_part1(self):
        result = day17_part1(remove_line_breaks(self.data))
        expected_result = 102
        self.assertEqual(result, expected_result)
