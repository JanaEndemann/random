from collections import defaultdict
from typing import List


def part1(lines: List[str]) -> int:
    coords = defaultdict(int)
    for line in lines:
        if len(line) == 0:
            continue
        first, second = line.split(" -> ")
        x1, y1 = [int(s) for s in first.split(",")]
        x2, y2 = [int(s) for s in second.split(",")]

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coords[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coords[(i, y1)] += 1
    too_dangerous = [1 for val in coords.values() if val >= 2]
    return sum(too_dangerous)


def part2(lines: List[str]) -> int:
    coords = defaultdict(int)
    for line in lines:
        if len(line) == 0:
            continue
        first, second = line.split(" -> ")
        x1, y1 = [int(s) for s in first.split(",")]
        x2, y2 = [int(s) for s in second.split(",")]

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coords[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coords[(i, y1)] += 1
        elif (x2 - x1) == (y2 - y1):
            step_dir = 1 if x1 < x2 else -1
            diff = x2 - x1
            for i in range(0, diff + step_dir, step_dir):
                coords[(x1 + i, y1 + i)] += 1
        else:
            step_dir = 1 if x1 < x2 else -1
            diff = x2 - x1
            for i in range(0, diff + step_dir, step_dir):
                coords[(x1 + i, y1 - i)] += 1
    too_dangerous = [1 for val in coords.values() if val >= 2]
    return sum(too_dangerous)
