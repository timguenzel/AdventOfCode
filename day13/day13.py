with open('input.txt') as f:
    input = list(map(lambda x: x.replace('\n',''),f.readlines()))
    input = list(map(lambda x: x.split(','), input))

def getMax(input):
    maxX = 0
    maxY = 0
    for line in input:
        if '' in line:
            break
        if int(line[0]) > maxX:
            maxX = int(line[0])
        if int(line[1]) > maxY:
            maxY = int(line[1])
    return maxX, maxY

def drawPaper(paper):
    for line in paper:
        print(''.join(line))
    print("\n")

def solution(input):
    maxX, maxY = getMax(input)
    paper = [['.' for x in range(maxX+1)] for i in range(maxY+1)]
    folds = []
    for line in input:
        if 'fold' in line[0]:
            folds.append(line[0])
        elif '' not in line:
            paper[int(line[1])][int(line[0])] = '#'

    for fold in folds:
        amount = int(fold.split("=")[1])
        if 'x' in fold:
            for line in range(len(paper)):
                for element in range(amount+1, len(paper[line])):
                    if paper[line][element] == "#":
                        paper[line][abs(element-(len(paper[line])-1))] = "#"
                del paper[line][amount:]
        if 'y' in fold:
            for line in range(amount,len(paper)):
                for element in range(len(paper[line])):
                    if paper[line][element] == "#":
                        paper[abs(line-(len(paper)-1))][element] = "#"
            del paper[amount:]

    sum = 0
    for line in paper:
        for element in line:
            if element == "#":
                sum += 1
    drawPaper(paper)
    return sum

print(solution(input))
