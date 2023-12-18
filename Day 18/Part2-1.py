import copy
import re
import heapq
import sys

# same as part1-1 but far to slow with the new read function something doesn't seem to work

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


# input = open("input1.txt", "r").read().strip()

input = input.split("\n")

x, y = (0, 0)
X = []
Y = []


def convert(param):
    if param == "0":
        return "R"
    if param == "1":
        return "D"
    if param == "2":
        return "L"
    if param == "3":
        return "U"
    assert False, "what direction"


print("cord start")
for row in input:
    s = re.findall(r"\(#([0-9,1-f]{6})\)", row)
    d = convert(s[0][5:])
    l = int(s[0][:5], 16)
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

print("cord done")
maxX = max(X)
minX = min(X)
maxY = max(Y)
minY = min(Y)

lenX = maxX - minX + 1
lenY = maxY - minY + 1

C = [[]] * lenY

for i in range(0, len(X)):
    if not C[Y[i]]:
        C[Y[i]] = []
    C[Y[i]].append(X[i])
for row in C:
    row.sort()

output = 0

print("compute")

def direction(x, y):
    global C
    if y == 0:
        return "D"
    elif y == lenY - 1:
        return "U"
    else:
        top = False
        bottom = False
        for cell in C[y - 1]:
            if cell == C[y][x]:
                top = True
                break
            elif cell > C[y][x]:
                break
        for cell in C[y + 1]:
            if cell == C[y][x]:
                bottom = True
                break
            elif cell > C[y][x]:
                break


        if top and bottom:
            return "S"
        elif bottom:
            return "D"
        else:
            return "U"


for y, row in enumerate(C):
    inside = False
    check = False
    for x, char in enumerate(row):
        if x == len(row)-1:
            break
        if row[x+1] == char + 1:
            output += 1
            if not check:
                ds = direction(x, y)
            if ds == "S":
                inside = not inside
            else:
                check = True
        elif check:
            de = direction(x - 1, y)
            if de != ds:
                inside = not inside
            check = False
            if inside:
                output += C[y][x+1]-char
                inside = not inside
        elif inside:
            output += row[x+1]-char
            inside = not inside

print(output)

# 952408144115
# 2582198