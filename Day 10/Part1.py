import re

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
input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

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
    prePosX = posX
    posX += X
    global posY
    global prePosY
    prePosY = posY
    posY += Y
    assert (posX, posY) not in positions, f"in loop at {posX},{posY}"
    positions.append((posX, posY))


prePosX = posX
prePosY = posY
positions = []
while True:
    step = input[posY][posX]
    steps += 1
    if steps % 100:
        print(steps)
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
print(steps / 2)
