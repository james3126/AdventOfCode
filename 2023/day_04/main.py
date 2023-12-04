# Advent of Code - Year 2023 - Day 4
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

# Card N: List of winning numbers | List of numbers you have

def part_1():
    # 1 match = 1 point
    # n match = 2^(n-1) for n > 0, else 0

    total_points = 0

    for line in puzzle_input.split('\n'):
        line = line.split(':')[1]
        winning_numbers = [x for x in line.split('|')[0].split(' ') if x != '']
        your_numbers = [x for x in line.split('|')[1].split(' ') if x != '']
        # print(winning_numbers,' | ',your_numbers)

        card_wins = 0
        for number in your_numbers:
            #number = number.strip(' ')

            # print(number)
            if number in winning_numbers:
                card_wins += 1

        total_points += 2**(card_wins - 1) if card_wins > 0 else 0

        # print(winning_numbers)
    
    answer = total_points
    print("Part 1: ",answer)

def part_2():
    # 1st card - 1 match = 1 extra copy of card 2
    # 1st card - n match = 1 extra copy of cards 2->n+1
    # 3rd card - 5 match = 1 extra copy of cards 4->9
    # x card - n match = 1 extra copy of cards x+1->x+n+1

    # Hold the number of card copies for later. This will always start at 1, and increase from there.
    card_copies = [1 for i in range(len(puzzle_input.split('\n')))]

    total_cards = 0

    # Loop through all cards
    for game_index,line in enumerate(puzzle_input.split('\n')):
        # print("\nGame: ",game_index+1,"Copies:",card_copies[game_index])
        line = line.split(':')[1]
        winning_numbers = [x for x in line.split('|')[0].split(' ') if x != '']
        your_numbers = [x for x in line.split('|')[1].split(' ') if x != '']
        # print(winning_numbers,' | ',your_numbers)

        # Check for winning numbers
        card_wins = 0
        for number in your_numbers:

            if number in winning_numbers:
                card_wins += 1

        # print("total wins: ",card_wins)

        # Loop through the wins to add wins onto each of the next games
        for i in range(card_wins):
            # print(f"Adding {card_copies[game_index]} copies to game",game_index+i+1+1) # Extra +1 for readability
            
            # Discard any inputs beyond the end of the games
            if i < len(puzzle_input.split('\n')):
                # print(card_copies[game_index+i+1],'+',card_copies[game_index])
                card_copies[game_index+i+1] += card_copies[game_index]
                # print("=",card_copies[game_index+i+1])

    answer = sum(card_copies)
    # print(card_copies)
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
