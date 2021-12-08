with open('input.txt') as file:
    input = file.readlines()

input = "\n".join(input)
input = input.split('\n')
input2 = input.copy()
for line in input:
    if line == '':
        input2.remove(line)
input = input2

def day4(part):
    numbers = input.pop(0).split(',')
    boards = [[] for i in range(len(input) // 5)]
    j = 0
    for i in range(len(input)):
        if i == 0:
            pass
        elif i % 5 == 0:
            j += 1
        boards[j] += [input[i].split(' ')]

    for i in range(len(boards)): #some weird shit to delete empty elements from list
        for j in range(len(boards[i])):
            try:
                while True:
                    boards[i][j].remove('')
            except ValueError:
                pass

    winnerBoards, unmarkedSum = [], 0
    for curNum in numbers:
        for curBoard in range(len(boards)):
            for row in range(len(boards[curBoard])):
                xr = 0
                for cell in range(len(boards[curBoard][row])):
                    xc = 0
                    if curNum == boards[curBoard][row][cell]:
                        boards[curBoard][row][cell] = "x"
                    if boards[curBoard][row][cell] == "x":
                        xr += 1
                    for col in range(len(boards[curBoard][row])):
                        if boards[curBoard][col][cell] == "x":
                            xc += 1
                    if xr == 5 or xc == 5:
                        if part == "part1":
                            for row2 in boards[curBoard]:
                                for num in row2:
                                    if num != 'x':
                                        unmarkedSum += int(num)
                            return unmarkedSum * int(curNum)
                        elif part == "part2":
                            if curBoard not in winnerBoards:
                                if len(winnerBoards) == len(boards) - 1:
                                    for row2 in boards[curBoard]:
                                        for num in row2:
                                            if num != 'x':
                                                unmarkedSum += int(num)
                                    return unmarkedSum * int(curNum)
                                winnerBoards.append(curBoard)
