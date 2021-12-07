# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

data = [int(d) for d in data[0].split(",")]
print(data)
print("Part 1")

acc = 0
ans = []

for i in range(max(data)):
    acc = 0
    for d in data:
        acc += abs(i-d)
    ans.append(acc)


print("Answer 1:", min(ans))


print("\n\nPart 2")

acc = 0
ans = []


def move_to(d, i):
    cost = 0
    mult = 1
    for i in range(abs(d-i)):
        cost += mult
        mult += 1

    return cost


for i in range(max(data)):
    acc = 0
    for d in data:
        acc += move_to(d, i)
    ans.append(acc)


print("Answer 2:", min(ans))
