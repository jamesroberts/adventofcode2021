# input_file = "test.txt"
input_file = "input.txt"


data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip().split(" -> "))

print("Part 1")
m = 0
points = []
for d in data:
    start, end = [p.split(",") for p in d]
    start = [int(p) for p in start]
    end = [int(p) for p in end]
    m = max([m, max(start), max(end)])
    points.append((start, end))

m += 1
grid = [[0]*m for _ in range(m)]

for p in points:
    start, end = p
    sx, ex = min(start[0], end[0]), max(start[0], end[0])
    sy, ey = min(start[1], end[1]), max(start[1], end[1])
    if start[0] == end[0] or start[1] == end[1]:
        for x in range(sx, ex+1):
            for y in range(sy, ey+1):
                grid[y][x] += 1

total = 0
for l in grid:
    for n in l:
        if n >= 2:
            total += 1

print("Answer 1:", total)


print("\nPart 2")
grid = [[0]*m for _ in range(m)]

for p in points:
    start, end = p
    sx, ex = min(start[0], end[0]), max(start[0], end[0])
    sy, ey = min(start[1], end[1]), max(start[1], end[1])
    if start[0] == end[0] or start[1] == end[1]:
        for x in range(sx, ex+1):
            for y in range(sy, ey+1):
                grid[y][x] += 1
    else:
        x, y = start
        grid[y][x] += 1
        while x != end[0] and y != end[1]:
            if end[0] > start[0]:
                x += 1
            else:
                x -= 1
            if end[1] > start[1]:
                y += 1
            else:
                y -= 1
            grid[y][x] += 1

total = 0
for l in grid:
    for n in l:
        if n >= 2:
            total += 1

print("Answer 2:", total)
