import re

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input_split = input.split("\n")

f = open("input1.txt", "r")

result = 0

for a in f:
    game = int(re.search(r"Game (\d+):", a).group(1))
    # 12 red, 13 green, 14 blue
    red = re.findall(r"(\d+) red", a)
    green = re.findall(r"(\d+) green", a)
    blue = re.findall(r"(\d+) blue", a)
    b = False
    if (len([*filter(lambda x: int(x) > 12, red)]) == 0 and
            len([*filter(lambda x: int(x) > 13, green)]) == 0 and
            len([*filter(lambda x: int(x) > 14, blue)]) == 0):
        b = True
        result += game
    print(f"game:{game} pass:{b} red:{red}, green:{green}, blue:{blue}")

print(result)
