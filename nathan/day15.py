from helpers.get_file_contents import get_file_contents, remove_line_breaks
from collections import defaultdict


def day15_part1(file_contents):
    results_sum = 0
    steps = file_contents[0].split(",")
    for step in steps:
        val = 0
        for char in step:
            val += ord(char)
            val *= 17
            val = val % 256
        results_sum += val

    return results_sum


def day15_part2(file_contents):
    results_sum = 0
    boxes = defaultdict(list)
    steps = file_contents[0].split(",")
    for step in steps:
        box = 0
        label = ""
        for char in step:
            if char == "=" or char == "-":
                break
            label += char

        for char in label:
            box += ord(char)
            box *= 17
            box = box % 256

        focused_box = boxes[box]
        if "=" in step:
            box_item = f"{label} {step[-1]}"
            existing_idx = None
            for idx, el in enumerate(focused_box):
                if el.startswith(label):
                    existing_idx = idx
            if existing_idx is None:
                focused_box.append(box_item)
            else:
                focused_box[existing_idx] = box_item
        elif "-" in step:
            existing_idx = None
            for idx, el in enumerate(focused_box):
                if el.startswith(label):
                    existing_idx = idx
            if existing_idx is not None:
                del focused_box[existing_idx]

    for box in boxes:
        for idx, lens in enumerate(boxes[box]):
            results_sum += (int(box) + 1) * (idx + 1) * int(lens[-1])

    return results_sum


def start():
    # pass
    result = get_file_contents("inputs/day15.txt", day15_part1, remove_line_breaks)
    print("(Part 1) result: ", result)
    result = get_file_contents("inputs/day15.txt", day15_part2, remove_line_breaks)
    print("(Part 2) result: ", result)


start()
