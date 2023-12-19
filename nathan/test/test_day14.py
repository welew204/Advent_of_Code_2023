import unittest
from day14 import day14_part1, day14_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day14(unittest.TestCase):
    data = [
        "O....#....\n",
        "O.OO#....#\n",
        ".....##...\n",
        "OO.#O....O\n",
        ".O.....O#.\n",
        "O.#..O.#.#\n",
        "..O..#O..O\n",
        ".......O..\n",
        "#....###..\n",
        "#OO..#....\n",
    ]

    def test_day14_part1(self):
        result = day14_part1(remove_line_breaks(self.data))
        expected_result = 136
        self.assertEqual(result, expected_result)

    def test_day14_part2(self):
        result = day14_part2(remove_line_breaks(self.data))
        expected_result = 64
        self.assertEqual(result, expected_result)
