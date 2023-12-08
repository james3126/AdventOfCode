# Advent of Code - Year 2023 - Day 7
import re
import collections

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
    card_strengths_list = []

    for game in puzzle_input:
        hand, bet = game.split()

        # Split hand up:
        hand_split = list(hand)
        counter = collections.Counter(hand_split)
        common_list = counter.most_common()
        sorted_hand = ''.join([k*v for k,v in common_list])

        # Calculate points (must be done in OG pull order
        points_list = []
        for card in hand_split:
            # print(card)
            # print(card_points_map[card])
            points_list.append(card_points_map[card])

        # Compare against regexes in decending order
        # print(sorted_hand)

        if re.match(r"^(.)\1{4}",sorted_hand): # Five of a Kind
            hand_type = 0
        elif re.match(r"^(.)\1{3}(?!\1)(.)",sorted_hand): # Four of a kind
            hand_type = 1
        elif re.match(r"^(.)\1{2}(?!\1)(.)\2",sorted_hand): # Full house
            hand_type = 2
        elif re.match(r"^(.)\1{2}(?!\1)(.)(?!\1)(?!\2)(.)",sorted_hand): # Three of a kind
            hand_type = 3
        elif re.match(r"^(.)\1(?!\1)(.)\2(?!\1)(?!\2)(.)",sorted_hand): # Two Pair
            hand_type = 4
        elif re.match(r"^(.)\1(?!\1)(.)(?!\1)(?!\2)(.)(?!\1)(?!\2)(?!\3)(.)",sorted_hand): # One pair
            hand_type = 5
        else: # High Card (r"^(.)(?!\1)(.)(?!\1)(?!\2)(.)(?!\1)(?!\2)(?!\3)(.)(?!\1)(?!\2)(?!\3)(?!\4)(.)")
            hand_type = 6

        card_strengths_list.append((points_list,bet,hand_type))

    # Sort the list by the hand type, and then the hand scoring
    sorted_handpoints_bets_list = sorted(card_strengths_list, key = lambda card_strengths_list: (card_strengths_list[2],card_strengths_list[0]))
    # print(sorted_handpoints_bets_list)

    total_winnings = 0

    for x in range(7):
        for y, handbet_tupple in enumerate(sorted_handpoints_bets_list,1):
            if handbet_tupple[2] == x:
                total_winnings += y*int(handbet_tupple[1])

    print("Part 1: ",total_winnings)

def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
