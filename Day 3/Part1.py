import re

input = """467....114
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
n=11
input = [input[i:i+n] for i in range(0, len(input), n)]
with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

output = 0
for index, row in enumerate(input):
    found = re.finditer(r"(\d+)", row)
    for number in found:
        done = False
        for i in range(index - 1, index + 2):
            if i == -1 or i == len(input):
                continue
            for j in range(number.start(1) - 1, number.end(1) + 1):
                if j == -1 or j == len(row):
                    continue
                test = input[i][j]
                symbol = re.findall(r"([^\d.\s])", test)
                if symbol:
                    output += int(number.group())
                    done = True
                    break
            if done:
                break

print(output)
