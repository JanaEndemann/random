from copy import deepcopy
from typing import List


def part1(lines: List[str]) -> int:
    cnt_0 = [0 for _ in lines[0]]
    cnt_1 = [0 for _ in lines[0]]
    for line in lines:
        for i, val in enumerate(line):
            if val == '1':
                cnt_1[i] += 1
            else:
                cnt_0[i] += 1

    gamma_str = ""
    epsilon_str = ""
    for i in range(len(cnt_0)):
        if cnt_1[i] > cnt_0[i]:
            gamma_str += '1'
            epsilon_str += '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    print(gamma)
    print(epsilon)
    return gamma * epsilon


def part2(lines: List[str]) -> int:
    oxygen_candidates = deepcopy(lines)
    for i in range(len(lines[0])):
        zeroes = [cand for cand in oxygen_candidates if len(cand) > 0 and cand[i] == '0']
        ones = [cand for cand in oxygen_candidates if len(cand) > 0 and cand[i] == '1']
        print(f"zeroes: {len(zeroes)}, ones: {len(ones)}")
        if len(zeroes) > len(ones):
            print(f"oxygen bit {i} is a 0")
            oxygen_candidates = zeroes
        else:
            print(f"oxygen bit {i} is a 1")
            oxygen_candidates = ones

        print(oxygen_candidates)
        if len(oxygen_candidates) == 1:
            break
    oxygen = int(oxygen_candidates[0], 2)

    scrubber_candidates = deepcopy(lines)
    for i in range(len(lines[0])):
        zeroes = [cand for cand in scrubber_candidates if len(cand) > 0 and cand[i] == '0']
        ones = [cand for cand in scrubber_candidates if len(cand) > 0 and cand[i] == '1']
        print(f"zeroes: {len(zeroes)}, ones: {len(ones)}")
        if len(ones) >= len(zeroes):
            print(f"scrubber bit {i} is a 0")
            scrubber_candidates = zeroes
        else:
            print(f"scrubber bit {i} is a 1")
            scrubber_candidates = ones

        print(scrubber_candidates)
        if len(scrubber_candidates) == 1:
            break
    scrubber = int(scrubber_candidates[0], 2)

    print(oxygen)
    print(scrubber)
    return oxygen * scrubber
