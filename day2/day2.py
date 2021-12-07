with open('input.txt') as f:
    input = list(map(lambda x: x.replace('\n',''),f.readlines()))

def solution(input):
    pos = [0,0]
    for i in input:
        dir = i.split(' ')[0]
        amount = int(i.split(' ')[1])
        if dir == "forward":
            pos[0] += amount
        elif dir == "up":
            pos[1] -= amount
        else:
            pos[1] += amount
    part1 = pos[0] * pos[1]
    aim = 0
    pos = [0,0]
    for i in input:
        dir = i.split(' ')[0]
        amount = int(i.split(' ')[1])
        if dir == "forward":
            pos[0] += amount
            pos[1] += aim * amount
        elif dir == "up":
            aim -= amount
        else:
            aim += amount
    part2 = pos[0] * pos[1]
    return part1, part2

print(solution(input)[0])
print(solution(input)[1])
