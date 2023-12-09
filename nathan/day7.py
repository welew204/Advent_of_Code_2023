from helpers.get_file_contents import get_file_contents, remove_line_breaks
from collections import defaultdict
import functools


card_type = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_type_joker = [
    "A",
    "K",
    "Q",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "J",
]

hand_type = ["five", "four", "full_house", "three", "two_pair", "one_pair", "high_card"]


def get_hand_type_idx(hand):
    counts_map = defaultdict(int)
    for card in hand:
        counts_map[card] += 1

    counts = counts_map.values()

    if 5 in counts:
        return "five"
    elif 4 in counts:
        return "four"
    elif 3 in counts and 2 in counts:
        return "full_house"
    elif 3 in counts:
        return "three"
    elif [count for count in counts].count(2) == 2:
        return "two_pair"
    elif 2 in counts:
        return "one_pair"
    else:
        return "high_card"


def get_hand_type_with_jokers_idx(hand):
    counts_map = defaultdict(int)
    for card in hand:
        counts_map[card] += 1

    joker_count = counts_map["J"]
    counts = counts_map.values()

    if 5 in counts:
        return "five"

    if joker_count > 0:
        if 4 in counts:
            return "five"
        elif 3 in counts and 2 in counts:
            return "five"
        elif 3 in counts:
            return "four"
        elif [count for count in counts].count(2) == 2 and joker_count == 2:
            return "four"
        elif [count for count in counts].count(2) == 2 and joker_count == 1:
            return "full_house"
        elif 2 in counts:
            return "three"
        else:
            return "one_pair"
    else:
        if 4 in counts:
            return "four"
        elif 3 in counts and 2 in counts:
            return "full_house"
        elif 3 in counts:
            return "three"
        elif [count for count in counts].count(2) == 2:
            return "two_pair"
        elif 2 in counts:
            return "one_pair"
        else:
            return "high_card"


def tie_break(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        idx_1 = card_type.index(hand1[i])
        idx_2 = card_type.index(hand2[i])
        if idx_1 < idx_2:
            return -1
        else:
            return 1
    return 0


def tie_break_w_jokers(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        idx_1 = card_type_joker.index(hand1[i])
        idx_2 = card_type_joker.index(hand2[i])
        if idx_1 < idx_2:
            return -1
        else:
            return 1
    return 0


def compare(hand_and_bid1, hand_and_bid2):
    hand1, _ = hand_and_bid1.split(" ")
    hand2, _ = hand_and_bid2.split(" ")
    hand1_type_idx = hand_type.index(get_hand_type_idx(hand1))

    hand2_type_idx = hand_type.index(get_hand_type_idx(hand2))
    if hand1_type_idx == hand2_type_idx:
        return tie_break(hand1, hand2)
    elif hand1_type_idx > hand2_type_idx:
        return 1
    else:
        return -1


def compare_with_jokers(hand_and_bid1, hand_and_bid2):
    hand1 = hand_and_bid1.split(" ")[0]
    hand2 = hand_and_bid2.split(" ")[0]

    hand_type_1 = get_hand_type_with_jokers_idx(hand1)
    print("==", hand1 + " " + hand_type_1)
    hand_type_2 = get_hand_type_with_jokers_idx(hand2)
    hand1_type_idx = hand_type.index(hand_type_1)
    hand2_type_idx = hand_type.index(hand_type_2)
    if hand1_type_idx == hand2_type_idx:
        return tie_break_w_jokers(hand1, hand2)
    elif hand1_type_idx > hand2_type_idx:
        return 1
    else:
        return -1


def day7_part1(file_contents):
    total_winnings = 0
    ranked_hands = sorted(file_contents, key=functools.cmp_to_key(compare))
    for i in range(len(ranked_hands)):
        bid = int(ranked_hands[len(ranked_hands) - i - 1].split(" ")[1])
        total_winnings += (i + 1) * bid
    return total_winnings


def day7_part2(file_contents):
    total_winnings = 0
    ranked_hands = sorted(file_contents, key=functools.cmp_to_key(compare_with_jokers))
    for i in range(len(ranked_hands)):
        bid = int(ranked_hands[len(ranked_hands) - i - 1].split(" ")[1])
        total_winnings += (i + 1) * bid
    return total_winnings


def start():
    # result = get_file_contents("inputs/day7.txt", day7_part1, remove_line_breaks)
    # print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day7.txt", day7_part2, remove_line_breaks)
    print("(Part 2) result: ", part2_result)


start()
data = [
    "32T3K 765\n",
    "T55J5 684\n",
    "KK677 28\n",
    "KTJJT 220\n",
    "QQQJA 483\n",
]
day7_part2(remove_line_breaks(data))
# print(day6_part2(data))
