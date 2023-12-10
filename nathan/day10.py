from helpers.get_file_contents import get_file_contents, remove_line_breaks
from collections import deque

# this queue is synchronized, which is pretty pointless...
from queue import Queue

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                return row, col
    raise Exception("No starting position")


def day10_part1(grid):
    start_row, start_col = find_start(grid)
    max_dist = 0

    visited = set()

    def is_valid(curr, next_pos):
        if next_pos in visited:
            return False
        next_row, next_col = next_pos
        if next_row < 0 or next_row >= len(grid):
            return False
        if next_col < 0 or next_col >= len(grid[0]):
            return False
        next_char = grid[next_row][next_col]
        if next_char == "." or next_char == "S":
            return False

        curr_row, curr_col = curr
        if next_char == "|":
            return abs(curr_row - next_row) == 1
        if next_char == "-":
            return abs(curr_col - next_col) == 1
        if next_char == "L":
            return next_row - 1 == curr_row or next_col + 1 == curr_col
        if next_char == "J":
            return next_row - 1 == curr_row or next_col - 1 == curr_col
        if next_char == "7":
            return next_row + 1 == curr_row or next_col - 1 == curr_col
        if next_char == "F":
            return next_row + 1 == curr_row or next_col + 1 == curr_col

        return False

    q = deque([(start_row, start_col)])
    curr_len = -1
    while q:
        curr_len += 1
        max_dist = max(max_dist, curr_len)
        nodes = []
        while q:
            nodes.append(q.popleft())

        for node in nodes:
            curr_row, curr_col = node
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                next_pos = (next_row, next_col)
                if is_valid(node, next_pos):
                    visited.add(node)
                    visited.add(next_pos)
                    q.append((next_pos))

    return max_dist


def is_enclosed(curr_row, curr_col, grid, visited):
    if curr_row == 1:
        print("hi")
    for d in dirs:
        next_row = curr_row + d[0]
        next_col = curr_col + d[1]

        if next_row < 0 or next_row >= len(grid):
            return False
        if next_col < 0 or next_col >= len(grid[0]):
            return False
        next_char = grid[next_row][next_col]
        if next_char == "O":
            return False
        if next_char == "I":
            return True
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        if next_char == "|" and abs(curr_row - next_row) == 1:
            return is_enclosed(next_row, next_col, grid, visited)
        if next_char == "-" and abs(curr_col - next_col) == 1:
            return is_enclosed(next_row, next_col, grid, visited)
        if next_char == "L" and (next_row - 1 == curr_row or next_col + 1 == curr_col):
            return is_enclosed(next_row, next_col, grid, visited)
        if next_char == "J" and (next_row - 1 == curr_row or next_col - 1 == curr_col):
            return is_enclosed(next_row, next_col, grid, visited)
        if next_char == "7" and (next_row + 1 == curr_row or next_col - 1 == curr_col):
            return is_enclosed(next_row, next_col, grid, visited)
        if next_char == "F" and (next_row + 1 == curr_row or next_col + 1 == curr_col):
            return is_enclosed(next_row, next_col, grid, visited)

        if next_char == ".":
            res = is_enclosed(next_row, next_col, grid, visited)
            grid[next_row][next_col] = "I" if res else "O"
            return res

    return True


def day10_part2(grid):
    m = [l.strip() for l in grid]
    n = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }

    x, y = None, None

    for yi, line in enumerate(m):
        for xi, c in enumerate(line):
            if c == "S":
                x, y = xi, yi
                break

    assert x != None
    assert y != None

    q = Queue()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = m[y + dy][x + dx]
        if c in n:
            for dx2, dy2 in n[c]:
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

    dists = {(x, y): 0}
    assert q.qsize() == 2

    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        # print(d,(x,y))
        dists[(x, y)] = d

        for dx, dy in n[m[y][x]]:
            q.put((d + 1, (x + dx, y + dy)))

    print(f"Part 1: {max(dists.values())}")

    w = len(m[0])
    h = len(m)

    inside_count = 0
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if (x, y) in dists:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < w and y2 < h:
                c2 = m[y2][x2]
                if (x2, y2) in dists and c2 != "L" and c2 != "7":
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside_count += 1
    print(f"Part 2: {inside_count}")


def start():
    pass
    result = get_file_contents("inputs/day10.txt", day10_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents(
        "inputs/day10.txt", day10_part2, remove_line_breaks
    )


start()
# data = [
#     "32T3K 765\n",
#     "T55J5 684\n",
#     "KK677 28\n",
#     "KTJJT 220\n",
#     "QQQJA 483\n",
# ]
# print(
#     day10_part2(
#         remove_line_breaks(
#             [
#                 "...........\n",
#                 ".S-------7.\n",
#                 ".|F-----7|.\n",
#                 ".||.....||.\n",
#                 ".||.....||.\n",
#                 ".|L-7.F-J|.\n",
#                 ".|..|.|..|.\n",
#                 ".L--J.L--J.\n",
#                 "...........\n",
#             ]
#         )
#     )
# )
# # print(day6_part2(data))
