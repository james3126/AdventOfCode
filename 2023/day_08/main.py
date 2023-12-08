# Advent of Code - Year 2023 - Day 8
import math
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    instructions, lookup_table = puzzle_input.split('\n\n')
    lookup_table_dict = {}

    for column in lookup_table.split('\n'):
        key,val = column.split(' = ')
        lookup_table_dict[key] = val[1:-1].split(', ')
    # print(lookup_table_dict)

    current_node = "AAA"
    steps_to_end = 0
    while current_node != "ZZZ":
        for instruction in list(instructions):
            steps_to_end += 1
            direction = 1 if instruction == "R" else 0
            current_node = lookup_table_dict[current_node][direction]
            # print(current_node)
            if current_node == "ZZZ":
                break
    
    print("Part 1: ",steps_to_end)

def part_2():
    # After noting that the bruteforce method was - most likely - the wrong method due to the run-time
    # I've had to have a brief look at the subreddit to see what I may be missing. Other than noting that during the brute force,
    # that if we remove the search for the Z in position [-1] (for example, putting the input into part 1) then we will
    # enter an infinite loop for all values found to start with an A in position [-1].
    # This is where I was stumped on making it quicker. I knew we needed to look for a crossing point but a plan wouldn't
    # come to mind. Subreddit noted LCM in the title of the first post, and from here I was able to quickly complete the task.    
    instructions, lookup_table = puzzle_input.split('\n\n')
    lookup_table_dict = {}

    current_nodes = []
    for column in lookup_table.split('\n'):
        key,val = column.split(' = ')
        lookup_table_dict[key] = val[1:-1].split(', ')
        if key[2] == "A":
            current_nodes.append(key)
    # print(valid_starting_nodes)

    # Keep running until everything checks out on the inner loop
    list_of_steps = []
    for i in range(len(current_nodes)):
        steps_to_end  = 0
        while current_nodes[i][-1] != "Z":
            for instruction in list(instructions):
                steps_to_end += 1
                direction = 1 if instruction == "R" else 0
                current_nodes[i] = lookup_table_dict[current_nodes[i]][direction]
                if current_nodes[i][-1] == "Z":
                    print(current_nodes, steps_to_end)
                    list_of_steps.append(steps_to_end)
                    break

    # print(list_of_steps)
    answer = math.lcm(*list_of_steps)
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
