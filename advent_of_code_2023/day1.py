from aocd import get_data, submit

day = 1
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")


NUMBER_DICT = {"one":1,"two":2,"three":3,"four":4, "five":5,"six":6,"seven":7, "eight":8, "nine":9}

def replace_number_str(s:str) -> str:
    for n_str, num in NUMBER_DICT.items():
        s = s.replace(n_str, str(num))
    return s


def find_first_int(s: str, from_start = True, with_replace = False) -> int:
    for i in range(len(s)):
        single_digit = s[i] if from_start else s[-(i+1)]
        if single_digit.isnumeric():
            return int(single_digit)
        if not with_replace:
            continue
            
        if from_start:
            sub_str = s[:i+1]
        else:
            sub_str = s[(len(s)-i-1):]
        n_str = replace_number_str(sub_str)
        for j in n_str:
            if j.isnumeric():
                return int(j)


#find_first_int("oneight3oneight",True,True)
#find_first_int("oneight3oneight",False,True)

def number_from_line(line: str, part: str) -> int:
    return 10 * find_first_int(line, True, part == "b") + find_first_int(line, False, part == "b")


part = "a"
answer = sum(number_from_line(line, part) for line in data_list)
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

part = "b"
answer = sum(number_from_line(line, part) for line in data_list)
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
