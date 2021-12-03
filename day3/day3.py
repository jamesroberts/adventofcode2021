# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())


# Part 1
bit_len = len(data[0])
g = ""
e = ""

for i in range(bit_len):
    zeros, ones = 0, 0
    for d in data:
        if d[i] == "0":
            zeros += 1
        if d[i] == "1":
            ones += 1

    if zeros > ones:
        g += "0"
        e += "1"
    else:
        g += "1"
        e += "0"

print("Answer 1: ", int(g, 2)*int(e, 2))

# Part 2

ox = data.copy()
co2 = data.copy()
k = 0
while len(ox) > 1:
    for i in range(bit_len):
        zeros, ones = [], []
        if len(ox) == 1:
            continue
        for idx, d in enumerate(ox):
            if d[i+k] == "0":
                zeros.append(d)
            if d[i+k] == "1":
                ones.append(d)

        if len(zeros) > len(ones):
            ox = zeros
        else:
            ox = ones
    k += 1

k = 0
while len(co2) > 1:
    for i in range(bit_len):
        zeros, ones = [], []
        if len(co2) == 1:
            continue
        for idx, d in enumerate(co2):
            if d[i+k] == "0":
                zeros.append(d)
            if d[i+k] == "1":
                ones.append(d)

        if len(zeros) <= len(ones):
            co2 = zeros
        else:
            co2 = ones

    k += 1

print("Answer 2: ", int(ox[0], 2)*(int(co2[0], 2)))
