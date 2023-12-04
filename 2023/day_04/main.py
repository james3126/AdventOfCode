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
        #winning_numbers = line.split('|')[0].split(' ')
        winning_numbers = [x for x in line.split('|')[0].split(' ') if x != '']
        your_numbers = [x for x in line.split('|')[1].split(' ') if x != '']
        print(winning_numbers,' | ',your_numbers)

        card_wins = 0
        win_num = []
        for number in your_numbers:
            #number = number.strip(' ')

            # print(number)
            if number in winning_numbers:
                card_wins += 1
                win_num.append(number)
        print(card_wins,win_num)
        total_points += 2**(card_wins - 1) if card_wins > 0 else 0

        #print(winning_numbers)
    
    answer = total_points
    print("Part 1: ",answer)

def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
