import requests

import day2
import day3
from day1 import part1

PAGE = "https://adventofcode.com/2021/day/NDAY/input"
SESSION = "53616c7465645f5fd91958053f6a245dd61da5123222135d9587a01952cb02be2a627f24d1c2714e9110f9ff3c9ce9fb"

FUNCS = {1: (part1,),
         2: (day2.part1, day2.part2),
         3: (day3.part1,)}


def get_input(day):
    url = PAGE.replace("NDAY", str(day))
    resp = requests.get(url, cookies={"session": SESSION})
    lines = resp.content.decode('utf-8').split("\n")
    return lines


def run(day, part):
    lines = get_input(day)
    func = FUNCS[day][part]
    solution = func(lines)
    print(f"SOLUTION is {solution}")


if __name__ == "__main__":
    run(3, 0)
