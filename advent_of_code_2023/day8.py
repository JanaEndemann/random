from aocd import get_data, submit

day =  8 # FILL DAY
year = 2023
use_example=False
submit_a = False
submit_b = False

if use_example:
    data = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)"  # FILL EXAMPLE IF YOU WANT TO USE IT
    data = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)"
else:
    data = get_data(day=day, year = year)

data_list = data.split("\n")

instructions, _, *rest = data_list
nr_instructions = len(instructions)

nodes = {line[:3]: (line[7:10],line[12:15]) for line in rest}

# MAKE SOME STUFF
steps = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    if instructions[steps % nr_instructions] == 'R':
        current_node = nodes[current_node][1]
    else:
        current_node = nodes[current_node][0]
    steps += 1

part = "a"
answer = steps # USE THE STUFF
print(answer)
if submit_a:
    submit(answer, part = part, day = day, year = year)


a_nodes = [node for node in nodes if node[2] == "A"]

class NodeLoop:
    def __init__(self, instructions, nodes, start_node):
        self.start_node = start_node
        self.until_loop, self.loop = self.init_loop(instructions, nodes)
        
    def init_loop(self, instructions, nodes):
        nodes_passed = [self.start_node]
        current_node = self.start_node
        for i in range(len(nodes)):
            if instructions[i % nr_instructions] == 'R':
                next_step_int = 1
            else:
                next_step_int = 0
            current_node = nodes[current_node][next_step_int]
            if current_node in nodes_passed:
                i_before_loop = nodes_passed.index(current_node)
                break
            else:
                nodes_passed.append(current_node)
        
        before_loop = nodes_passed[:i_before_loop]
        loop = nodes_passed[i_before_loop:]
        return [n[2] == "Z" for n in before_loop], [nl[2] == "Z" for nl in loop]
    
    def is_z_at_step(self, step_i):
        if step_i < len(self.until_loop):
            return self.until_loop[step_i]
        else:
            return self.loop[(step_i - len(self.until_loop))%len(self.loop)]


node_loops = {NodeLoop(instructions,nodes, start_node) for start_node in a_nodes}
steps = 0
all_end_with_z = False
while not all_end_with_z:
    steps += 1
    all_end_with_z = all(nl.is_z_at_step(steps) for nl in node_loops)


part = "b"
answer = steps # USE MORE STUFF
print(answer)
if submit_b:
    submit(answer, part = part, day = day, year = year)
