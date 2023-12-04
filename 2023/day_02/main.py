# Advent of Code - Year 2023 - Day 2
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    avail_cubes = {'red':12,
             'green':13,
             'blue':14}

    possible_games = []

    def check_possible_game(game_id,line):
        line = line.split(':')[1]
        for hand in line.split(';'):
            for color in hand.split(','):
                # print(color)
                # [number, color]
                formatted_color = color[1:].split(' ')
                # print(formatted_color)

                # if number > dic(color)
                # print(formatted_color[0])
                if int(formatted_color[0]) > avail_cubes[formatted_color[1]]:
                    #print("not possible")
                    return False

        return True

    for game_id,line in enumerate(puzzle_input.split('\n'),1):
        #print('game:',game_id)

        if check_possible_game(game_id,line):
            possible_games.append(game_id)

    answer = sum(possible_games)
    print("Part 1: ",answer)

from math import prod
def part_2():
    sum_of_power = 0
    for game_id,line in enumerate(puzzle_input.split('\n'),1):
        #print('game:',game_id)
        print(line)
        
        minimums = {'red':0,
                    'green':0,
                    'blue':0}

        line = line.split(':')[1]
        for hand in line.split(';'):
            for color in hand.split(','):
                # [number, color]
                formatted_color = color[1:].split(' ')
                #print(formatted_color)

                if int(formatted_color[0]) > minimums[formatted_color[1]]:
                    minimums[formatted_color[1]] = int(formatted_color[0])

        print(minimums)

        #print("mins for game: ",minimums)
        power = prod(minimums.values())
        #print(power)
        sum_of_power += power
    
    answer = sum_of_power
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
