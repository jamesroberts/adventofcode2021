# input_file = "test.txt"
input_file = "input.txt"

data = []

with open(input_file, "r") as file:
    for line in file:
        data.append(line.strip())

print("Part 1")
nums = data[0].split(",")

boards = []
board = []
for line in data[2:]:
    if line == "":
        boards.append(board)
        board = []
    else:
        board.append(line.split())

boards.append(board)


def find_sum(board):
    for r in board:
        print(r)
    print()
    sum = 0
    for indx in range(5):
        for jndx in range(5):
            if board[indx][jndx] != "X":
                sum += int(board[indx][jndx])

    return sum


def bingo(board):
    r, c = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    for indx in range(5):
        for jndx in range(5):
            if board[indx][jndx] == "X":
                r[indx] += 1
                c[jndx] += 1
                if r[indx] == 5 or c[jndx] == 5:
                    return True
    return False


def mark_number(board, n):
    for indx in range(5):
        for jndx in range(5):
            if board[indx][jndx] == str(n):
                board[indx][jndx] = "X"


# Part 1
found = False
for n in nums:
    if found:
        break
    for board in boards:
        mark_number(board, n)
        if bingo(board):
            found = True
            sum = find_sum(board)
            ans = int(n)*sum
            print("Answer:", ans)
            break

# Part 2
print("\n\nPart 2")
winning_boards = {i: False for i in range(len(boards))}
for n in nums:
    for i in range(len(boards)):
        board = boards[i]
        if winning_boards[i] is True:
            continue
        mark_number(board, n)
        if bingo(board):
            winning_boards[i] = True
            num_winning_boards = len(list(filter(lambda x: x, winning_boards.values())))
            if num_winning_boards == len(boards):
                sum = find_sum(board)
                ans = int(n)*sum
                print("Answer:", ans)
