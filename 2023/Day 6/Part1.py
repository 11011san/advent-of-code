import math
import re

input = """Time:      7  15   30
Distance:  9  40  200"""

input = input.split("\n")
with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

time = [int(i) for i in re.findall(r"(\d+)", input[0])]
distance = [int(i) for i in re.findall(r"(\d+)", input[1])]
output = 1
for race in range(0, len(time)):
    wins = 0
    for hold in range(0, time[race]):
        if ((time[race] - hold) * hold) > distance[race]:
            wins += 1
    output *= wins

print(output)
