# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

nums = []
folds = []
for d in data:
    if d == "":
        continue
    if "fold along" in d:
        fold = d.split("fold along ")[1]
        letter, num = fold.split("=")
        folds.append((letter, int(num)))
    else:
        x, y = d.split(",")
        nums.append((int(x), int(y)))

max_x = max([n[0] for n in nums]) + 1
max_y = max([n[1] for n in nums]) + 1

grid = [[0] * max_x for _ in range(max_y)]

for n in nums:
    x, y = n
    grid[y][x] = 1  # Flip x, y

for f in folds:
    axis, index = f
    if axis == "y":
        temp_grid = grid.copy()[:index]
    if axis == "x":
        temp_grid = [l[:index] for l in grid.copy()]

    temp_nums = []
    for n in nums:
        x, y = n
        if axis == "y" and y >= index:
            x, y = x, index - (y - index)
            temp_grid[y][x] += 1

        if axis == "x" and x >= index:
            x, y = index - (x - index), y
            temp_grid[y][x] += 1
        temp_nums.append((x, y))

    grid = temp_grid
    nums = temp_nums


acc = 0
s = ""
for l in grid:
    for n in l:
        if n > 0:
            s += "#"
            acc += 1
        else:
            s += "."
    s += "\n"

print("\nAnswer 1:", acc)

print("Answer 2:")
print(s)
