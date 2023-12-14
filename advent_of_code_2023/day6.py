from aocd import get_data, submit
from math import floor, ceil

day = 6  # FILL DAY
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = ""  # FILL EXAMPLE IF YOU WANT TO USE IT
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

# MAKE SOME STUFF
times = [int(t.strip()) for t in data_list[0].split(":")[1].split(" ") if t != ""]
distances = [int(t.strip()) for t in data_list[1].split(":")[1].split(" ") if t != ""]

def find_press_min_max(time, distance):
    press_min = (time - (time*time-4*distance)**0.5 )/2
    press_max = (time + (time*time-4*distance)**0.5 )/2
    return press_min, press_max


def get_options_for_min_max(press_min, press_max):
    return floor(press_max) - ceil(press_min) + 1


options_list = []
answer_a = 1
for t,d in zip(times, distances):
    press_min, press_max = find_press_min_max(t, d)
    options = get_options_for_min_max(press_min, press_max)
    print(f"found points {press_min} and {press_max}, leading to {options} options\n")
    options_list.append(options)
    answer_a *= options


part = "a"
answer = answer_a # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

long_time = ""
for t in times:
    long_time += str(t)

long_time = int(long_time)

long_distance = ""
for t in distances:
    long_distance += str(t)

long_distance = int(long_distance)

press_min, press_max = find_press_min_max(long_time, long_distance)
options = get_options_for_min_max(press_min, press_max)

part = "b"
answer = options # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
