import re

input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")


stars = []
start_width = [0] * len(input[0])
start_height = [0] * len(input)
for y, row in enumerate(input):  # find start before expansion
    for star in re.finditer(r"(#)", row):
        stars.append([star.start(1), y])
        start_width[star.start(1)] += 1
        start_height[y] += 1

x = 0
y = 1
expand = 10**6-1
for i in range(len(start_width) - 1, -1, -1):  # expand in width
    if start_width[i] == 0:
        for star in stars:
            if star[x] > i:
                star[x] += 1*expand
for i in range(len(start_height) - 1, -1, -1):  # expand in height
    if start_height[i] == 0:
        for star in stars:
            if star[y] > i:
                star[y] += 1*expand

output = 0
for i, star1 in enumerate(stars): # pare and compute distends
    for star2 in stars[i:]:
        output += (abs(star1[x] - star2[x]) + abs(star1[y] - star2[y]))

print(output)
