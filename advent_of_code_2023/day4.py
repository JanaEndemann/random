from aocd import get_data, submit

day = 4  # FILL DAY
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = ""  # FILL EXAMPLE IF YOU WANT TO USE IT
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

def split_nrs(nr_str):
    return [int(s.strip()) for s in nr_str.split(" ") if s != ""]


class Card:
    def __init__(self, line_str: str):
        card_str, rest = line_str.split(":")
        self.nr = int(card_str[5:])
        win_str, card_str = rest.split("|")
        self.winning_nrs = split_nrs(win_str.strip())
        self.card_nrs = split_nrs(card_str.strip())
        
    def get_matches(self):
        matches = 0
        for win in self.winning_nrs:
            if win in self.card_nrs:
                matches += 1
        return matches
        
    def get_points(self):
        matches = self.get_matches()
        if matches == 0:
            return matches
        else:
            return 2**(matches-1)
    
    def __repr__(self):
        return f"Card {self.nr}: {self.get_matches()} matches"


cards = [Card(line) for line in data_list]

part = "a"
answer = sum(c.get_points() for c in cards) # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

card_count = [1]*len(cards)
for card in cards:
    print(card)
    this_card_count = card_count[card.nr-1]
    print(this_card_count)
    for i in range(card.get_matches()):
        change_index = card.nr +i
        if change_index < len(card_count):
            card_count[change_index] += this_card_count


part = "b"
answer = sum(card_count) # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
