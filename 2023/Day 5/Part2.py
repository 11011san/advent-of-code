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
        map_destination = found[0]
        map_source = found[1]
        map_range = found[2]

        for seed_e in seeds:
            if f"{destination}_start" in seed_e:
                continue
            if (map_source <= seed_e[f"{source}_start"] <= map_source + map_range and
                    map_source <= seed_e[f"{source}_end"] <= map_source + map_range):
                seed_e[f"{destination}_start"] = map_destination + (seed_e[f"{source}_start"] - map_source)
                seed_e[f"{destination}_end"] = map_destination + (seed_e[f"{source}_end"] - map_source)
            elif map_source <= seed_e[f"{source}_start"] <= map_source + map_range:
                diff = (map_source + map_range) - seed_e[f"{source}_start"]
                seed_range = seed_e[f"{source}_end"] - seed_e[f"{source}_start"]
                new_seed = seed_e.copy()
                for key in seed_e.keys():
                    if key.endswith("_start"):
                        seed_e[key] += diff + 1
                for key in new_seed.keys():
                    if key.endswith("_end"):
                        new_seed[key] -= seed_range - diff
                new_seed[f"{destination}_start"] = map_destination + (new_seed[f"{source}_start"] - map_source)
                new_seed[f"{destination}_end"] = map_destination + (new_seed[f"{source}_end"] - map_source)
                seeds.append(new_seed)
            elif map_source <= seed_e[f"{source}_end"] <= map_source + map_range:
                diff = seed_e[f"{source}_end"] - map_source
                seed_range = seed_e[f"{source}_end"] - seed_e[f"{source}_start"]
                new_seed = seed_e.copy()
                for key in seed_e.keys():
                    if key.endswith("_end"):
                        seed_e[key] -= diff
                for key in new_seed.keys():
                    if key.endswith("_start"):
                        new_seed[key] += seed_range - diff
                new_seed[f"{destination}_start"] = map_destination + (new_seed[f"{source}_start"] - map_source)
                new_seed[f"{destination}_end"] = map_destination + (new_seed[f"{source}_end"] - map_source)
                seeds.append(new_seed)
            elif seed_e[f"{source}_start"] <= map_source and seed_e[f"{source}_end"] >= map_source + map_range:
                befor_seed = seed_e.copy()
                after_seed = seed_e.copy()
                for key in befor_seed.keys():
                    if key.endswith("_end"):
                        befor_seed[key] -= seed_e[f"{source}_end"] - map_source +1
                for key in after_seed.keys():
                    if key.endswith("_start"):
                        after_seed[key] += (map_source + map_range) - seed_e[f"{source}_start"] +1
                seeds.append(befor_seed)
                seeds.append(after_seed)
                for key in seed_e.keys():
                    if key.endswith("_start"):
                        seed_e[key] += map_source - seed_e[f"{source}_start"]
                    if key.endswith("_end"):
                        seed_e[key] -= seed_e[f"{source}_end"] - (map_source + map_range)
                seed_e[f"{destination}_start"] = map_destination + (seed_e[f"{source}_start"] - map_source)
                seed_e[f"{destination}_end"] = map_destination + (seed_e[f"{source}_end"] - map_source)

        return False
    else:
        for seed_d in seeds:
            if f"{destination}_start" not in seed_d:
                seed_d[f"{destination}_start"] = seed_d[f"{source}_start"]
                seed_d[f"{destination}_end"] = seed_d[f"{source}_end"]
        return True


for row in input:
    if section == "seeds":
        if re.match(r"seeds: ", row):
            found = re.findall(r"(\d+)", row)
            ranges = []
            first = None
            for a in found:
                if first is None:
                    first = int(a)
                    continue
                seeds.append({"seed_start": first,
                              "seed_end": first + int(a)})
                first = None
            section = "soil"
            print(f"starting {section}")
            active = False
        continue
    if section == "soil":
        if convert("seed", "soil", row):
            active = False
            section = "fertilizer"
            print(f"starting {section}")
        continue
    if section == "fertilizer":
        if convert("soil", "fertilizer", row):
            active = False
            section = "water"
            print(f"starting {section}")
        continue
    if section == "water":
        if convert("fertilizer", "water", row):
            active = False
            section = "light"
            print(f"starting {section}")
        continue
    if section == "light":
        if convert("water", "light", row):
            active = False
            section = "temperature"
            print(f"starting {section}")
        continue
    if section == "temperature":
        if convert("light", "temperature", row):
            active = False
            section = "humidity"
            print(f"starting {section}")
        continue
    if section == "humidity":
        if convert("temperature", "humidity", row):
            active = False
            section = "location"
            print(f"starting {section}")
        continue
    if section == "location":
        if convert("humidity", "location", row):
            active = False
            section = "evaluate"
            print(f"starting {section}")
        continue
convert("humidity", "location", "")
output = seeds[0]
for seed_o in seeds:
    if output["location_start"] > seed_o["location_start"]:
        output = seed_o
print(output)
