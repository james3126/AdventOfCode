# Advent of Code - Year 2023 - Day 4
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

def calc_wins(card):
    card = card.split(':')[1].split('|')
    winning_numbers = [x for x in card[0].split()]
    your_numbers    = [x for x in card[1].split()]

    card_wins = 0
    for number in your_numbers:
        if number in winning_numbers:
            card_wins += 1

    return card_wins

def part_1():
    total_points = 0

    for line in puzzle_input:
        card_wins = calc_wins(line)
        total_points += 2**(card_wins - 1) if card_wins > 0 else 0

    print("Part 1: ",total_points)

def part_2():
    card_copies = [1]*len(puzzle_input)
    total_cards = 0

    for game_index,line in enumerate(puzzle_input):
        card_wins = calc_wins(line)

        for i in range(card_wins):
            if i < len(puzzle_input):
                card_copies[game_index+i+1] += card_copies[game_index]

    print("Part 2: ",sum(card_copies))

if __name__ == "__main__":
    part_1()
    part_2()
