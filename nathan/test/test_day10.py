import unittest
from day10 import day10_part1, day10_part2
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

    def test_day10_part2(self):
        data = [
            ".F----7F7F7F7F-7....\n",
            ".|F--7||||||||FJ....\n",
            ".||.FJ||||||||L7....\n",
            "FJL7L7LJLJ||LJ.L-7..\n",
            "L--J.L7...LJS7F-7L7.\n",
            "....F-J..F7FJ|L7L7L7\n",
            "....L7.F7||L7|.L7L7|\n",
            ".....|FJLJ|FJ|F7|.LJ\n",
            "....FJL-7.||.||||...\n",
            "....L---J.LJ.LJLJ...\n",
        ]
        data2 = [
            "FF7FSF7F7F7F7F7F---7\n",
            "L|LJ||||||||||||F--J\n",
            "FL-7LJLJ||||||LJL-77\n",
            "F--JF--7||LJLJ7F7FJ-\n",
            "L---JF-JLJ.||-FJLJJ7\n",
            "|F|F-JF---7F7-L7L|7|\n",
            "|FFJF7L7F-JF7|JL---7\n",
            "7-L-JL7||F7|L7F-7F7|\n",
            "L.L7LFJ|||||FJL7||LJ\n",
            "L7JLJL-JLJLJL--JLJ.L\n",
        ]
        result = day10_part2(remove_line_breaks(data))
        result2 = day10_part2(remove_line_breaks(data2))
        expected_result = 8
        expected_result2 = 10
        self.assertEqual(result, expected_result)
        self.assertEqual(result2, expected_result2)
