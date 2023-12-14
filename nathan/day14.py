from helpers.get_file_contents import get_file_contents, remove_line_breaks
import itertools
from functools import cache


def day14_part1(platform):
    load = 0
    for col_idx in range(len(platform[0])):
        curr_barrier = -1
        curr_rock_count = 0
        for row_idx in range(len(platform)):
            curr_char = platform[row_idx][col_idx]

            if curr_char == "O":
                curr_rock_count += 1
            if curr_char == "#" or (row_idx == (len(platform) - 1)):
                for i in range(curr_barrier + 1, curr_barrier + 1 + curr_rock_count):
                    load += len(platform) - i
                curr_barrier = row_idx
                curr_rock_count = 0

    return load


def start():
    # pass
    result = get_file_contents("inputs/day14.txt", day14_part1, remove_line_breaks)
    print("(Part 1) result: ", result)


start()
# data = [
#     "#.##..##.\n",
#     "..#.##.#.\n",
#     "##......#\n",
#     "##......#\n",
#     "..#.##.#.\n",
#     "..##..##.\n",
#     "#.#.##.#.\n",
#     "         \n",
#     "#...##..#\n",
#     "#....#..#\n",
#     "..##..###\n",
#     "#####.##.\n",
#     "#####.##.\n",
#     "..##..###\n",
#     "#....#..#\n",
# ]
# print(day13_part1(remove_line_breaks(data)))
