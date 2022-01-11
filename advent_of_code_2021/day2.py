from typing import List


def part1(lines : List[str]) -> int:
    hor  =0
    depth = 0
    for line in lines:
        if len(line) == 0:
            continue
        dir, amount = line.split(" ")
        if dir == "forward":
            hor += int(amount)
        elif dir == "up":
            depth -= int(amount)
        elif dir == "down":
            depth += int(amount)
    print(hor, depth)
    return hor * depth

def part2(lines: List[str]) -> int:
    hor = 0
    depth = 0
    aim = 0
    for line in lines:
        if len(line) == 0:
            continue
        dir, amount = line.split(" ")
        if dir == "forward":
            hor += int(amount)
            depth += (int(amount) * aim)
        elif dir == "up":
            aim -= int(amount)
        elif dir == "down":
            aim += int(amount)
    print(hor, depth)
    return hor * depth