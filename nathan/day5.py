from helpers.get_file_contents import get_file_contents, remove_line_breaks
import re
from itertools import groupby


def get_destination(prevSource, mapperLine):
    dest_range_start, source_range_start, range_len = [
        int(x) for x in mapperLine.split(" ")
    ]
    if source_range_start <= prevSource < (source_range_start + range_len):
        return dest_range_start + (prevSource - source_range_start)
    return None


def find_min_location_number(seeds, file_contents):
    lowest_location_number = float("inf")
    for seed in seeds:
        prevSource = int(seed)
        for currLineIdx in range(1, len(file_contents)):
            currLine = file_contents[currLineIdx]
            if "map:" in currLine:
                mapperLineIdx = currLineIdx + 1
                mapperLine = file_contents[mapperLineIdx]
                while mapperLine != "":
                    found = get_destination(prevSource, mapperLine)
                    if found is not None:
                        prevSource = found
                        break
                    if mapperLineIdx == (len(file_contents) - 1):
                        break
                    mapperLineIdx += 1
                    mapperLine = file_contents[mapperLineIdx]

        lowest_location_number = min(lowest_location_number, prevSource)
    return lowest_location_number


def day5_part1(file_contents):
    seeds = file_contents[0].split(": ")[1].strip().split(" ")
    return find_min_location_number(seeds, file_contents)


def find_overlap(r1, r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    o_start = max(r1_start, r2_start)
    o_end = min(r1_end, r2_end)
    return (o_start, o_end) if o_start <= o_end else None


def shift_range(r, delta):
    r_start, r_end = r
    return (r_start + delta, r_end + delta)


def split_range(r, overlap):
    result = set()

    o_start, o_end = overlap
    r_start, r_end = r

    if r_start < o_start:
        result.add((r_start, o_start - 1))

    if r_end > o_end:
        result.add((o_end + 1, r_end))

    return result


def as_range(start_count):
    start, count = start_count
    return (start, start + count - 1)


def parse_ints(s):
    return list(map(int, re.findall("\d+", s)))


def split_list(lst):
    return (list(group) for _, group in groupby(lst, lambda x: x != ""))


def day5_part2(file_contents):
    seeds = parse_ints(file_contents[0])
    maps = [[parse_ints(x) for x in m[1:]] for m in split_list(file_contents[2:])]

    ranges = set(map(as_range, zip(seeds[0::2], seeds[1::2])))

    for m in maps:
        shifted_ranges = set()

        for to, start, count in m:
            for r in ranges.copy():
                if overlap := find_overlap(r, as_range((start, count))):
                    ranges.remove(r)
                    ranges |= split_range(r, overlap)
                    shifted_ranges.add(shift_range(overlap, to - start))

        ranges |= shifted_ranges

    return ranges


def start():
    result = get_file_contents("inputs/day5.txt", day5_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    part2_result = get_file_contents("inputs/day5.txt", day5_part2, remove_line_breaks)
    print("(Part 2) result: ", min(min(part2_result)))


start()
