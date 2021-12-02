# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip().split())

x, y = 0, 0
aim = 0
for d in data:
    if d[0] == "forward":
        x += int(d[1])
        y += a*int(d[1])
    elif d[0] == "up":
        aim -= int(d[1])
    elif d[0] == "down":
        aim += int(d[1])


print("Answer: ", x*y)
