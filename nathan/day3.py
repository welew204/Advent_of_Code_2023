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
            char_to_check = file_contents[next_y][next_x]
            if not char_to_check.isalnum() and char_to_check != '.':
                return True
    return False


def day3(input_file_contents):
    file_contents = [line[:-1] for line in input_file_contents]
    running_sum = 0
    for line_idx, line in enumerate(file_contents):
        is_part_number = False
        curr_number = ''
        for char_idx, char in enumerate(line):
            
            if char.isdigit():
                curr_number += char

                is_part_number = is_part_number or is_adjacent_to_symbol(char_idx, line_idx, file_contents)
                
                if char_idx + 1 >= len(line) or not line[char_idx + 1].isdigit():
                    if is_part_number:
                        running_sum += int(curr_number)
                    curr_number = ''
                    is_part_number = False
    print(running_sum)
    return running_sum


def is_inbound_and_number(x, y, file_contents):
    return (0 <= x < len(file_contents[0])) and (0 <= y < len(file_contents)) and file_contents[y][x].isdigit()


def get_num_from_coords(x, y, file_contents):
    left, right = x, x
    while left > 0:
        if not file_contents[y][left-1].isdigit():
            break
        left -= 1
    while right < len(file_contents[0]) - 1:
        if not file_contents[y][right+1].isdigit():
            break
        right += 1
    
    return int(file_contents[y][left:right+1])


def day3_pt2(input_file_contents):
    file_contents = [line[:-1] for line in input_file_contents]
    running_sum = 0
    for line_idx, line in enumerate(file_contents):
        
        for char_idx, char in enumerate(line):
            adj_numbers = []
            if char == '*':
                adj_numbers.extend([[char_idx + x, line_idx + y] for x, y in [[-1, 0], [1, 0]] if is_inbound_and_number(char_idx + x, line_idx + y, file_contents)])
                
                found = [[char_idx + x, line_idx + y] for x, y in [[-1, 1], [0, 1], [1, 1]] if is_inbound_and_number(char_idx + x, line_idx + y, file_contents)]
                if len(found) == 3:
                    adj_numbers.append([char_idx + 1, line_idx + 1])
                elif len(found) == 1:
                    adj_numbers.extend(found)
                elif len(found) == 2:
                    if abs(found[0][0] - found[1][0]) == 1:
                        adj_numbers.append(found[0])
                    else:
                        adj_numbers.extend(found)
            
                found = [[char_idx + x, line_idx + y] for x, y in [[-1, -1], [0, -1], [1, -1]] if is_inbound_and_number(char_idx + x, line_idx + y, file_contents) ]
                if len(found) == 3:
                    adj_numbers.append([char_idx - 1, line_idx - 1])
                elif len(found) == 1:
                    adj_numbers.extend(found)
                elif len(found) == 2:
                    if abs(found[0][0] - found[1][0]) == 1:
                        adj_numbers.append(found[0])
                    else:
                        adj_numbers.extend(found)
                if len(adj_numbers) == 2:
                    product = 1
                    for adj_num_x, adj_num_y in adj_numbers:
                        product *= get_num_from_coords(adj_num_x, adj_num_y, file_contents)
                    running_sum += product

    print(running_sum)
    return running_sum


def start():
    get_file_contents("inputs/day3.txt", day3)
    get_file_contents("inputs/day3.txt", day3_pt2)


start()