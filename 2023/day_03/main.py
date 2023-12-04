# Advent of Code - Year 2023 - Day 3

# THIS TASK WAS A FAILURE
# FLAG HAS BEEN RAISED AND TIME HAS BEEN CALLED
# CODE RESULTS IN A NUMBER APPROX -0.3% OUT
# 
# WHOLE METHODOLOGY IS WRONG.
# FUTURE APPROACH IS TO HAVE A CHECK PER CHARACTER WHILE GOING, AND BUILD NUMBERS ON THE FLY.
#
# FOR EXAMPLE, WE COME TO THE NUMBER 3. WE NOW IMMEDIATELY CHECK THE -1,-1 -1,0 {...} 1,1 POSITIONS AND NOTE WHETHER THIS IS A VALID NUMBER FROM HERE
# ONCE WE HIT THE END OF THE RUNNING NUMBER, THEN APPEND TO THE LIST PER BEFORE.
# NO NEED FOR PADDING OUT IN THE +X/-X AND +Y/-Y POSITIONS

with open('input.txt', 'r') as f:
    puzzle_input = f.read()

# Symbols are anything except 0123456789.
# Lazy method is to add 'padding' to each side of the grid. IE, row 1 [....], and row last-1 [.....]
# Side padding too, where every row gets . added to the start and end.

def part_1(puzzle_input):
    non_symbol = ['0','1','2','3','4','5','6','7','8','9','.']

    blank_row = ''.join('.' for i in range(140))
    padded_puzzle_input = f'{blank_row}\n{puzzle_input}\n{blank_row}'

    valid_numbers_list = []

    for line_index,line in enumerate(puzzle_input.split('\n')):
        current_number = ''
        for col_index,character in enumerate(line):
            if character.isnumeric():
                #print(pos,character)
                current_number += character

                # Check around the number in 8 directions. NW, N, NE, E, SE, S, SW, W. We can cheat this by checking rows of 3 (-1, 0, 1) on rows -1, 0 and 1 from current.
                # Ignore a number or '.' if found. Then continue if anything else is found

                # Pad line with additional . at start and finish
                line_before = '.'+padded_puzzle_input.split('\n')[line_index]+'.' # Not line_index-1 as we're handling a padded input
                padded_line = '.'+padded_puzzle_input.split('\n')[line_index+1]+'.'
                line_after  = '.'+padded_puzzle_input.split('\n')[line_index+2]+'.' # As above, +1 to expected

                #print("HERE")
                #print(f'{line_before}\n{padded_line}\n{line_after}')

                # Now we can check the -1, 0, 1 positions of each line. Using +1 to each for padding
                #print(f"\nTEST:") 
                for i in [0,1,2]:

                    #print(line_before)
                    #print(col_index+i)

                    if line_index == 37:
                        print(current_number)
                        print(number_valid)
                        #print(line_before[col_index+i],padded_line[col_index+i],line_after[col_index+i])
                        
                    if (line_before[col_index+i] not in non_symbol) or (padded_line[col_index+i] not in non_symbol) or (line_after[col_index+i] not in non_symbol):
                        #print("Valid")
                        number_valid = True

            else:
                # If a number has been built, then proceed to checking whether it's valid
                if current_number != '':
                            
                    #print(number_valid)
                    if number_valid:
                        print(current_number)
                        valid_numbers_list.append(int(current_number))

                # Finally, reset the number and the validity status
                current_number = ''
                number_valid = False

    answer = sum(valid_numbers_list)
    print(valid_numbers_list)
    print("Part 1: ",answer)

def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1(puzzle_input)
    part_2()
