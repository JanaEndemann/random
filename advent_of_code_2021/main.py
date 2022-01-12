import requests

import day2
import day3
import day4
import day5
from day1 import part1

PAGE = "https://adventofcode.com/2021/day/NDAY/input"
SESSION = "53616c7465645f5fd91958053f6a245dd61da5123222135d9587a01952cb02be2a627f24d1c2714e9110f9ff3c9ce9fb"

FUNCS = {1: (part1,),
         2: (day2.part1, day2.part2),
         3: (day3.part1, day3.part2),
         4: (day4.part1, day4.part2),
         5: (day5.part1, day5.part2)}


def get_input(day):
    url = PAGE.replace("NDAY", str(day))
    resp = requests.get(url, cookies={"session": SESSION})
    lines = resp.content.decode('utf-8').split("\n")
    return lines


def get_example():
    example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    return example.split("\n")


def run(day: int, part: int, use_example: bool = False):
    if use_example:
        lines = get_example()
    else:
        lines = get_input(day)
    func = FUNCS[day][part]
    solution = func(lines)
    print(f"SOLUTION is {solution}")


if __name__ == "__main__":
    run(5, 1, use_example=False)
