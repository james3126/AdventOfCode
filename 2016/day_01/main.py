# Advent of Code - Year 2016 - Day 1
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    coords = [0,0]
    current_direction = 0

    # N [1,0] | 0
    # E [0,1] | 1
    # S [-1,0]| 2
    # W [0,-1]| 3

    for instruction in puzzle_input.split(', '):
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == "R":
            current_direction += 1
        else:
            current_direction -= 1

        if current_direction % 4 == 0: coords[1] += distance
        if current_direction % 4 == 1: coords[0] += distance
        if current_direction % 4 == 2: coords[1] -= distance
        if current_direction % 4 == 3: coords[0] -= distance

    # print(coords)
    answer = abs(coords[0])+abs(coords[1])
    print("Part 1: ",answer)

def part_2():
    coords = [0,0]
    coords_list = []
    current_direction = 0
    
    for instruction in puzzle_input.split(', '):
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == "R":
            current_direction += 1
        else:
            current_direction -= 1

        if current_direction % 4 == 0:
            for i in range(distance):
                coords[1] += 1
                coords_list.append(coords[:])
        if current_direction % 4 == 1:
            for i in range(distance):
                coords[0] += 1
                coords_list.append(coords[:])
        if current_direction % 4 == 2:
            for i in range(distance):
                coords[1] -= 1
                coords_list.append(coords[:])
        if current_direction % 4 == 3:
            for i in range(distance):
                coords[0] -= 1
                coords_list.append(coords[:])

    # print(coords_list)

    def find_duplicate(inp_coords):
        temp_list = []
        for tmp_coord in inp_coords:
            # print("Checking",tmp_coord)
            # print(temp_list)
            if tmp_coord in temp_list:
                # print("Found",tmp_coord)
                return tmp_coord[:]
            else:
                temp_list.append(tmp_coord[:])

    # print(coords_list)
    first_duplicate = find_duplicate(coords_list)
    # print(first_duplicate)
    answer = abs(first_duplicate[0])+abs(first_duplicate[1])
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
