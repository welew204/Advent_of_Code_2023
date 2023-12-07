from helpers.get_file_contents import get_file_contents, remove_line_breaks


def day6_part1(file_contents):
    races = zip(
        [int(x) for x in file_contents[0].split(":")[1].split()],
        [int(x) for x in file_contents[1].split(":")[1].split()],
    )
    total_ways_to_win_product = 1
    for race_time, race_distance_record in races:
        ways_to_win_for_race = 0
        for charge_time in range(0, race_time + 1):
            distance = charge_time * (race_time - charge_time)
            if distance > race_distance_record:
                ways_to_win_for_race += 1
        total_ways_to_win_product *= ways_to_win_for_race
    return total_ways_to_win_product


def day6_part2(file_contents):
    race_time = int("".join(file_contents[0].split(":")[1].split()))
    race_distance_record = int("".join(file_contents[1].split(":")[1].split()))
    total_ways_to_win_product = 1
    ways_to_win_for_race = 0
    for charge_time in range(0, race_time + 1):
        distance = charge_time * (race_time - charge_time)
        if distance > race_distance_record:
            ways_to_win_for_race += 1
    total_ways_to_win_product *= ways_to_win_for_race
    return total_ways_to_win_product


def start():
    result = get_file_contents("inputs/day6.txt", day6_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day6.txt", day6_part2, remove_line_breaks)
    print("(Part 2) result: ", part2_result)


start()
# data = ["Time:      7  15   30\n", "Distance:  9  40  200\n"]
# # day6_part1(data)
# print(day6_part2(data))
