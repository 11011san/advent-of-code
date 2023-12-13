import re

input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")
output = 0

mem={}
def locations(spring_map, spring_numbers, middle):
    global mem
    key = f"{spring_map}|{spring_numbers}|{middle}"
    if key not in mem:
        mem[key] = locations_comput(spring_map, spring_numbers, middle)
    return mem[key]

def locations_comput(spring_map, spring_numbers, middle):
    if len(spring_numbers) == 0:
        if re.search(r"(#)", spring_map):
            return 0
        else:
            return 1
    if len(spring_map) == 0:
        return 0
    if middle and spring_map[0] == ".":
        return 0
    temp = spring_numbers.copy()
    if spring_map[0] == "#":
        temp[0] -= 1
        if temp[0] == 0:
            if len(spring_map) >= 2:
                if spring_map[1] == "#":
                    return 0
                else:
                    return locations(spring_map[2:], temp[1:], False)
            else:
                if len(spring_numbers) == 1:
                    if re.search(r"(#)", spring_map[1:]):
                        return 0
                    else:
                        return 1
                else:
                    return 0

        else:
            return locations(spring_map[1:], temp, True)
    if spring_map[0] == "?":
        temp[0] -= 1
        if temp[0] == 0:
            if len(spring_map) >= 2:
                if spring_map[1] == "#":
                    if middle:
                        return 0
                    else:
                        return locations(spring_map[1:], spring_numbers, False)
                else:
                    if middle:
                        return locations(spring_map[2:], temp[1:], False)
                    else:
                        return locations(spring_map[2:], temp[1:], False) + locations(
                            spring_map[1:], spring_numbers, False)
            else:
                if len(spring_numbers) == 1:
                    if re.search(r"(#)",spring_map[1:]):
                        return 0
                    else:
                        return 1
                else:
                    return 0
        else:
            if middle:
                return locations(spring_map[1:], temp, True)
            else:
                return locations(spring_map[1:], temp, True) + locations(
                    spring_map[1:], spring_numbers, False)
    else:
        if middle:
            return 0
        else:
            return locations(spring_map[1:], spring_numbers, False)


for row in input:
    spring_map_org, spring_numbers_org = row.split(" ")
    spring_numbers_org = [int(x) for x in spring_numbers_org.split(",")]

    spring_map = spring_map_org
    spring_numbers = spring_numbers_org.copy()
    for i in range(0, 4):
        spring_map += "?"+spring_map_org
        spring_numbers += spring_numbers_org
    t = locations(spring_map, spring_numbers, False)
    mem = {}
    print(t)
    output += t

print(output)
