from typing import List


def part1(lines: List[str]) -> int:
    cnt_0 = [0 for _ in lines[0]]
    cnt_1 = [0 for _ in lines[0]]
    for line in lines:
        for i, val in enumerate(line):
            if val == '1':
                cnt_1[i] +=1
            else:
                cnt_0[i] +=1

    gamma_str = ""
    epsilon_str = ""
    for i in range(len(cnt_0)):
        if cnt_1[i] > cnt_0[i]:
            gamma_str+= '1'
            epsilon_str+= '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str,2)

    print(gamma)
    print(epsilon)
    return gamma * epsilon



def part2(lines) -> int:
    pass