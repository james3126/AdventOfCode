# Advent of Code - Year 2015 - Day 3
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    homes_list = [[0,0]]

    direction_map = {'^':[0,1],'v':[0,-1],'>':[1,0],'<':[-1,0]}

    for direction in puzzle_input:
        current_place = homes_list[-1]
        new_place = [sum(x) for x in zip(current_place, direction_map[direction])]
        homes_list.append(new_place)

    unique_houses = []
    for i in homes_list:
        if i not in unique_houses:
            unique_houses.append(i)

    print(f"Unique houses: {len(unique_houses)}")

def part_2():
    homes_list = [[0,0],[0,0]]

    direction_map = {'^':[0,1],'v':[0,-1],'>':[1,0],'<':[-1,0]}

    for direction in puzzle_input:
        current_place = homes_list[-2]
        new_place = [sum(x) for x in zip(current_place, direction_map[direction])]
        homes_list.append(new_place)

    unique_houses = []
    for i in homes_list:
        if i not in unique_houses:
            unique_houses.append(i)

    print(f"Unique houses: {len(unique_houses)}")


if __name__ == "__main__":
    part_1()
    part_2()
