from aocd import get_data, submit

day =   # FILL DAY
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

part = "a"
answer =  # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

part = "b"
answer = # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
