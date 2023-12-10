from helpers.get_file_contents import get_file_contents, remove_line_breaks
from collections import deque

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


# def day9_part2(file_contents):
#     histories = get_histories(file_contents)

#     total = 0
#     for history in histories:
#         total += get_prev(history)
#     return total


def start():
    result = get_file_contents("inputs/day10.txt", day10_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    # part2_result = get_file_contents("inputs/day9.txt", day9_part2, remove_line_breaks)
    # print("(Part 2) result: ", part2_result)


start()
# data = [
#     "32T3K 765\n",
#     "T55J5 684\n",
#     "KK677 28\n",
#     "KTJJT 220\n",
#     "QQQJA 483\n",
# ]
print(
    day10_part1(
        remove_line_breaks(
            [
                ".....\n",
                ".S-7.\n",
                ".|.|.\n",
                ".L-J.\n",
                ".....\n",
            ]
        )
    )
)
# print(day6_part2(data))
