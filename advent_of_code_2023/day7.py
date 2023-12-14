from aocd import get_data, submit
from enum import IntEnum
from functools import total_ordering

day = 7  # FILL DAY
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"  # FILL EXAMPLE IF YOU WANT TO USE IT
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

CARD_VALUES = {"J":-1,"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"Q":10,"K":11,"A":12}

class CardType(IntEnum):
    HIGH = 0
    PAIR = 1
    TWOPAIR = 2
    THREEKIND = 3
    FULLHOUSE = 4
    FOURKIND = 5
    FIVEKIND = 6


@total_ordering
class Card:
    def __init__(self, line, with_complex = False):
        self.values, bid = line.split(" ")
        self.bid = int(bid)
        self.card_type = self._get_card_type(with_complex)
    
    def _get_card_type(self, with_complex):
        if "J" in self.values and with_complex:
            count_dict = self._get_complex_count_dict()
        else:
            count_dict = self._get_simple_count_dict()
        return self._get_card_type_from_count_dict(count_dict)
    
    def _get_complex_count_dict(self):
        count_dict = self._get_simple_count_dict()
        j_count = count_dict.pop("J")
        if j_count == 5:
            return {"J": 5}
        
        max_value = max(count_dict.values())
        for k, v in count_dict.items():
            if v == max_value:
                count_dict[k] += j_count
                return count_dict
    
    def _get_simple_count_dict(self):
        count_dict = {}
        for l in self.values:
            if l in count_dict:
                count_dict[l] += 1
            else:
                count_dict[l] = 1
        return count_dict
    
    def _get_card_type_from_count_dict(self, count_dict):
        max_count = max(count_dict.values())
        if max_count == 5:
            return CardType.FIVEKIND
        if max_count == 4:
            return CardType.FOURKIND
        if max_count == 3:
            if min(count_dict.values()) == 2:
                return CardType.FULLHOUSE
            else:
                return CardType.THREEKIND
        if max_count == 2:
            if len(count_dict.values()) == 3:
                return CardType.TWOPAIR
            else:
                return CardType.PAIR
        return CardType.HIGH
    
    def wins_on_value(self, other):
        for own_value, other_value in zip(self.values, other.values):
            if CARD_VALUES[own_value] > CARD_VALUES[other_value]:
                return True
            elif CARD_VALUES[own_value] < CARD_VALUES[other_value]:
                return False
    
    def __lt__(self,other):
        if self.card_type > other.card_type:
            return True
        elif self.card_type < other.card_type:
            return False
        else:
            return self.wins_on_value(other)
    
    def __eq__(self,other):
        return (self.card_type == other.card_type) & (self.values == other.values)
    
    def __repr__(self):
        return f"{self.values} {self.card_type.name} ({self.bid})" 


cards = [Card(line) for line in data_list]

cards = sorted(cards, reverse = True)

winnings = 0
for i, card in enumerate(cards):
    winnings += (i+1) * card.bid


# MAKE SOME STUFF

part = "a"
answer = winnings # USE THE STUFF
print(answer)
# 248836197
if submit_a:
    submit(answer, part = part, day = day, year = year)


cards = [Card(line, True) for line in data_list]

cards = sorted(cards, reverse = True)

winnings = 0
for i, card in enumerate(cards):
    print(card)
    winnings += (i+1) * card.bid
    print(winnings)
    print()



part = "b"
answer = winnings # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
