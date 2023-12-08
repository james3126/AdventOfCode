# Advent of Code - Year 2023 - Day 8
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
    instructions, lookup_table = puzzle_input.split('\n\n')
    lookup_table_dict = {}

    current_nodes = []
    for column in lookup_table.split('\n'):
        key,val = column.split(' = ')
        lookup_table_dict[key] = val[1:-1].split(', ')
        if key[2] == "A":
            current_nodes.append(key)

    # print(current_nodes)

    # Keep running until everything checks out on the inner loop
    steps_to_end  = 0
    all_finished  = False
    while not all_finished:
        for instruction in list(instructions):
            steps_to_end += 1
            direction = 1 if instruction == "R" else 0
            for i,node in enumerate(current_nodes):
                current_nodes[i] = lookup_table_dict[node][direction]

            #print(current_nodes,instruction)

            nodes_finished = True
            valid_nodes = 0
            #print("CHECK")
            for node in current_nodes:
                if node[-1] == "Z":
                    valid_nodes += 1
                    # print("VALID",node,current_nodes.index(node),steps_to_end)
                    # if current_nodes.index(node) == 1:
                        # print(node, steps_to_end, valid_nodes)

                else:
                    nodes_finished = False
                    # print("INVALID NODE",node)
                    #nodes_finished = False
                    #break
                #else:
                    #print("VALID",node)

            if valid_nodes == len(current_nodes):
                print("FINISH",steps_to_end)
                break
            #    break
    
    print("Part 2: ",steps_to_end)

if __name__ == "__main__":
    part_1()
    part_2()
