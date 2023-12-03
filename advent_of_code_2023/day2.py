from aocd import get_data, submit

day = 2
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

COLORS = {"red": 12, "blue": 14, "green": 13}

def clean_color(c_str: str):
    for color in COLORS:
        if color in c_str:
            num = int(c_str.strip()[:-len(color)].strip())
            return color, num


def pick_valid(pick_dict) -> bool:
    color_checks = [COLORS[color] >= c_num for color, c_num in pick_dict]
    return all(color_checks)


class Game:
    def __init__(self, line_str: str):
        game_str, rest = line_str.split(":")
        self.game_nr = int(game_str[4:])
        picks = rest.split(";")
        self.all_picks = []
        for pick in picks:
            pick_list = {clean_color(p) for p in pick.split(",")}
            self.all_picks.append(pick_list)
    
    def all_picks_valid(self) -> bool:
        pick_valid_list = [pick_valid(p) for p in self.all_picks]
        return all(pick_valid_list)
    
    def min_colors(self):
        min_of_colors = {"red": 0, "blue": 0, "green": 0}
        for pick in self.all_picks:
            for color, num in pick:
                min_of_colors[color] = max(min_of_colors[color], num)
        return min_of_colors
    
    def cube(self) -> int:
        min_of_colors = self.min_colors()
        return min_of_colors["red"] * min_of_colors["blue"] * min_of_colors["green"]


games = [Game(line) for line in data_list]

part = "a"
answer = sum(game.game_nr for game in games if game.all_picks_valid())
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

part = "b"
answer = sum(game.cube() for game in games)
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
