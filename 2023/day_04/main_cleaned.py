# Advent of Code - Year 2023 - Day 4
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

def calc_wins(card): 
    winning_numbers,your_numbers = map(lambda n: n.split(),card.split(':')[1].split('|'))
    
    return sum(map(lambda number: 1 if number in winning_numbers else 0,your_numbers))

def part_1():
    total_points = 0

    for line in puzzle_input:
        card_wins = calc_wins(line)
        if card_wins > 0: total_points += 2**(card_wins - 1)

    print("Part 1: ",total_points)

def part_2():
    inputs = len(puzzle_input)
    card_copies = [1]*inputs
    total_cards = 0

    for game_index,line in enumerate(puzzle_input):
        for i in range(calc_wins(line)):
            if i < inputs: card_copies[game_index+i+1] += card_copies[game_index]

    print("Part 2: ",sum(card_copies))

if __name__ == "__main__":
    part_1()
    part_2()
