from helpers.get_file_contents import get_file_contents, remove_line_breaks
from collections import defaultdict


direction_map = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}


def day18_part1(file_contents):
    dug, x, y = {(0, 0)}, 0, 0

    directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    for line in file_contents:
        line = line.split()
        for i in range(int(line[1])):
            x, y = x + directions[line[0]][0], y + directions[line[0]][1]
            dug.add((x, y))
    min_x, min_y, max_x, max_y = (
        min({tile[0] for tile in dug}),
        min({tile[1] for tile in dug}),
        max({tile[0] for tile in dug}),
        max({tile[1] for tile in dug}),
    )
    old_tiles, new_tiles = set(), {
        (x, y)
        for y in range(min_y, max_y + 1)
        for x in [min_x, max_x]
        if (x, y) not in dug
    } | {
        (x, y)
        for x in range(min_x, max_x + 1)
        for y in [min_y, max_y]
        if (x, y) not in dug
    }
    while new_tiles:
        new_new_tiles = {
            (tile[0] + direction[0], tile[1] + direction[1])
            for tile in new_tiles
            for direction in directions.values()
            if min_x <= tile[0] + direction[0] <= max_x
            and min_y <= tile[1] + direction[1] <= max_y
            and (tile[0] + direction[0], tile[1] + direction[1]) not in dug
            and (tile[0] + direction[0], tile[1] + direction[1]) not in old_tiles
            and (tile[0] + direction[0], tile[1] + direction[1]) not in new_tiles
        }
        old_tiles, new_tiles = old_tiles | new_tiles, new_new_tiles
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(old_tiles))


def day18_part2(file_contents):
    # https://adventofcode.com/2023/day/18#part2

    h_lines, v_lines, x, y = [], [], 0, 0
    for line in file_contents:
        line = line.split()
        n = int(line[2][2:7], 16)
        match line[2][7]:
            case "0":
                h_lines.append((x, x + n, y))
                x += n
            case "1":
                v_lines.append((y, y + n, x))
                y += n
            case "2":
                h_lines.append((x - n, x, y))
                x -= n
            case "3":
                v_lines.append((y - n, y, x))
                y -= n
    h_bars = sorted({h_line[2] for h_line in h_lines})
    v_bars = sorted({v_line[2] for v_line in v_lines})
    total = 0
    cells = []
    for y in range(len(h_bars) - 1):
        cell_row = []
        h_bar_prev = h_bars[y]
        h_bar = h_bars[y + 1]
        for x in range(len(v_bars) - 1):
            v_bar_left = False
            for v_line in v_lines:
                if (
                    h_bar_prev >= v_line[0]
                    and h_bar <= v_line[1]
                    and v_bars[x] == v_line[2]
                ):
                    v_bar_left = True
                    break
            prev_in = False if (x == 0 or not cell_row[x - 1]) else True
            if prev_in != v_bar_left:
                cell_row.append(True)
                total += (h_bar - h_bar_prev - 1) * (v_bars[x + 1] - v_bars[x] - 1)
                if prev_in:
                    total += h_bar - h_bar_prev - 1
                if y > 0 and cells[y - 1][x]:
                    total += v_bars[x + 1] - v_bars[x] - 1
                if (
                    prev_in
                    and not v_bar_left
                    and y > 0
                    and cells[y - 1][x]
                    and cells[y - 1][x - 1]
                ):
                    total += 1
            else:
                cell_row.append(False)
        cells.append(cell_row)
    print(
        total
        + sum([v_line[1] - v_line[0] + 1 for v_line in v_lines])
        + sum([h_line[1] - h_line[0] + 1 for h_line in h_lines])
        - len(v_lines)
        - len(h_lines)
    )


def start():
    # pass
    # result = get_file_contents("inputs/day18.txt", day18_part1, remove_line_breaks)
    # print("(Part 1) result: ", result)
    result = get_file_contents("inputs/day18.txt", day18_part2, remove_line_breaks)
    print("(Part 2) result: ", result)


start()

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


# print(day18_part1(remove_line_breaks(data)))
