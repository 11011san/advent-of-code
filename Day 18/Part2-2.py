import copy
import re
import heapq
import sys

# same as part1-2 just changed the read works

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


def array_to_string(array):
    result = ""
    for row in array:
        result += "".join(row) + "\n"
    return result[:-1]


def string_to_array(string):
    return [[*x] for x in string.split("\n")]


input = open("input1.txt", "r").read().strip()

input = input.split("\n")

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

x, y = (0, 0)
X = []
Y = []
for row in input:
    s = re.findall(r"\(#([0-9,1-f]{6})\)", row)
    d = convert(s[0][5:])
    l = int(s[0][:5], 16)
    if d == "U":
        y -= l
    elif d == "D":
        y += l
    elif d == "R":
        x += l
    elif d == "L":
        x -= l

    X.append(x)
    Y.append(y)

def length(x, y, i, j):
    if x == i:
        return abs(y - j)
    else:
        return abs(x - i)


a = (Y[len(X) - 1] + Y[0]) * (X[len(X) - 1] - X[0])
b = length(X[len(X) - 1], Y[len(X) - 1], X[0], Y[0])

for i in range(0, len(X) - 1):
    a += (Y[i] + Y[i + 1]) * (X[i] - X[i + 1])
    b += length(X[i], Y[i], X[i + 1], Y[i + 1])
a = a // 2

print(f"a={a},b={b},a+0.5*b-1={a+(0.5*b)+1}")

# 952408144115
# 952408144115
