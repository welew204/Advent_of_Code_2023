from helpers.get_file_contents import get_file_contents, remove_line_breaks
import itertools


def day11_part1(file_contents, empty_factor=2):
    grid = [[*line] for line in file_contents]
    cols = list(zip(*grid))
    empty_row_idx_list = []
    empty_col_idx_list = []

    for row_idx in range(len(grid)):
        if len(set(grid[row_idx])) == 1 and grid[row_idx][0] == ".":
            empty_row_idx_list.append(row_idx)
    for col_idx in range(len(cols)):
        if len(set(cols[col_idx])) == 1 and cols[col_idx][0] == ".":
            empty_col_idx_list.append(col_idx)
    galaxies = []
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == "#":
                galaxies.append((row_idx, col_idx))
    combinations = list(itertools.combinations(galaxies, 2))
    diffs_sum = 0
    for c in combinations:
        cols_between = 0
        rows_between = 0
        for empty_col in empty_col_idx_list:
            if (c[0][1] < empty_col < c[1][1]) or (c[1][1] < empty_col < c[0][1]):
                cols_between += 1
        for empty_row in empty_row_idx_list:
            if (c[0][0] < empty_row < c[1][0]) or (c[1][0] < empty_row < c[0][0]):
                rows_between += 1
        initial_diff = abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1])
        diff_with_expansion = (
            (empty_factor * cols_between)
            + (empty_factor * rows_between)
            - (cols_between + rows_between)
        ) + initial_diff
        diffs_sum += diff_with_expansion
    return diffs_sum


def start():
    # pass
    # result = get_file_contents("inputs/day11.txt", day11_part1, remove_line_breaks)
    # print("(Part 1) result: ", result)
    part2_result = get_file_contents(
        "inputs/day11.txt", day11_part1, remove_line_breaks, 1000000
    )
    print("(Part 2) result: ", part2_result)


start()
