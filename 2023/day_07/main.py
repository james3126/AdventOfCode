# Advent of Code - Year 2023 - Day 7
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

def part_1():
    card_points_map = {'A':13,
                       'K':12,
                       'Q':11,
                       'J':10,
                       'T':9,
                       '9':8,
                       '8':7,
                       '7':6,
                       '6':5,
                       '5':4,
                       '4':3,
                       '3':2,
                       '2':1}

    scoring_hands = ["AAAAA","AABAA","ABBBA","AAABC","AABBC","AABCD","ABCDE"]

    #for hand in puzzle_input:
    #    pass

    hand = puzzle_input[0]
    print(hand)
    hand.sort()
    
    
    
    

    answer = ''
    print("Part 1: ",answer)

def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
