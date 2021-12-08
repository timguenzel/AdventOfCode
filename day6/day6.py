with open('input2.txt') as file:
    input = list(map(int,file.readline().split(',')))

def fishes(input, days: int):
    fishes = [0] * 9
    for i in input:
        fishes[i] += 1

    for i in range(days):
        fishes.append(fishes.pop(0))
        fishes[6] += fishes[8]

    return sum(fishes)



print(fishes(input,16))
