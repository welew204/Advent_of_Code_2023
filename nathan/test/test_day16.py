import unittest
from day16 import day16_part1
from helpers.get_file_contents import remove_line_breaks


class Test_Day16(unittest.TestCase):
    data = [
        ".|...\....\n",
        "|.-.\.....\n",
        ".....|-...\n",
        "........|.\n",
        "..........\n",
        ".........\\n",
        "..../.\\\\..\n",
        ".-.-/..|..\n",
        ".|....-|.\\n",
        "..//.|....\n",
    ]

    def test_day16_part1(self):
        result = day16_part1(remove_line_breaks(self.data))
        expected_result = 46
        self.assertEqual(result, expected_result)
