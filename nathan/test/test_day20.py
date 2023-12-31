import unittest
from day20 import day20_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day20(unittest.TestCase):
    data = [
        "broadcaster -> a, b, c\n",
        "%a -> b\n",
        "%b -> c\n",
        "%c -> inv\n",
        "&inv -> a\n",
    ]

    data2 = [
        "broadcaster -> a\n",
        "%a -> inv, con\n",
        "&inv -> b\n",
        "%b -> con\n",
        "&con -> output\n",
    ]

    def test_day20_part1(self):
        result = day20_part1(remove_line_breaks(self.data))
        result2 = day20_part1(remove_line_breaks(self.data2))
        expected_result = 32000000
        expected_result2 = 11687500
        self.assertEqual(result, expected_result)
        self.assertEqual(result2, expected_result2)
