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
    # print(seeds_to_soil_map_ranges)
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
                    # print("Found range:",source_range)
                    range_found = True

                    # Calculate delta between seed and source range starting boundary
                    source_delta = value - source_range[1][0]
                    # print(source_delta)

                    # Thus calculate the destination number:
                    destination_number = source_delta + source_range[0][0]

                    # if not (destination_number >= source_range[0][0]) and (destination_number <= source_range[0][1]):
                    #     print("PROBLEM")

            if not range_found:
                destination_number = value

            destination_list.append(destination_number)

        # print("DESTINATION LIST: ",destination_list)
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
    
    # print("LOCATIONS:",locations_list)

    answer = min(locations_list)
    print("Part 1: ",answer)

def part_2():
    # Find the LOWEST LOCATION number that corresponds to ANY of the input seed numbers
    # In PART2 the seed numbers are provided as a list of start_numbers and values rather than a raw list of values.
    # For example, seeds: 5 2 10 4 is now seeds 5,6,10,11,12,13 rather than just 5,2,10,4

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

    def calc_seed_ranges(seed_list):
        seed_ranges = []
        for i in range(0,len(seed_list),2):
            seed_ranges.append(([seed_list[i],seed_list[i]+seed_list[i+1]]))

        return seed_ranges

    # Convert seeds input to int list, and then to a list containing [start,end] sub-lists
    seeds_inp = list(map(int, seeds_inp))
    seeds_inp_ranges = calc_seed_ranges(seeds_inp) # Contains a list of [start,finish] sub-lists

    # Save each maps range start and end, for destination and source as a list of tupples:
    # Example index from list: ([3352941879, 3482792380], [1247490906, 1377341407])
    seeds_to_soil_map_ranges           = list(map(calc_range_start_fin, seeds_to_soil_map))
    soil_to_fertilizer_map_ranges      = list(map(calc_range_start_fin, soil_to_fertilizer_map))
    fertilizer_to_water_map_ranges     = list(map(calc_range_start_fin, fertilizer_to_water_map))
    water_to_light_map_ranges          = list(map(calc_range_start_fin, water_to_light_map))
    light_to_temperature_map_ranges    = list(map(calc_range_start_fin, light_to_temperature_map))
    temperature_to_humidity_map_ranges = list(map(calc_range_start_fin, temperature_to_humidity_map))
    humidity_to_location_map_ranges    = list(map(calc_range_start_fin, humidity_to_location_map))

    # source_range_to_check is passed as a [start_value, values] list
    # ranges_to_check contains a full map list of ranges using a list of tupples of sub [start_value, values] lists 
    def find_sub_ranges(source_range_to_check,ranges_map):
        valid_ranges = []
        for map_part in ranges_map:
            source_range      = source_range_to_check
            destination_range = map_part[1]
            #print(source_range, destination_range)
            # Logic to find whether any source list fits within a destination list without checking ranges of billions against billions
            # if source_start >= destination_start AND source_start <= destination_end AND source_end <= destination_end AND source_end >= destination_start
            if (source_range[0] >= destination_range[0]) and (source_range[0] <= destination_range[-1]) and (source_range[-1] <= destination_range[-1]) and (source_range[-1] >= destination_range[0]):
                # source_range falls entirely within the list.
                # print("ENTIRELY")

                # Append entire converted range
                start_num = source_range[1]-source_range[0]
                converted_start = destination_range[0]+start_num
                converted_end   = converted_start+start_num

                valid_ranges.append(([converted_start,converted_end]))
            elif (source_range[0] >= destination_range[0]) and (source_range[0] <= destination_range[-1]) and (source_range[-1] > destination_range[-1]):
                # source_range falls within the list, but extends beyond
                print("PARTIALLY, BEYOND")

                excess = [destination_range[-1]+1,source_range[-1]]
                valid_excess_ranges = find_sub_ranges(excess,ranges_map)

                # Default back if nothing found
                if len(valid_excess_ranges) == 0:
                    valid_excess_ranges = excess
                
                valid_ranges.append(([destination_range[0],source_range[-1]],valid_excess_ranges))
            elif (source_range[0] < destination_range[0]) and (source_range[-1] <= destination_range[-1]) and (source_range[-1] >= destination_range[0]):
                # source_range falls within the list, but starts before
                print("PARTIALLY, BEFORE")

                excess = [source_range[1],destination_range[1]-1]
                valid_excess_ranges = find_sub_ranges(excess,ranges_map)

                # Default back if nothing found
                if len(valid_excess_ranges) == 0:
                    valid_excess_ranges = excess
                
                valid_ranges.append(([source_range[1],destination_range[-1]],valid_excess_ranges))
            else:
                # source_range does not fall within the list at all
                # print("NOT AT ALL")
                pass

        # If no valid ranges are found, then the entire range can be passed through as an "as is" input
        # if len(valid_ranges) == 0:
        #     valid_ranges.append(([source_range[0],source_range[1]]))

        return valid_ranges

    valid_soil_ranges = []
    for seed_range in seeds_inp_ranges:
        #print(seed_range)
        valid_soil_ranges.append(find_sub_ranges(seed_range,seeds_to_soil_map_ranges))
        #print(x)

    print(valid_soil_ranges)

    answer = ''
    print("Part 2: ",answer)

if __name__ == "__main__":
    part_1()
    part_2()
