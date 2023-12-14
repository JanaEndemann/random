from aocd import get_data, submit

day = 5  # FILL DAY
year = 2023
use_example=True
submit_a = False
submit_b = False

if use_example:
    data = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light\nmap:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

# MAKE SOME STUFF
seeds  = [int(seed.strip()) for seed in data_list[0][7:].split(" ")]

class Map:
    def __init__(self, dest_start, source_start, range_len):
        self.destination_start = int(dest_start)
        self.source_start = int(source_start)
        self.range_length = int(range_len)
        self.destination_end = self.destination_start + self.range_length -1
        self.source_end = self.source_start + self.range_length -1
        self.offset = self.destination_start - self.source_start
    
    def does_map(self, range_start, range_end):
        if self.source_start > range_end:
            return False
        
        if self.source_end < range_start:
            return False
        
        return True
    
    def map(self, range_start, range_end):
        start_map = max(range_start, self.source_start)
        end_map = min(range_end, self.source_end)
        return Map(start_map + self.offset, start_map, end_map - start_map)
    
    def map_int(self, map_value):
        return map_value + self.offset
    
    def __repr__(self):
        return f"MAP {self.source_start}:{self.source_end} to {self.destination_start}:{self.destination_end}"


mappings = []
mapping_list = []
for line in data_list[2:]:
    if line == "":
        mappings.append(mapping_list)
        mapping_list = []
    elif not line[0].isnumeric():
        continue
    else:
        dest_start, source_start, range_len = line.split(" ")
        mapping_list.append(Map(dest_start, source_start, range_len))

mappings.append(mapping_list)

def get_location(seed_int, mappings_list, verbose = True):
    current_value = seed_int
    mapping_nr = 1
    for mapping in mappings_list:
        if verbose:
            print(f"mapping nr {mapping_nr}")
        
        mapping_nr+=1
        for mapper in mapping:
            if mapper.does_map(current_value, current_value):
                if verbose:
                    print(f"{current_value} maps to...")
                
                current_value = mapper.map_int(current_value)
                if verbose:
                    print(f"...{current_value}!\n")
                
                break
    
    return current_value


locations = [get_location(seed, mappings) for seed in seeds]

part = "a"
answer = min(locations) # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)

seed_starts = [seed for i, seed in enumerate(seeds) if i%2 == 0]
seed_rls = [seed for i, seed in enumerate(seeds) if i%2 == 1]
    
# TODO, this is not wokring...
seed_mapping = {}
for seed_start, seed_rl in zip(seed_starts, seed_rls):
    for mapping_list in mappings:
        level_map = []
        for mapping in mapping_list:
            if mapping.does_map(seed_start,seed_rl+seed_start):
                level_map.append(mapping.map(seed_start,seed_rl+seed_start)


part = "b"
answer = "" # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
