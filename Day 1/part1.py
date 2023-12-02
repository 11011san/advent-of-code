import re

input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

input_split = input.split("\n")

f = open("input1.txt", "r")

output = 0
for a in f:
    found1 = re.search("^[^\\d]*(\\d)", a)
    found2 = re.search("([\\d])[^\\d]*$", a)
    output += int(str(found1.group(1)) + str(found2.group(1)))

print(output)
