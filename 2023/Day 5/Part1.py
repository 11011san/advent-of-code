import math
import re

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

input = input.split("\n")
with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

seeds = []
section = "seeds"
active = True


def convert(source, destination, row):
    global active
    global seeds
    if not active:
        if re.match(f"{source}-to-{destination} map:", row):
            active = True
        return False
    found = [int(i) for i in re.findall(r"(\d+)", row)]
    if len(found) == 3:
        for seed_e in seeds:
            if found[1] <= seed_e[source] <= found[1] + found[2]:
                seed_e[destination] = found[0] + (seed_e[source] - found[1])
        return False
    else:
        for seed_d in seeds:
            if destination not in seed_d:
                seed_d[destination] = seed_d[source]
        return True


for row in input:
    if section == "seeds":
        if re.match(r"seeds: ", row):
            found = re.findall(r"(\d+)", row)
            for seed in found:
                seeds.append({"seed": int(seed)})
            section = "soil"
            active = False
        continue
    if section == "soil":
        if convert("seed", "soil", row):
            active = False
            section = "fertilizer"
        continue
    if section == "fertilizer":
        if convert("soil", "fertilizer", row):
            active = False
            section = "water"
        continue
    if section == "water":
        if convert("fertilizer", "water", row):
            active = False
            section = "light"
        continue
    if section == "light":
        if convert("water", "light", row):
            active = False
            section = "temperature"
        continue
    if section == "temperature":
        if convert("light", "temperature", row):
            active = False
            section = "humidity"
        continue
    if section == "humidity":
        if convert("temperature", "humidity", row):
            active = False
            section = "location"
        continue
    if section == "location":
        if convert("humidity", "location", row):
            active = False
            section = "done"
        continue
convert("humidity", "location", "")

output = seeds[0]
for seed_o in seeds:
    if output["location"] > seed_o["location"]:
        output = seed_o
print(output)
