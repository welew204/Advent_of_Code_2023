from helpers.get_file_contents import get_file_contents

dirs = [[1, 0], [-1, 0], [1, 1], [-1, -1], [0, 1], [0, -1], [-1, 1], [1, -1]]

"""
    - - -
   - x -
   - - -
"""


def is_adjacent_to_symbol(char_idx, line_idx, file_contents):
    for d in dirs:
        next_x = char_idx + d[0]
        next_y = line_idx + d[1]
        if (0 <= next_x < len(file_contents[0])) and (0 <= next_y < len(file_contents)):
            char_to_check = file_contents[next_x][next_y]
            if not char_to_check.isalnum() and char_to_check != '.':
                return True
    return False


def day3(file_contents):
    running_sum = 0
    for line_idx, line in file_contents:
        for char_idx, char in line:
            curr_number = ''
            is_part_number = False
            if char.is_digit():
                curr_number += char

                is_part_number = is_part_number or is_adjacent_to_symbol(char_idx, line_idx, file_contents)
                
                if char_idx + 1 >= len(line) or not line[char_idx + 1].is_digit():
                    if is_part_number:
                        running_sum += int(curr_number)
                    curr_number = ''
                    is_part_number = False
    return running_sum



def start():
    get_file_contents("inputs/day1.txt", day3)


start()