with open('input.txt') as file:
    input = file.readlines()

for i in range(len(input)):
    input[i] = input[i].replace('\n','')

def part1(input):
    inc = 0
    for i in range(len(input)-1):
        if int(input[i]) < int(input[i+1]):
            inc += 1
    return inc

def part2(input):
    threeList = []
    for i in range(len(input)-2):
        if len(input) - i > 2:
            threeList += [int(input[i]) + int(input[i+1]) + int(input[i+2])]
    return part1(threeList)

print(part2(input))
