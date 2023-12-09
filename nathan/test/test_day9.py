import unittest
from day9 import day9_part1, day9_part2
from helpers.get_file_contents import remove_line_breaks


class Test_Day9(unittest.TestCase):
    data = [
        "RL              \n",
        "                \n",
        "AAA = (BBB, CCC)\n",
        "BBB = (DDD, EEE)\n",
        "CCC = (ZZZ, GGG)\n",
        "DDD = (DDD, DDD)\n",
        "EEE = (EEE, EEE)\n",
        "GGG = (GGG, GGG)\n",
        "ZZZ = (ZZZ, ZZZ)\n",
    ]
    data2 = [
        "LLR             \n",
        "                \n",
        "AAA = (BBB, BBB)\n",
        "BBB = (AAA, ZZZ)\n",
        "ZZZ = (ZZZ, ZZZ)\n",
    ]

    def test_day9_part1(self):
        result = day9_part1(remove_line_breaks(self.data))
        expected_result = 2
        expected_result2 = 6
        self.assertEqual(result, expected_result)

    # def test_day9_part2(self):
    #     data = [
    #         "LR              \n",
    #         "                \n",
    #         "11A = (11B, XXX)\n",
    #         "11B = (XXX, 11Z)\n",
    #         "11Z = (11B, XXX)\n",
    #         "22A = (22B, XXX)\n",
    #         "22B = (22C, 22C)\n",
    #         "22C = (22Z, 22Z)\n",
    #         "22Z = (22B, 22B)\n",
    #         "XXX = (XXX, XXX)\n",
    #     ]
    #     result = day8_part2(remove_line_breaks(data))
    #     expected_result = 6
    #     self.assertEqual(result, expected_result)
