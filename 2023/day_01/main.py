# Advent of Code - Year 2023 - Day 1
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    answer_nums = []

    for line in puzzle_input.split('\n'):
        finalNum = ''.join(x for x in line if (x in numbers))
        answer_nums.append(finalNum)

    #print(answer_nums[1:10])

    answer = 0
    for num in answer_nums:
        # We only want the FIRST and LAST digit of each combined number for part 1
        answer += int(f'{num[0]}{num[-1]}')

    print("Part 1: ",answer)

def part_2():
    numbers_convert = {'one':'o1e',
                       'two':'t2o',
                       'three':'t3e',
                       'four':'f4r',
                       'five':'f5e',
                       'six':'s6x',
                       'seven':'s7n',
                       'eight':'e8t',
                       'nine':'n9e'}
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    answer_nums = []

    def replace_text_with_num(text, conv_dic):
        for k, v in conv_dic.items():
            #print(f"Checking for {k} in {text}")
            text = text.replace(k, v)
            #print(f"converted: {text}")
        return text

    for line in puzzle_input.split('\n'):
        #print(line)
        line = replace_text_with_num(line, numbers_convert)
        #print(line)

        finalNum = ''.join(x for x in line if (x in numbers))
        #print(finalNum)

        # We only want the FIRST and LAST digit of each combined number for part 1
        finalDigitPair = f'{finalNum[0]}{finalNum[-1]}'
        #print(finalDigitPair)
        
        answer_nums.append(int(finalDigitPair))

    answer = sum(answer_nums)

    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
