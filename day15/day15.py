from functools import lru_cache

# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

grid = []
for l in data:
    grid.append([int(i) for i in l])

BIGNUM = 100000


@lru_cache
def helper(x, y):
    if x >= 0 and y >= 0:
        if x < len(grid) and y < len(grid[0]):
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return grid[x][y]

            return grid[x][y] + min(helper(x + 1, y), helper(x, y + 1))
    return BIGNUM


print("Answer 1:", helper(0, 0) - grid[0][0])

grid = []
for l in data:
    line = [int(i) for i in l]
    lt = l
    for j in range(4):
        temp = [(int(i) + 1) for i in lt]
        temp = [1 if z > 9 else z for z in temp]
        line += temp
        lt = temp
    grid.append(line)

temp_grid = grid.copy()

for x in range(4):
    new_grid = []
    for l in temp_grid:
        temp_line = l
        line = [(int(i) + 1) for i in temp_line]
        line = [1 if z > 9 else z for z in line]
        temp_line = line
        grid.append(line)
        new_grid.append(line)
    temp_grid = new_grid

from heapq import heappop, heappush

path_heap = [(0, 0, 0)]
seen = {}

while True:
    shortest_path, x, y = heappop(path_heap)
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        print("Answer 2:", shortest_path)
        break

    if (x, y) not in seen:
        seen[(x, y)] = 1
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for x, y in neighbours:
            if x >= 0 and y >= 0:
                if x < len(grid) and y < len(grid[0]):
                    if (x, y) not in seen:
                        path_length = grid[x][y] + shortest_path
                        path = (path_length, x, y)
                        heappush(path_heap, path)
