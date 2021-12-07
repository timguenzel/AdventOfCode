with open('input.txt') as file:
    input = file.readlines()

for i in range(len(input)):
    input[i] = input[i].replace('\n','')
    input[i] = input[i].split('->')

for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = input[i][j].split(',')

def solution(input):
    lines = [[0 for i in range(1000)] for i in range(1000)]
    for i in input:
        x = int(i[0][0])
        x2 = int(i[1][0])
        y = int(i[0][1])
        y2 = int(i[1][1])
        if x == x2 and y == y2: pass
        else:
            if y == y2:
                line = abs(x - x2)
                for j in range(line+1):
                    lines[y][min(x,x2) + j] += 1
            elif x==x2:
                line = abs(y - y2)
                for j in range(line+1):
                    lines[min(y, y2) + j][x] += 1
            else:
                if (x<x2 and y<y2) or (x>x2 and y>y2):
                    for u,o in zip(range(min(x,x2),max(x,x2)+1),range(min(y,y2),max(y,y2)+1)):
                        lines[o][u] += 1
                else:
                    for u,o in zip(range(min(x,x2),max(x,x2)+1),range(max(y,y2),min(y,y2)-1,-1)):
                        lines[o][u] += 1

    count = 0
    for i in lines:
        for j in i:
            if j > 1:
                count += 1
    return count



print(solution(input))
