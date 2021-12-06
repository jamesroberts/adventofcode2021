from collections import Counter

# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

ages = [int(d) for d in data[0].split(",")]
new_ages = ages.copy()

print("Part 1")
for _ in range(80):
    for i in range(len(new_ages)):
        new_ages[i] -= 1
        if new_ages[i] == -1:
            new_ages.append(8)
            new_ages[i] = 6

print("Answer 1:", len(new_ages))
assert len(new_ages) == 374927

print("Part 2")
age_counts = Counter(ages)
for _ in range(256):
    temp_counts = Counter()
    for age, numfish in age_counts.items():
        if age == 0:
            temp_counts[6] += numfish
            temp_counts[8] += numfish
        else:
            temp_counts[age-1] += numfish
    age_counts = temp_counts

print("Answer 2:", sum(age_counts.values()))
