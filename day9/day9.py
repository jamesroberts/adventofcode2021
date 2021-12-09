# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

hmap = []
for d in data:
    hmap.append([int(x) for x in d])


def get_local_min(hmap, adj):
    vals = {}
    for p in adj:
        x, y = p
        if x < len(hmap) and y < len(hmap[0]):
            if x >= 0 and y >= 0:
                vals[(x, y)] = hmap[x][y]

    m = (-1, -1), 100
    for k, v in vals.items():
        if v == min(m[1], v):
            m = k, v

    return m


def find_min(hmap):
    mins = []
    for x in range(len(hmap)):
        for y in range(len(hmap[0])):
            adj = [(x, y), (x-1, y), (x, y-1), (x, y+1), (x+1, y)]
            if (x, y) == get_local_min(hmap, adj)[0]:
                mins.append(hmap[x][y])

    return mins


acc = 0
for m in find_min(hmap):
    acc += 1+m

print("Part 1")

print("Answer 1:", acc)


print("\n\n\nPart 2")


def find_min2(hmap):
    mins = []
    for x in range(len(hmap)):
        for y in range(len(hmap[0])):
            adj = [(x, y), (x-1, y), (x, y-1), (x, y+1), (x+1, y)]
            if (x, y) == get_local_min(hmap, adj)[0]:
                mins.append((x, y))

    return mins


def basin_helper(hmap, x, y):
    if x < len(hmap) and y < len(hmap[0]):
        if x >= 0 and y >= 0:
            if hmap[x][y] == 9:
                return 0

            hmap[x][y] = 9
            rec = [
                basin_helper(hmap, x+1, y),
                basin_helper(hmap, x, y+1),
                basin_helper(hmap, x, y-1),
                basin_helper(hmap, x-1, y)
            ]
            return 1 + sum(rec)
        return 0
    return 0


def find_basins(hmap):
    acc = 1
    basins = []
    for b in find_min2(hmap):
        basins.append(basin_helper(hmap, b[0], b[1]))

    for bs in sorted(basins)[-3:]:
        acc *= bs

    return acc


print("Answer 2:", find_basins(hmap))
