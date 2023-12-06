# Advent of Code - Year 2023 - Day 3 - Attempt 2
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

def part_1():
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    surrounding_positions = [[-1,1],
                             [0,1],
                             [1,1],
                             [-1,0],
                             [1,0],
                             [-1,-1],
                             [0,-1],
                             [1,-1]]

    valid_numbers_list = []

    # Loop through every row (y)
    for row_index,row in enumerate(puzzle_input):
        # print(row)
        current_number = ''
        valid_number = False

        # Loop through every col (x) on that row
        for col_index,col in enumerate(row):
            
            # If we find a number, then begin to process
            if col in numbers:
                current_number += col
                #print("NUMBER FOUND:",col,"Current number:",current_number)

                for pos in surrounding_positions:
                    #print("Checking:",pos)
                    check_row_pos = row_index+pos[0]
                    check_col_pos = col_index+pos[1]
                    #print("Real Pos:",check_row_pos,check_col_pos)
                    if (check_row_pos >= 0) and (check_col_pos >= 0):
                        #print("Proceeding with check")
                        try:
                            #print(row[row_index+pos[0]][col[col_index+pos[1]]])
                            char_to_check = puzzle_input[check_row_pos][check_col_pos]
                            #print("CHECKING CHAR: ",char_to_check)
                            if (char_to_check not in numbers+['.']):
                                #print("FOUND VALID NUMBER",char_to_check)
                                valid_number = True
                        except IndexError:
                            pass

                # Right-side edge-case (literally) handling
                if col_index+1 >= len(row):
                    if valid_number:
                        # print("Adding edge-case",current_number)
                        valid_numbers_list.append(current_number)
                        valid_number=False
                    current_number = ''
                    
            else:
                #print("valid status:",valid_number)
                if valid_number:
                    #print("Adding",current_number)
                    valid_numbers_list.append(current_number)
                    valid_number=False
                current_number = ''
        
    print("Part 1: ",sum(list(map(int,valid_numbers_list))))
    
def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()  
