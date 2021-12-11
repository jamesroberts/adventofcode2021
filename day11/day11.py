# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

grid = []
print("Part 1")
acc = 0
for d in data:
    grid.append([int(c) for c in d])


def prop_flash(grid, x, y, flashed):
    global acc
    if x >= 0 and y >= 0:
        if x < len(grid) and y < len(grid[0]):
            if not flashed[x][y]:
                grid[x][y] += 1
            if grid[x][y] > 9 and not flashed[x][y]:
                grid[x][y] = 0
                flashed[x][y] = 1
                acc += 1

                prop_flash(grid, x + 1, y, flashed)
                prop_flash(grid, x - 1, y, flashed)
                prop_flash(grid, x, y + 1, flashed)
                prop_flash(grid, x, y - 1, flashed)
                prop_flash(grid, x + 1, y + 1, flashed)
                prop_flash(grid, x - 1, y - 1, flashed)
                prop_flash(grid, x - 1, y + 1, flashed)
                prop_flash(grid, x + 1, y - 1, flashed)


all_flashed = False
i = 0
while not all_flashed:
    flashed = [[0] * len(grid) for _ in range(len(grid))]
    if sum([sum(l) for l in grid]) == 0:
        print("\n\nPart 2")
        print("Answer 2:", i)
        break
    i += 1
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not flashed[x][y]:
                grid[x][y] += 1
            if grid[x][y] > 9:
                prop_flash(grid, x, y, flashed)

    if i == 100:
        print("Answer 1:", acc)
