# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

acc = 0

score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

acc = 0
open_list = "({[<"
close_list = ")}]>"

for d in data:
    stack = []
    for c in d:
        if c in open_list:
            stack.append(c)
        else:
            pos = close_list.index(c)
            if open_list[pos] == stack[-1]:
                stack.pop()
            else:
                acc += score_map[c]
                break

print("Part 1")

print("Answer 1:", acc)

print("\n\nPart 2")

score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

acc = 0
open_list = "({[<"
close_list = ")}]>"

incomplete = []

for d in data:
    stack = []
    corrupted = False
    for c in d:
        if c in open_list:
            stack.append(c)
        else:
            pos = close_list.index(c)
            if open_list[pos] == stack[-1]:
                stack.pop()
            else:
                corrupted = True
                break
    if not corrupted:
        incomplete.append(d)

acc = 0

scores = []
for s in incomplete:
    acc = 0
    stack = []
    for c in s:
        if c in open_list:
            pos = open_list.index(c)
            stack.append(close_list[pos])
        elif c == stack[-1]:
            stack.pop()

    for c in reversed(stack):
        acc *= 5
        acc += score_map[c]

    scores.append(acc)

ans = sorted(scores)[len(scores)//2]
print("Answer 2:", ans)
