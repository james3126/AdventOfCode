# Advent of Code - Year 2015 - Day 1
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

import time

def part_1():
    good_strings = 0
    bad_strings = ['ab','cd','pq','xy']
    vowels = ['a','e','i','o','u']

    for string in puzzle_input.split('\n'):
        vowel_count = 0
        checks = {'three_vowels':False,
                  '2_same_in_row':False,
                  'no_bad_strings':True}

        for i in range(len(string)-1):
            letters = string[i:i+2]

            #print("string", str(letters))

            if letters[0] == letters[1]:
                checks['2_same_in_row'] = True

            if letters in bad_strings:
                checks['no_bad_strings'] = False

        for letter in string:
            if letter in vowels:
                vowel_count += 1

        if vowel_count >= 3:
            checks['three_vowels'] = True

        #print(checks)
        if (checks['three_vowels'] == True) and (checks['2_same_in_row'] == True) and (checks['no_bad_strings'] == True):
            good_strings += 1
    print(good_strings)

def part_2():
    good_strings = 0

    for string in puzzle_input.split('\n'):
        for letters4

if __name__ == "__main__":
    part_1()
    part_2()
