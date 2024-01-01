import math
import re

input = """Time:      7  15   30
Distance:  9  40  200"""

input = input.split("\n")
with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

time = int(input[0].split(":")[1].replace(" ", ""))
distance = int(input[1].split(":")[1].replace(" ", ""))
wins = 0
for hold in range(0, time):
    if ((time - hold) * hold) > distance:
        wins += 1

print(wins)
