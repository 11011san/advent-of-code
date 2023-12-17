import copy
import re
import heapq

input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


def array_to_string(array):
    result = ""
    for row in array:
        result += "".join(row) + "\n"
    return result[:-1]


def string_to_array(string):
    return [[*x] for x in string.split("\n")]


input = open("input1.txt", "r").read().strip()

have_image = False
image = input
input = string_to_array(input)

mem = {}
output = 0
next = [(-int(input[0][0]), 0, 0, "S", 0, image)]

maxX = len(input[0]) - 1
maxY = len(input) - 1

while next:
    step = heapq.heappop(next)
    x = step[1]
    y = step[2]
    if not (0 <= x <= maxX and 0 <= y <= maxY):
        continue
    strait = step[4] + 1
    direction = step[3]
    score = step[0] + int(input[y][x])

    if have_image:
        image = string_to_array(step[5])
        image[y][x] = direction
        image = array_to_string(image)
    else:
        image = ""

    if x == maxX and y == maxY:
        output = score
        mem[(x, y, direction, strait)] = score
        break

    if (x, y, direction, strait) in mem:
        assert score >= mem[(x, y, direction, strait)]
        continue

    mem[(x, y, direction, strait)] = score

    if strait < 3:
        if direction == "^":
            heapq.heappush(next, (score, x, y - 1, direction, strait, image))
        elif direction == ">":
            heapq.heappush(next, (score, x + 1, y, direction, strait, image))
        elif direction == "v":
            heapq.heappush(next, (score, x, y + 1, direction, strait, image))
        elif direction == "<":
            heapq.heappush(next, (score, x - 1, y, direction, strait, image))

    if direction != "^" and direction != "v":
        heapq.heappush(next, (score, x, y - 1, "^", 0, image))
    if direction != ">" and direction != "<":
        heapq.heappush(next, (score, x + 1, y, ">", 0, image))
    if direction != "v" and direction != "^":
        heapq.heappush(next, (score, x, y + 1, "v", 0, image))
    if direction != "<" and direction != ">":
        heapq.heappush(next, (score, x - 1, y, "<", 0, image))

print(output)

print(image)
