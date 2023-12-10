import re
from colorama import Fore, Back, Style
import sys

sys.setrecursionlimit(20000)
# input = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""
# input = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""
input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L--7F-J|.
.|...||..|.
.L---JL--J.
..........."""

input = input.split("\n")

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

posX = 0
posY = 0
steps = -1
for i, row in enumerate(input):
    found = re.search(r"(S)", row)
    if found:
        posY = i
        posX = found.start(1)
        break
print(f"start at Y={posY}, X={posX}, {input[posY][posX]}")


def change(X, Y):
    global posX
    global prePosX
    global posY
    global prePosY
    global positions
    positions.append((posX, posY))
    prePosX = posX
    posX += X
    prePosY = posY
    posY += Y
    assert input[posY][posX] == "S" or (posX, posY) not in positions, f"in loop at {posX},{posY}"


maxX = len(input[0])
maxY = len(input)


def fina_area(x, y, side):
    if (x, y) in positions:
        return
    global maxX
    global maxY
    if not (0 <= x < maxX) or not (0 <= y < maxY):
        return
    global left_area
    global right_area
    if side == "L":
        area = left_area
        not_area = right_area
    else:
        area = right_area
        not_area = left_area
    if (x, y) in not_area:
        assert False, f"This is not working x={x}, y={y}"
    if (x, y) in area:
        return
    area.append((x, y))
    input[y] = input[y][:x] + ("I" if side == "R" else "O") + input[y][x + 1:]
    fina_area(x, y + 1, side)
    fina_area(x, y - 1, side)
    fina_area(x + 1, y, side)
    fina_area(x - 1, y, side)


prePosX = posX
prePosY = posY
positions = []
positions.append((posX, posY))
while True:
    step = input[posY][posX]
    steps += 1
    # if steps % 100:
    #     print(steps)
    assert steps < 20000, "impossible"
    if step == "S" and steps != 0:
        break
    if step == "S":
        if input[posY + 1][posX] == "|" or input[posY + 1][posX] == "L" or input[posY + 1][posX] == "J":
            posY += 1
            continue
        if input[posY - 1][posX] == "|" or input[posY - 1][posX] == "F" or input[posY - 1][posX] == "7":
            posY -= 1
            continue
        if input[posY][posX + 1] == "-" or input[posY][posX + 1] == "7" or input[posY][posX + 1] == "J":
            posX += 1
            continue
        if input[posY][posX - 1] == "-" or input[posY][posX - 1] == "L" or input[posY][posX - 1] == "F":
            posX -= 1
            continue
        assert "----Cant find a starting pos----"
    if step == "F":
        if posY != prePosY:
            change(1, 0)
        else:
            change(0, 1)
        continue
    if step == "7":
        if posY != prePosY:
            change(-1, 0)
        else:
            change(0, 1)
        continue
    if step == "J":
        if posY != prePosY:
            change(-1, 0)
        else:
            change(0, -1)
        continue
    if step == "L":
        if posY != prePosY:
            change(1, 0)
        else:
            change(0, -1)
        continue
    if step == "-":
        if posX < prePosX:
            change(-1, 0)
        else:
            change(1, 0)
        continue
    if step == "|":
        if posY < prePosY:
            change(0, -1)
        else:
            change(0, 1)
        continue
    assert False, f"I'm lost from {prePosX}, {prePosY} to {posX}, {posY}"
print(f"midpoint is {steps / 2}")
left_area = []
right_area = []

side = "R"
x = 0
y = 1

for i, pos in enumerate(positions):
    if i == 0:
        continue
    prepos = positions[i - 1]
    if i + 1 < len(positions):
        nextpos = positions[i + 1]
    else:
        nextpos = positions[i]
    if prepos[x] != pos[x]:
        if prepos[x] < pos[x]:  # going left
            fina_area(pos[x], pos[y] - 1, "R")
            fina_area(pos[x], pos[y] + 1, "L")
            if pos[x] + 1 != nextpos[x]:
                if pos[y] < nextpos[y]:  # going down next
                    fina_area(pos[x] + 1, pos[y], "R")
                else:
                    fina_area(pos[x] + 1, pos[y], "L")
        else:  # going right
            fina_area(pos[x], pos[y] - 1, "L")
            fina_area(pos[x], pos[y] + 1, "R")
            if pos[x] + 1 != nextpos[x]:
                if pos[y] < nextpos[y]:  # going down next
                    fina_area(pos[x] + 1, pos[y], "L")
                else:
                    fina_area(pos[x] + 1, pos[y], "R")
    else:
        if prepos[y] < pos[y]:  # going up
            fina_area(pos[x] + 1, pos[y], "R")
            fina_area(pos[x] - 1, pos[y], "L")
            if pos[y] + 1 != nextpos[y]:
                if pos[x] < nextpos[x]:  # going Right next
                    fina_area(pos[x], pos[y] + 1, "L")
                else:
                    fina_area(pos[x], pos[y] + 1, "R")
        else:  # going Down
            fina_area(pos[x] + 1, pos[y], "L")
            fina_area(pos[x] - 1, pos[y], "R")
            if pos[y] + 1 != nextpos[y]:
                if pos[x] < nextpos[x]:  # going Right next
                    fina_area(pos[x], pos[y] + 1, "L")
                else:
                    fina_area(pos[x], pos[y] + 1, "R")

print(f"left = {len(left_area)}, right= {len(right_area)}")
for y, row in enumerate(input):
    for x, char in enumerate(row):
        if char == "S":
            print(Fore.GREEN + char, end="")
            print(Style.RESET_ALL, end="")
        elif (x, y) in positions:
            print(Fore.RED + char, end="")
            print(Style.RESET_ALL, end="")
        elif char == "I":
            print(Back.GREEN + char, end="")
            print(Style.RESET_ALL, end="")
        elif char == "O":
            print(Back.BLUE + char, end="")
            print(Style.RESET_ALL, end="")
        else:
            print(char, end="")
    print("")
# 365 low
# 365
