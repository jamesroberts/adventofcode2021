from collections import Counter


# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

cave_map = {}

for cave in data:
    start, end = cave.split("-")
    if cave_map.get(start):
        cave_map[start].append(end)
    else:
        cave_map[start] = [end]

    if cave_map.get(end):
        cave_map[end].append(start)
    else:
        cave_map[end] = [start]

possible_paths = set()


def find_paths(caves, current_path):
    global possible_paths
    global cave_map
    temp_paths = {current_path}
    for cave in caves:
        if cave == "start":
            continue

        if cave.islower():
            C = Counter(current_path.split(","))
            if any([v for k, v in C.items() if k.islower() and v >= 2]):
                if cave in current_path.split(","):
                    continue

        temp = f"{current_path},{cave}"
        temp_paths.add(temp)

        if cave != "end" and cave_map.get(cave):
            for i in find_paths(cave_map.get(cave), temp):
                temp_paths.add(i)

    return temp_paths


print(cave_map)

result = find_paths(cave_map["start"], "start")
for i in result:
    possible_paths.add(i)

acc = 0
for l in sorted(possible_paths):
    if l.endswith("end"):
        print(l)
        acc += 1


print("\nAnswer", acc)