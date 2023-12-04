import os
from helpers.get_file_contents import get_file_contents

# Get the current working directory
current_directory = os.getcwd()

# maxes 12 red cubes, 13 green cubes, and 14 blue cubes
max_map = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_line_valid(line: str):
    # "Game 2: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    game_idx = int(line[len("Game ") : line.index(":")])  # "2"
    line = line[
        line.index(":") + 1 :
    ]  # " 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    line = (
        line.strip()
    )  # "7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    games = line.split(
        ";"
    )  # ["7 red, 14 blue", " 2 blue, 3 red, 3 green", " 4 green, 12 blue, 15 red", " 3 green, 12 blue, 3 red", " 11 red, 2 green"]
    for game in games:
        game = game.strip()  # "7 red, 14 blue"
        cubes = game.split(",")  # ["7 red", " 14 blue"]
        for cube in cubes:
            cube = cube.strip()  # "7 red"
            cube = cube.split(" ")  # ["7", "red"]
            num_cubes = int(cube[0])  # "7"
            cube_color = cube[1]  # "red"
            if num_cubes > max_map[cube_color]:
                return False
    return True


def get_max_cubes(line: str):
    # "Game 2: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    game_idx = int(line[len("Game ") : line.index(":")])  # "2"
    line = line[
        line.index(":") + 1 :
    ]  # " 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    line = (
        line.strip()
    )  # "7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
    games = line.split(
        ";"
    )  # ["7 red, 14 blue", " 2 blue, 3 red, 3 green", " 4 green, 12 blue, 15 red", " 3 green, 12 blue, 3 red", " 11 red, 2 green"]
    max_blue = 0
    max_red = 0
    max_green = 0
    for game in games:
        game = game.strip()
        cubes = game.split(",")
        for cube in cubes:
            cube = cube.strip()
            cube = cube.split(" ")
            num_cubes = int(cube[0])
            cube_color = cube[1]
            if cube_color == "blue":
                max_blue = max(max_blue, num_cubes)
            elif cube_color == "red":
                max_red = max(max_red, num_cubes)
            elif cube_color == "green":
                max_green = max(max_green, num_cubes)
    return max_blue, max_red, max_green


def part_1(file_contents):
    res = 0
    # Iterate over each line in the file
    for line in file_contents:
        line: str = (
            line.strip()
        )  # "Game 2: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
        game_idx = int(line[len("Game ") : line.index(":")])  # "2"
        if is_line_valid(line):
            res += game_idx
    print(res)


def part_2(file_contents):
    res = 0
    for line in file_contents:
        line: str = (
            line.strip()
        )  # "Game 2: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
        min_blue, min_red, min_green = get_max_cubes(line)
        res += min_blue * min_red * min_green
    print(res)


def start():
    get_file_contents("inputs/day2.txt", part_1)
    get_file_contents("inputs/day2.txt", part_2)


start()


# Tests
# print(is_line_valid("Game 2: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green") == False)
# print(is_line_valid("Game 3: 7 red, 13 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 11 red; 3 green, 12 blue, 3 red; 11 red, 2 green") == True)
