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


def locations(spring_map, spring_numbers, middle, org):
    if len(spring_numbers) == 0:
        if re.search(r"(#)", spring_map):
            return 0
        else:
            print(org)
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
                    return locations(spring_map[2:], temp[1:], False, org[:len(org) - len(spring_map)] + "#." + org[
                                                                                                                len(org) - len(
                                                                                                                    spring_map) + 2:])
            else:
                if len(spring_numbers) == 1:
                    if re.search(r"(#)", spring_map[1:]):
                        return 0
                    else:
                        print(org)
                        return 1
                else:
                    return 0

        else:
            return locations(spring_map[1:], temp, True, org)
    if spring_map[0] == "?":
        temp[0] -= 1
        if temp[0] == 0:
            if len(spring_map) >= 2:
                if spring_map[1] == "#":
                    if middle:
                        return 0
                    else:
                        return locations(spring_map[1:], spring_numbers, False,
                                         org[:len(org) - len(spring_map)] + "." + org[len(org) - len(spring_map) + 1:])
                else:
                    if middle:
                        return locations(spring_map[2:], temp[1:], False, org[:len(org) - len(spring_map)] + "#." + org[
                                                                                                                    len(org) - len(
                                                                                                                        spring_map) + 2:])
                    else:
                        return locations(spring_map[2:], temp[1:], False, org[:len(org) - len(spring_map)] + "#." + org[
                                                                                                                    len(org) - len(
                                                                                                                        spring_map) + 2:]) + locations(
                            spring_map[1:], spring_numbers, False,
                            org[:len(org) - len(spring_map)] + "." + org[len(org) - len(spring_map) + 1:])
            else:
                if len(spring_numbers) == 1:
                    if re.search(r"(#)", spring_map[1:]):
                        return 0
                    else:
                        print(org[:len(org) - len(spring_map)] + "#" + org[len(org) - len(spring_map) + 1:])
                        return 1
                else:
                    return 0
        else:
            if middle:
                return locations(spring_map[1:], temp, True,
                                 org[:len(org) - len(spring_map)] + "#" + org[len(org) - len(spring_map) + 1:])
            else:
                return locations(spring_map[1:], temp, True,
                                 org[:len(org) - len(spring_map)] + "#" + org[
                                                                          len(org) - len(spring_map) + 1:]) + locations(
                    spring_map[1:], spring_numbers, False,
                    org[:len(org) - len(spring_map)] + "." + org[len(org) - len(spring_map) + 1:])
    else:
        if middle:
            return 0
        else:
            return locations(spring_map[1:], spring_numbers, False, org)


for row in input:
    spring_map, spring_numbers = row.split(" ")
    spring_numbers = [int(x) for x in spring_numbers.split(",")]
    print(f"{spring_map} {spring_numbers}")
    t = locations(spring_map, spring_numbers, False, spring_map)
    print(t)
    output += t

print(output)
