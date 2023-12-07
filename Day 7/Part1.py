import collections
import functools
import math
import re

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

input = input.split("\n")

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)


def convert(cards):
    result = []
    for card in cards:
        if card == "T":
            result.append(10)
        elif card == "J":
            result.append(11)
        elif card == "Q":
            result.append(12)
        elif card == "K":
            result.append(13)
        elif card == "A":
            result.append(14)
        else:
            result.append(int(card))
    return result


def compare(hand1, hand2):
    card1 = hand1["cards"]
    dup1 = hand1["type"]
    card2 = hand2["cards"]
    dup2 = hand2["type"]

    if dup1 == dup2:
        for i in range(0, 5):
            if card1[i] == card2[i]:
                continue
            if card1[i] > card2[i]:
                return 1
            else:
                return -1
    if dup1 < dup2:
        return -1
    else:
        return 1


def evaluate_type(cards):
    dups = [0] * 14
    for card in cards:
        dups[card - 1] += 1
    max_pare = max(dups)
    if max_pare == 2:
        found = False
        for f in dups:
            if f == 2:
                if found:
                    return 2
                found = True
        return 1
    elif max_pare == 1:
        return 0
    elif max_pare == 3:
        if 2 in dups:
            return 4
        else:
            return 3
    return max_pare + 1


formatted = []
for row in input:
    split = row.split(" ")
    cards = convert(split[0])
    formatted.append({
        "bid": int(split[1]),
        "cards": cards,
        "type": evaluate_type(cards)
    })
print(formatted)

formatted.sort(key=functools.cmp_to_key(compare))
print(formatted)

output = 0
for index, hand in enumerate(formatted):
    output += (index + 1) * hand["bid"]

print(output)
