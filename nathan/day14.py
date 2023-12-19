from helpers.get_file_contents import get_file_contents, remove_line_breaks
from itertools import count
import json


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


cache = {}


def day14_part2(input_platform):
    platform = [[char for char in row] for row in input_platform]
    for c in range(1000000):
        for col_idx in range(len(platform[0])):
            curr_barrier = -1
            curr_rock_count = 0
            for row_idx in range(len(platform)):
                curr_char = platform[row_idx][col_idx]

                if curr_char == "O":
                    curr_rock_count += 1
                if curr_char == "#" or (row_idx == (len(platform) - 1)):
                    for i in range(
                        curr_barrier + 1, curr_barrier + 1 + curr_rock_count
                    ):
                        platform[i][col_idx] = "O"
                    for j in range(
                        curr_barrier + 1 + curr_rock_count,
                        row_idx if curr_char == "#" else row_idx + 1,
                    ):
                        char_to_set = "."
                        platform[j][col_idx] = char_to_set
                    curr_barrier = row_idx
                    curr_rock_count = 0

        string_platform = json.dumps(platform)
        if string_platform not in cache:
            list_of_tuples = list(zip(*platform))[::-1]
            next_platform = [list(elem) for elem in list_of_tuples]
            cache[string_platform] = json.dumps(next_platform)
        next_platform = json.loads(cache[string_platform])

        # if (c + 1) % 4 == 0:
        # print("after", ["".join(row) for row in platform])

    return day14_part1(["".join(row) for row in platform])


def start():
    pass
    # result = get_file_contents("inputs/day14.txt", day14_part1, remove_line_breaks)
    # print("(Part 1) result: ", result)


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


with open("inputs/day14.txt") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
blocked = {loc for loc, val in board.items() if val == "#"}
rounds = {loc for loc, val in board.items() if val == "O"}


def tilt(rounds, d=1):
    while True:
        free = board.keys() - rounds - blocked
        newrounds = {z - d if z - d in free else z for z in rounds}
        if newrounds == rounds:
            return newrounds
        rounds = newrounds


def load(rounds):
    return sum(100 - z.real for z in rounds)


def cycle(rounds):
    for d in (1, 1j, -1, -1j):
        rounds = tilt(rounds, d)
    return rounds


# Part 1
print(load(tilt(rounds)))


# Part 2
seen = []
for i in count():
    rounds = cycle(rounds)
    if rounds in seen:
        start = seen.index(rounds)
        break
    seen.append(rounds)


print(load(seen[(1000000000 - i) % (start - i) + i - 1]))
