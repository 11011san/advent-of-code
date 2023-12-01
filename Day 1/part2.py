import re

input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

input_split = input.split("\n")


def convert(value):
    match value:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
    return int(value)


# Correct: 55652

f = open("input2.txt", "r")
output = 0


def findLast(param, a):
    for i in range(len(a),-1,-1):
        found1 = re.findall(param,a[0:i])
        if found1:
            return found1[0]


for a in f:
    found = re.findall(r"(one|two|three|four|five|six|seven|eight|nine|\d)", a)
    b = (convert(found[0]) * 10 + convert(findLast(r"(one|two|three|four|five|six|seven|eight|nine|\d)$", a)))
    #print(str(b) + " - " + a.replace("\n", ""))
    output += b

print(output)
