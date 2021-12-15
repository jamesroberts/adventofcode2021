from collections import defaultdict
from itertools import zip_longest
from typing import Counter


# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

acc = 0
template = data[0]


pairs = []
for d in data[2:]:
    pairs.append(tuple(d.split(" -> ")))

print("\nAnswer 1:", acc)

pairs_map = {}
for p in pairs:
    pairs_map[p[0]] = p[1]

s = template
for i in range(10):
    temp = ""
    for x in range(len(s) - 1):
        sp = f"{s[x]}{s[x+1]}"

        if sp in pairs_map:
            r = pairs_map[sp]
            if x > 0:
                temp += "".join([r, sp[1]])
            else:
                temp += "".join([sp[0], r, sp[1]])
        else:
            temp += sp
    s = temp

C = Counter(s)
print("Part 1 Answer:", max(C.values()) - min(C.values()))

template = data[0]

pair_count = Counter([x + y for x, y in zip(template, template[1:])])

pairs = {}

for q in data[2:]:
    x, y = q.split(" -> ")
    pairs[x] = y

# Count the pairs
for _ in range(40):
    temp_pair_count = defaultdict(int)
    for p in pair_count:
        r = p[0] + pairs[p]
        temp_pair_count[r] += pair_count[p]
        r1 = pairs[p] + p[1]
        temp_pair_count[r1] += pair_count[p]
    pair_count = temp_pair_count

# Split the pairs into individual letters
p0_counts = defaultdict(int)
p1_counts = defaultdict(int)

letters = set()
for p in pair_count:
    p0, p1 = p
    p0_counts[p0] += pair_count[p]
    p1_counts[p1] += pair_count[p]
    letters.add(p0)
    letters.add(p1)

counts = {}
for letter in letters:
    # Only add the biggest count for each letter
    counts[letter] = max(p0_counts.get(letter, 0), p1_counts.get(letter, 0))


print("Part 2 Answer:", max(counts.values()) - min(counts.values()))