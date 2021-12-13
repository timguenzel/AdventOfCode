with open('input.txt') as f:
    input = list(map(lambda x: x.replace('\n',''), f.readlines()))

def getNeighbours(input, pos):
    neighbours = []
    for i,j in zip([1,-1,0,0],[0,0,1,-1]):
        if pos[0]+i >= 0 and pos[1]+j >= 0 and pos[0]+1 <= len(input)-i and pos[1]+j <= len(input)-j:
            neighbours.append(input[pos[0]+i] [pos[1]+j])
    return neighbours

def getNeighbours2(input,pos,curpos):
    neighbours = []
    for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        if pos[0] + i >= 0 and pos[1] + j >= 0 and pos[0] + 1 <= len(input) - i and pos[1] + j <= len(input) - j:
            if [pos[0]+i, pos[1]+j] == curpos:
                return
            else:
                if input[pos[0] + i][pos[1] + j] == "9":
                    pass
                else:
                    neighbours.append(input[pos[0] + i][pos[1] + j])
                    neighbours.append(getNeighbours2(input, [pos[0]+i, pos[1]+j],pos))
                    return neighbours
    return neighbours

def solution(input):
    lowpoints = []
    lowpointPos = []
    for line in range(len(input)):
        for num in range(len(input[line])):
            neighbours = getNeighbours(input,[line,num])
            smaller = True
            for neighbour in neighbours:
                if input[line][num] < neighbour:
                    pass
                else:
                    smaller = False
                    break
            if smaller:
                lowpoints.append(input[line][num])
                lowpointPos.append([line,num])
    sum = 0
    for lowpoint in lowpoints:
        sum += int(lowpoint)+1
    basins = []
    print(getNeighbours2(input, [lowpointPos[0][0],lowpointPos[0][1]],[lowpointPos[0][0],lowpointPos[0][1]]))

    return sum

print(solution(input))
