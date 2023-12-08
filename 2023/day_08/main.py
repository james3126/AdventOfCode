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
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
