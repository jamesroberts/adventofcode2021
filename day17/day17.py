# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

target = []
c = data[0].split("=")
x = c[1].split(",")[0].split("..")
y = c[2].split("..")
target.append([int(i) for i in x])
target.append([int(i) for i in y])

print("target", target)


def target_area_reached(x, y):
    if x >= min(target[0]) and x <= max(target[0]):
        if y >= min(target[1]) and y <= max(target[1]):
            return True

    return False


max_heights = []

velocities = set()
tx = max(target[0]) + 1
for i in range(-tx, tx):
    for j in range(-tx, tx):
        xv = i
        yv = j
        x, y = 0, 0
        heights = []
        while True:
            x += xv
            y += yv
            yv -= 1
            if xv > 0:
                xv -= 1
            elif xv < 0:
                xv += 1
            else:
                xv = 0
            heights.append(y)
            if target_area_reached(x, y):
                velocities.add((i, j))
                max_heights.append(max(heights))
                break

            if y < min(target[1]):
                break


print("Answer 1:", max(max_heights))
print()
print("Answer 2:", len(velocities))
