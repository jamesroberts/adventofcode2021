# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(int(line.strip()))

# Part 1
times_increased = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        times_increased += 1

print("Part 1: ", times_increased)

# Part 2
times_increased = 0
triples = []
for i in range(len(data)+1-3):
    triples.append(sum(data[i:i+3]))

for i in range(1, len(triples)):
    if triples[i] > triples[i-1]:
        times_increased += 1

print("Part 2: ", times_increased)
