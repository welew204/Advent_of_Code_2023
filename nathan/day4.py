from collections import defaultdict, deque
from helpers.get_file_contents import get_file_contents


def day4(input_file_contents):
    file_contents = [line[:-1] for line in input_file_contents]  # remove trailing newline char
    total = 0
    card_matches_list = []
    for card in file_contents:
        possible_winning_numbers_start_idx = card.index(":") + 2
        possible_winning_numbers_end_idx = card.index("|") - 1
        possible_winning_numbers_raw = card[possible_winning_numbers_start_idx:possible_winning_numbers_end_idx].split(" ")
        possible_winning_numbers = [int(n) for n in possible_winning_numbers_raw if n != ""]

        given_numbers_start_idx = card.index("|") + 2
        given_numbers_raw = card[given_numbers_start_idx:].split(" ")
        given_numbers = [int(n) for n in given_numbers_raw if n != ""]

        winning_numbers_count = 0
        for n in given_numbers:
            if n in possible_winning_numbers:
                winning_numbers_count += 1

        card_score = 0
        for i in range(winning_numbers_count):
            if i == 0:
                card_score = 1
            else:
                card_score *= 2
        total += card_score
        card_matches_list.append(winning_numbers_count)
    return total, card_matches_list


def day4_part2(input_file_contents):
    total = 0
    _, card_matches_list = day4(input_file_contents)
    matches_map = dict([(key, value) for key, value in enumerate(card_matches_list)])
    counts_map = defaultdict(int)
    q = deque(idx for idx, _ in enumerate(card_matches_list))
    while q:
        curr_idx = q.popleft()
        counts_map[curr_idx] += 1
        lower = curr_idx+1
        upper = matches_map[curr_idx] + curr_idx + 1
        for copy_idx in range(lower, min(upper, len(card_matches_list))):
            q.append(copy_idx)
    for card_idx, count in counts_map.items():
        total += count
    return total


def start():
    result, _ = get_file_contents("inputs/day4.txt", day4)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day4.txt", day4_part2)
    print("(Part 2) result: ", part2_result)


start()