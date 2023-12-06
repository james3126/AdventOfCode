# Advent of Code - Year 2023 - Day 6
import math
with open('input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')

def find_shortest_hold_time(max_time,req_distance):
    for time in range(max_time):
        if time*(max_time-time) > req_distance:            
            return time

def part_1():
    time_list = map(int,puzzle_input[0].split()[1:])
    dist_list = map(int,puzzle_input[1].split()[1:])
    time_dist_list = list(zip(time_list,dist_list))
    # print(time_dist_list)
    
    answer = 1
    for pair in time_dist_list:
        time, dist = pair

        shortest = find_shortest_hold_time(time,dist)

        ways_to_win = time-(2*shortest)+1 # +1 due to overlap on the 2*
        answer *= ways_to_win

    print("Part 1: ",answer)

def part_2():
    time = int(''.join(puzzle_input[0].split()[1:]))
    dist = int(''.join(puzzle_input[1].split()[1:]))

    shortest = find_shortest_hold_time(time,dist)

    ways_to_win = time-(2*shortest)+1
    print("Part 2: ",ways_to_win)

if __name__ == "__main__":
    part_1()
    part_2()
