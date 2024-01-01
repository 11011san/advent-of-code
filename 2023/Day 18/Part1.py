import copy
import re
import heapq
import sys

# Works on small gives pic

input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

sys.setrecursionlimit(1300000)

def array_to_string(array):
    result = ""
    for row in array:
        result += "".join(row) + "\n"
    return result[:-1]


def string_to_array(string):
    return [[*x] for x in string.split("\n")]


input = open("input1.txt", "r").read().strip()

input = input.split("\n")

x, y = (0, 0)
X = []
Y = []
for row in input:
    s = row.split(" ")
    d = s[0]
    l = int(s[1])
    for i in range(0, l):
        if d == "U":
            y -= 1
        elif d == "D":
            y += 1
        elif d == "R":
            x += 1
        elif d == "L":
            x -= 1

        X.append(x)
        Y.append(y)

maxX = max(X)
minX = min(X)
maxY = max(Y)
minY = min(Y)

lenX = maxX - minX + 1
lenY = maxY - minY + 1
image = [["." for x in range(0, lenX)] for y in range(0, lenY)]

output = 0

for i in range(0, len(X)):
    image[Y[i] - minY][X[i] - minX] = "#"


def fill(x, y):
    global image
    if not (0 <= x < lenX and 0 <= y < lenY):
        return
    if image[y][x] == "#":
        return
    image[y][x] = "#"
    fill(x + 1, y)
    fill(x - 1, y)
    fill(x, y + 1)
    fill(x, y - 1)


for y, row in enumerate(image):
    found = False
    for x, char in enumerate(row):
        if char == '#' and not found:
            found = True
        elif char == '#' and found:
            break
        elif found:
            fill(x, y)


for y, row in enumerate(image):
    for x, char in enumerate(row):
        if char == "#":
            output += 1

print(array_to_string(image))
print(output)
