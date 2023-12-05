# Advent of Code - Year 2023 - Day 5
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

# File follows the format of:
# seeds:
# seed-to-soil map:
# soil-to-fertilizer map:
# fertilizer-to-water map:
# water-to-light map:
# light-to-temperature map:
# temperature-to-humidity map:
# humidity-to-location map:

# Each map follows the format of:
# 50 98 2
# 52 50 48
# Where we have:
# destination range start, source range start, range length
# So here we have 50 with a range of 2. (50-51), and 98 with a range of 2. (98-99)
# Line 2 has 52 with a range of 48. (52-99), and 50 with a range of 48. (50-97).
# Line 1 shows that seed 98 fits into (50, range 2), and thus seed 98->soil 50.
# Any SOURCE numbers (seeds in this case) that aren't mapped, match the SAME destination number. IE, seed 10 -> soil 10.

def part_1():
    # Find the LOWEST LOCATION number that corresponds to ANY of the input seed numbers

    # Split up the input
    split_inp = puzzle_input.split('\n\n')
    seeds_inp = split_inp[0].split()[1:]
    seeds_to_soil_map = split_inp[1].split('\n')[1:]
    soil_to_fertilizer_map = split_inp[2].split('\n')[1:]
    fertilizer_to_water_map = split_inp[3].split('\n')[1:]
    water_to_light_map = split_inp[4].split('\n')[1:]
    light_to_temperature_map = split_inp[5].split('\n')[1:]
    temperature_to_humidity_map = split_inp[6].split('\n')[1:]
    humidity_to_location_map = split_inp[7].split('\n')[1:]

    # Function takes a raw row from the text input such as '10 5 2'
    # and then returns a tupple with 2 lists. [0] for the destination, and [1] for the source.
    # Of each sub-list, we have the start and end bounds for the range
    def calc_range_start_fin(map_part):
        destination,source,count = map(int,map_part.split())
        destination_end = destination + (count-1)
        source_end = source + (count-1)

        return ([destination,destination_end],[source,source_end])

    # Convert seeds input to int
    seeds_inp = list(map(int, seeds_inp))

    # print(soil_to_fertilizer_map)
    # print(calc_range_start_fin(seeds_to_soil_map[0]))
    # Save each maps range start and end, for destination and source as a list of tupples:
    # Example index from list: ([3352941879, 3482792380], [1247490906, 1377341407])
    seeds_to_soil_map_ranges           = list(map(calc_range_start_fin, seeds_to_soil_map))
    print(seeds_to_soil_map_ranges)
    soil_to_fertilizer_map_ranges      = list(map(calc_range_start_fin, soil_to_fertilizer_map))
    fertilizer_to_water_map_ranges     = list(map(calc_range_start_fin, fertilizer_to_water_map))
    water_to_light_map_ranges          = list(map(calc_range_start_fin, water_to_light_map))
    light_to_temperature_map_ranges    = list(map(calc_range_start_fin, light_to_temperature_map))
    temperature_to_humidity_map_ranges = list(map(calc_range_start_fin, temperature_to_humidity_map))
    humidity_to_location_map_ranges    = list(map(calc_range_start_fin, humidity_to_location_map))

    # Function to calculate the destination of a given source, calculated against the converted 'map' tupples
    # We check whether the value lies within a given source range. If so, calculate the delta and add to the destination range start
    # From here, we have the destination number.
    def calc_destinations(source_list, current_map):
        destination_list = []
        for value in source_list:
            range_found = False
            for source_range in current_map:
                if value >= source_range[1][0] and value <= source_range[1][1]:
                    print("Found range:",source_range)
                    range_found = True

                    # Calculate delta between seed and source range starting boundary
                    source_delta = value - source_range[1][0]
                    print(source_delta)

                    # Thus calculate the destination number:
                    destination_number = source_delta + source_range[0][0]

                    if not (destination_number >= source_range[0][0]) and (destination_number <= source_range[0][1]):
                        print("PROBLEM")

            if not range_found:
                destination_number = value

            destination_list.append(destination_number)

        print("DESTINATION LIST: ",destination_list)
        return destination_list


    # source_list = seeds_inp # Again, as below
    # current_map = seeds_to_soil_map_ranges# Temporary, to be replaced by function handling
    next_inp = calc_destinations(seeds_inp, seeds_to_soil_map_ranges)
    next_inp = calc_destinations(next_inp, soil_to_fertilizer_map_ranges)
    next_inp = calc_destinations(next_inp, fertilizer_to_water_map_ranges)
    next_inp = calc_destinations(next_inp, water_to_light_map_ranges)
    next_inp = calc_destinations(next_inp, light_to_temperature_map_ranges)
    next_inp = calc_destinations(next_inp, temperature_to_humidity_map_ranges)
    locations_list = calc_destinations(next_inp, humidity_to_location_map_ranges)
    
    print("LOCATIONS:",locations_list)

    answer = min(locations_list)
    print("Part 1: ",answer)

def part_2():
    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
