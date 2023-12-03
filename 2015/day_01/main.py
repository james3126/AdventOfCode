# Advent of Code - Year 2015 - Day 1
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

current_floor = 0
basement_entered = False

for i,character in enumerate(puzzle_input):
    if character == "(":
        current_floor += 1

    if character == ")":
        current_floor -= 1

    if (current_floor < 0) and (basement_entered == False):
        basement_entered = True
        print(f"First basement character: {i+1}")

print(f"Final floor: {current_floor}")
