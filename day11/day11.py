with open("input.txt") as f:
    input = list(map(lambda x: x.replace("\n",""),f.readlines()))
    input = list(map(lambda x: list(x), input))

def drawBoard(board):
    for line in board:
        print(''.join(line))
    print("")

def getNeighbors(input, pos):
    neighbors = []
    for i in range(pos[0]-1, pos[0]+2):
        for j in range(pos[1]-1, pos[1]+2):
            if i >= 0 and j >= 0 and i < len(input) and j < len(input[i]) and [i,j] != pos:
                neighbors.append([i,j])
    return neighbors

def flash(input, pos):
    neighbors = getNeighbors(input, [pos[0], pos[1]])
    input[pos[0]][pos[1]] = "100"
    for x in neighbors:
        energy = int(input[x[0]][x[1]]) + 1
        input[x[0]][x[1]] = str(energy)
        if int(input[x[0]][x[1]]) > 9 and int(input[x[0]][x[1]]) <100:
            flash(input, [x[0],x[1]])

def countFlashes(input):
    sum = 0
    for line in input:
        for num in line:
            if num == "0":
                sum += 1
    return sum

def solution(input):
    sum = 0
    step = 0
    length = len(input) * len(input[0])
    while True:
        for line in range(len(input)):
            for num in range(len(input[line])):
                    energy = int(input[line][num]) + 1
                    input[line][num] = str(energy)

        for line in range(len(input)):
            for num in range(len(input[line])):
                if int(input[line][num]) > 9 and int(input[line][num]) < 100:
                    flash(input, [line,num])

        for line in range(len(input)):
            for num in range(len(input[line])):
                if int(input[line][num]) > 9:
                    input[line][num] = "0"
        step += 1

        if step <= 100:
            sum += countFlashes(input)
        if countFlashes(input) == 100:
            break
    return sum, step

solution = solution(input)

print(solution[0])
print(solution[1])
