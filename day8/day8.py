from itertools import permutations
from typing import Counter


# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

parsed = []
for d in data:
    s, o = d.split(" | ")
    parsed.append((s, o))

print("Part 1")

acc = 0
out = []
for p in parsed:
    for o in p[1].split(" "):
        out.append(len(o))
C = Counter(out)


acc = 0
for k, v in C.items():
    if str(k) in "2347":
        acc += v

print("Answer 1:", acc)


print("\n\nPart 2")

normal_nums = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
]

acc = 0
for p in parsed:
    for perm in permutations("abcdefg"):
        jumbled_mapping = {a: b for a, b in zip(perm, "abcdefg")}
        jumbled_numbers = []
        for signal in p[0].split(" "):
            key = "".join(sorted(jumbled_mapping[s] for s in signal))
            jumbled_numbers.append(key)
        num = ""
        if set(jumbled_numbers) == set(normal_nums):
            unjumbled = []
            for a in p[1].split(" "):
                translated = ""
                for n in a:
                    translated += jumbled_mapping[n]
                unjumbled.append("".join(sorted(translated)))

            for u in unjumbled:
                num += str(normal_nums.index(u))
            acc += int(num)

print("Answer 2:", acc)
