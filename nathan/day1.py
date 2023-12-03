from helpers.get_file_contents import get_file_contents

numbers_spelled_set = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def number_from_outer_digits(input_str: str):
    left_digit = None
    right_digit = None

    for i, char in enumerate(input_str):
        if char.isdigit():
            left_digit = char
        else:
            for idx, n in enumerate(numbers_spelled_set):
                if input_str[i:].startswith(n):
                    left_digit = str(idx + 1)

        if left_digit is not None:
            break

    for i in range(len(input_str) - 1, -1, -1):
        if input_str[i].isdigit():
            right_digit = input_str[i]
        else:
            for idx, n in enumerate(numbers_spelled_set):
                start = i - len(n) + 1
                if input_str[start : i + 1] == n:
                    right_digit = str(idx + 1)
                    break
        if right_digit is not None:
            break

    return int(left_digit + right_digit)


def cb(file_contents):
    res = 0
    # Iterate over each line in the file
    for line in file_contents:
        line = line.strip()
        res += number_from_outer_digits(line)
    print(res)


def start():
    get_file_contents("inputs/day1.txt", cb)


start()

# cases = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

# for case in cases:
#     print(number_from_outer_digits(case))
