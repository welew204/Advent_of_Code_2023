from helpers.get_file_contents import get_file_contents, remove_line_breaks
import math
import itertools


def get_elements(file_contents):
    elements = {}

    for i in range(2, len(file_contents)):
        curr_line = file_contents[i]
        key = curr_line.split(" ")[0]
        left_el_raw, right_el_raw = curr_line.split("(")[1].split(" ")
        left_el = left_el_raw[:-1]
        right_el = right_el_raw[:-1]
        elements[key] = (left_el, right_el)
    return elements


def day8_part1(file_contents):
    instructions = file_contents[0].split(" ")[0]
    elements = get_elements(file_contents)

    steps = 0
    curr_element = "AAA"
    curr_instructions_idx = 0
    while curr_element != "ZZZ":
        curr_instruction = instructions[curr_instructions_idx]
        el_choice = 0 if curr_instruction == "L" else 1
        curr_element = elements[curr_element][el_choice]
        curr_instructions_idx = (curr_instructions_idx + 1) % len(instructions)
        steps += 1

    return steps


def day8_part2(file_contents):
    # taken from https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kckv5xg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # I learned stuff!
    routes = {line[:3]: (line[7:10], line[12:15]) for line in file_contents[2:]}

    def length(node, is_end=lambda node: node.endswith("Z")):
        for index, move in enumerate(itertools.cycle(file_contents[0])):
            if is_end(node):
                return index
            node = routes[node][dict(L=0, R=1)[move]]

    return math.lcm(*(length(node) for node in routes if node.endswith("A")))


def start():
    # pass
    result = get_file_contents("inputs/day8.txt", day8_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day8.txt", day8_part2, remove_line_breaks)
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
