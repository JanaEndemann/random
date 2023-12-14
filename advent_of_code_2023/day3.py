from aocd import get_data, submit
from collections import defaultdict

day = 3
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = ""  # FILL EXAMPLE IF YOU WANT TO USE IT
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

class Index:
    def __init__(self, row, col, line_str, prev_line_str, next_line_str):
        self.row = row
        self.col = col
        self.line_str = line_str
        self.prev_line_str = prev_line_str
        self.next_line_str = next_line_str
        self.start_of_number = self.is_start_of_number()
        if self.start_of_number:
            self.full_number, self.len_num = self.get_full_number()
            self.all_neighbors = self.get_all_neighbors()
            self.any_symbols = self.has_any_symbols()
        else:
            self.any_symbols = False
        
    
    def is_start_of_number(self):
        is_number = self.line_str[self.col].isnumeric()
        if self.col == 0:
            return is_number
        elif not is_number:
            return is_number
        else:
            last_is_number = self.line_str[self.col-1].isnumeric()
            return not last_is_number
    
    def get_full_number(self):
        i = self.col
        full_number = ""
        while i < len(self.line_str):
            i_str = self.line_str[i]
            if not i_str.isnumeric():
                break
            full_number += i_str
            i+=1
        return int(full_number), i - self.col
    
    def get_all_neighbors(self):
        neighbors = {}
        if self.col == 0:
            col_from = 0
        else:
            col_from = self.col - 1
            neighbors[self.row,col_from] = self.line_str[col_from]
        
        if (self.col + self.len_num) == len(self.line_str):
            col_until = self.col + self.len_num -1
        else:
            col_until = self.col + self.len_num
            neighbors[self.row,col_until] = self.line_str[col_until]
        
        if self.prev_line_str is not None:
            for c in range(col_from, col_until + 1):
                neighbors[self.row-1,c] = self.prev_line_str[c]
        
        if self.next_line_str is not None:
            for c in range(col_from, col_until + 1):
                neighbors[self.row+1,c] = self.next_line_str[c]
        
        return neighbors
    
    def has_any_symbols(self):
        return any(n != "." for n in self.all_neighbors.values())



# TEST = Index(4,"....123",None,None)
# print(TEST.full_number)

all_inds = []
prev_lines = [None] + data_list[:-1]
next_lines = data_list[1:] + [None]

for row, (line, prev_line, next_line) in enumerate(zip(data_list, prev_lines, next_lines)):
    for col in range(len(line) -1):
        ind = Index(row, col, line, prev_line, next_line)
        if ind.start_of_number:
            all_inds.append(ind)


part = "a"
answer =  sum(ind.full_number for ind in all_inds if ind.any_symbols) # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

potential_gears = defaultdict(list)
for ind in all_inds:
    for loc, n in ind.all_neighbors.items():
        if n == "*":
            potential_gears[loc].append(ind.full_number)

gears_list = [nums[0] * nums[1] for _, nums in potential_gears.items() if len(nums) == 2]

part = "b"
answer = sum(gears_list) # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
