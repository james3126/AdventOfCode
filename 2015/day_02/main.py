# Advent of Code - Year 2015 - Day 2
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

# Formulae for right rectangular prism surface area:
# 2*l*w + 2*w*h + 2*h*l

def part_1():
    total_surface_area = 0
    for present in puzzle_input.split('\n'):
        l,w,h = list(map(int, present.split("x")))

        side_a = l*w
        side_b = w*h
        side_c = h*l

        shortest = side_a
        if side_b < shortest: shortest = side_b
        if side_c < shortest: shortest = side_c

        #print(l,w,h,side_a,side_b,side_c,shortest)
        
        total_surface_area += (2*side_a)+(2*side_b)+(2*side_c)+shortest

    print(f"Total surface area: {total_surface_area}")

def part_2():
    total_ribbon = 0
    for present in puzzle_input.split('\n'):
        l,w,h = list(map(int, present.split("x")))

        side_a = 2*(l+w)
        side_b = 2*(w+h)
        side_c = 2*(h+l)

        smallest_perimeter = side_a
        if side_b < smallest_perimeter: smallest_perimeter = side_b
        if side_c < smallest_perimeter: smallest_perimeter = side_c

        extra = l*w*h

        total_ribbon += smallest_perimeter+extra

    print(f"Total ribbon: {total_ribbon}")

if __name__ == "__main__":
    part_1()
    part_2()
