# Advent of Code - Year 2023 - Day 1
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

# Writing this a bit different as it seems there will be a lot of recursion here

def formatSequenceToList(sequence):
    return list(map(int, sequence.split()))

def findDiffBetweenVals(sequence):
    delta_sequence = []

    # [1,2,3,4]
    #  [1,1,1]
    #   [0,0]

    # Cycle through the sequence (less 1), and take the delta to the value infront of it
    for i in range(len(sequence)-1):
        delta = sequence[i+1]-sequence[i]
        delta_sequence.append(delta)
    
    return delta_sequence

def checkIfSequenceZeros(sequence):
    for num in sequence:
        if num != 0:
            return False

    return True


def findExtrapolatedValue(og_sequence,delta_sequence):
    next_val = 0
    for value in delta_sequence[1:]:
        # print(next_val,'+',value)
        next_val += value

    return og_sequence[-1]+next_val

def part_1():
    running_total = 0
    for sequence in puzzle_input:
        sequence = formatSequenceToList(sequence)
        og_sequence = sequence.copy()
        # print("SEQ:",sequence)

        delta_list = []
        while checkIfSequenceZeros(sequence) != True:
            sequence = findDiffBetweenVals(sequence)
            delta_list.append(sequence[-1])

        # Reverse the delta list:
        delta_list.reverse()

        # print("NEX:",findExtrapolatedValue(og_sequence,delta_list))
        # print("OGS:",og_sequence)
        extrapolated_value = findExtrapolatedValue(og_sequence,delta_list)
        running_total += extrapolated_value
        # print("TOT:,",running_total)

    print("Part 1: ",running_total)

def part_2():
    running_total = 0
    for sequence in puzzle_input:
        sequence = formatSequenceToList(sequence)
        sequence.reverse() # This was easy ...
        og_sequence = sequence.copy()

        delta_list = []
        while checkIfSequenceZeros(sequence) != True:
            sequence = findDiffBetweenVals(sequence)
            delta_list.append(sequence[-1])

        delta_list.reverse()

        extrapolated_value = findExtrapolatedValue(og_sequence,delta_list)
        running_total += extrapolated_value



    print("Part 2: ",running_total)

if __name__ == "__main__":
    part_1()
    part_2()
