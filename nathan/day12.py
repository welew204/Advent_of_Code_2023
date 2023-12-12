from helpers.get_file_contents import get_file_contents, remove_line_breaks
import itertools
from functools import cache


def get_is_segment_valid(segment):
    for char in segment:
        if char not in set(["?", "#"]):
            return False
    return True


def dfs(springs_list, group_sizes_list, curr_group_size_idx, count=0):
    if curr_group_size_idx >= len(group_sizes_list):
        return True, count
    if not springs_list or springs_list == ["."]:
        return False, count

    curr_group_count = group_sizes_list[curr_group_size_idx]
    for j in range(len(springs_list)):
        is_segment_valid = get_is_segment_valid(springs_list[j:curr_group_count])
        if (
            is_segment_valid
            and (
                j + curr_group_count >= (len(springs_list) - 1)
                or springs_list[j + curr_group_count] == "."
                or springs_list[j + curr_group_count] == "?"
            )
            and (j == 0 or springs_list[j - 1] == ".")
        ):
            is_valid, _ = dfs(
                ["."] + springs_list[(j + curr_group_count + 1) :],
                group_sizes_list,
                curr_group_size_idx + 1,
                count + 1,
            )
            if is_valid:
                count += 1
        elif j == (len(springs_list) - 1):
            return False, count
    return True, count


@cache
def calculate_arrangements(pattern: str, counts: tuple[int]) -> int:
    # base case
    if not pattern:
        return len(counts) == 0

    if not counts:
        return "#" not in pattern

    result = 0

    if pattern[0] in ".?":
        result += calculate_arrangements(pattern[1:], counts)

    if (
        pattern[0] in "#?"
        and counts[0] <= len(pattern)
        and "." not in pattern[: counts[0]]
        and (counts[0] == len(pattern) or pattern[counts[0]] != "#")
    ):
        result += calculate_arrangements(pattern[counts[0] + 1 :], counts[1:])

    return result


def day12_part1(rows):
    arrangements_count = 0
    for row in rows:
        springs_list_str, group_sizes_str = row.split(" ")
        group_sizes_list = tuple(int(x) for x in group_sizes_str.split(","))

        arrangements_count += calculate_arrangements(springs_list_str, group_sizes_list)

    return arrangements_count


def day12_part2(rows):
    arrangements_count = 0
    for row in rows:
        print(row)
        springs_list_str, group_sizes_str = row.split(" ")

        res1 = []
        res2 = []
        for i in range(5):
            res1.append(springs_list_str)
            res2.append(group_sizes_str)
        group_sizes_list = tuple(int(x) for x in ",".join(res2).split(","))
        pattern = "?".join(res1)
        arrangements_count += calculate_arrangements(pattern, group_sizes_list)

    return arrangements_count


def start():
    result = get_file_contents("inputs/day12.txt", day12_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    result = get_file_contents("inputs/day12.txt", day12_part2, remove_line_breaks)
    print("(Part 1) result: ", result)


start()

# data = [
#     "???.### 1,1,3\n",
#     ".??..??...?##. 1,1,3\n",
#     "?#?#?#?#?#?#?#? 1,3,1,6\n",
#     "????.#...#... 4,1,1\n",
#     "????.######..#####. 1,6,5\n",
#     "?###???????? 3,2,1\n",
# ]
# print(day12_part1(remove_line_breaks(data)))
