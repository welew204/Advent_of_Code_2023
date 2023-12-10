from helpers.get_file_contents import get_file_contents, remove_line_breaks


def get_next(num_list):
    if len(set(num_list)) <= 1:
        return num_list[0]
    last_diff = get_next([j - i for i, j in zip(num_list[:-1], num_list[1:])])
    return num_list[-1] + last_diff


def get_prev(num_list):
    if len(set(num_list)) <= 1:
        return num_list[0]
    last_diff = get_prev([j - i for i, j in zip(num_list[:-1], num_list[1:])])
    return num_list[0] - last_diff


def get_histories(file_contents):
    histories = []
    for line in file_contents:
        nums = line.split(" ")
        histories.append([int(num) for num in nums if num != ""])
    return histories


def day9_part1(file_contents):
    histories = get_histories(file_contents)

    total = 0
    for history in histories:
        total += get_next(history)
    return total


def day9_part2(file_contents):
    histories = get_histories(file_contents)

    total = 0
    for history in histories:
        total += get_prev(history)
    return total


def start():
    result = get_file_contents("inputs/day9.txt", day9_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day9.txt", day9_part2, remove_line_breaks)
    print("(Part 2) result: ", part2_result)


start()
# data = [
#     "32T3K 765\n",
#     "T55J5 684\n",
#     "KK677 28\n",
#     "KTJJT 220\n",
#     "QQQJA 483\n",
# ]
# day7_part2(remove_line_breaks(data))
# print(day6_part2(data))
