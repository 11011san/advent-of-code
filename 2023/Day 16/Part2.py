import sys

input = open("input1.txt", "r").read().strip()

sys.setrecursionlimit(13000)
input = input.split("\n")

mem = {}
output = 0


def add_move(x, y, direction):
    if direction == "N":
        move(x, y - 1, "N")
    elif direction == "E":
        move(x + 1, y, "E")
    elif direction == "S":
        move(x, y + 1, "S")
    elif direction == "W":
        move(x - 1, y, "W")


def move(x, y, direction):
    if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input):
        return
    global mem
    if (x, y) not in mem:
        mem[(x, y)] = []
    if direction in mem[(x, y)]:
        return
    mem[(x, y)].append(direction)
    char = input[y][x]
    if char == ".":
        add_move(x, y, direction)
    elif char == "\\":
        if direction == "N":
            add_move(x, y, "W")
        elif direction == "E":
            add_move(x, y, "S")
        elif direction == "S":
            add_move(x, y, "E")
        elif direction == "W":
            add_move(x, y, "N")
    elif char == "/":
        if direction == "N":
            add_move(x, y, "E")
        elif direction == "E":
            add_move(x, y, "N")
        elif direction == "S":
            add_move(x, y, "W")
        elif direction == "W":
            add_move(x, y, "S")
    elif char == "-":
        if direction == "N":
            mem[(x, y)].append("S")
            add_move(x, y, "W")
            add_move(x, y, "E")
        elif direction == "E":
            add_move(x, y, "E")
        elif direction == "S":
            mem[(x, y)].append("N")
            add_move(x, y, "W")
            add_move(x, y, "E")
        elif direction == "W":
            add_move(x, y, "W")
    elif char == "|":
        if direction == "N":
            add_move(x, y, "N")
        elif direction == "E":
            mem[(x, y)].append("W")
            add_move(x, y, "N")
            add_move(x, y, "S")
        elif direction == "S":
            add_move(x, y, "S")
        elif direction == "W":
            mem[(x, y)].append("E")
            add_move(x, y, "N")
            add_move(x, y, "S")


for x in range(0, len(input[0])):
    for y in range(0, len(input)):
        if (y != 0 and y != len(input) - 1) and (x != 0 and x != len(input[0]) - 1):
            continue
        if x == 0:
            move(x, y, "E")
            if len(mem) > output:
                output = len(mem)
            mem = {}
        if x == len(input[0]) - 1:
            move(x, y, "W")
            if len(mem) > output:
                output = len(mem)
            mem = {}
        if y == 0:
            move(x, y, "S")
            if len(mem) > output:
                output = len(mem)
            mem = {}
        if y == len(input) - 1:
            move(x, y, "N")
            if len(mem) > output:
                output = len(mem)
            mem = {}

print(output)
