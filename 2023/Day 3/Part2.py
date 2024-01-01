import re

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
664.598..."""
n = 11
input = [input[i:i + n] for i in range(0, len(input), n)]

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)


def part(index):
    if index == 0:
        return input[0:1]
    if index == len(input):
        return input[-2:-1]
    return input[index - 1:index + 2]


output = 0

for index, row in enumerate(input):
    found = re.finditer(r"(\*)", row)
    for symbol in found:
        symbol_start = symbol.start(1)
        symbol_end = symbol.end(1)
        done = False
        first = 0
        for line in part(index):
            for number in re.finditer(r"(\d+)", line):
                number_start = number.start(1)
                number_end = number.end(1)
                if (symbol_start <= number_start <= symbol_end) or (symbol_start <= number_end <= symbol_end) or (
                        number_start < symbol_start and number_end > symbol_end):
                    if first == 0:
                        first = int(number.group())
                    else:
                        print(f"line {index + 1} on row {symbol_end}, {first}*{number.group()}")
                        output += first * int(number.group())
                        done = True
                        break
            if done:
                break
print(output)
