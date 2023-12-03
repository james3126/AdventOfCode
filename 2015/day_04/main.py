# Advent of Code - Year 2015 - Day 4
import hashlib
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part_1():
    i = 0
    while True:
        concat = puzzle_input+str(i)
        adventCoin = hashlib.md5(str(concat).encode("utf-8")).hexdigest()

        if adventCoin[:5] == "00000":
            print(i)
            break

        i += 1
    
def part_2():
    i = 0
    while True:
        concat = puzzle_input+str(i)
        adventCoin = hashlib.md5(str(concat).encode("utf-8")).hexdigest()

        if adventCoin[:6] == "000000":
            print(i)
            break

        i += 1

if __name__ == "__main__":
    part_1()
    part_2()
