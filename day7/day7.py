with open('input.txt') as f:
    input = list(map(int,f.readline().split(',')))

def solution(input, part):
    input = sorted(input)
    if part == "1":
        median = input[int(len(input) / 2)]
        sum = 0
        for i in input:
            sum += abs(i-median)
        return sum

    elif part == "2":
        sum = 0
        for i in input:
            sum += i
        avg= round(sum/len(input))
        sum3 = 10000000000
        for j in range(avg-5,avg+5):
            sum2 = 0
            for i in input:
                dst = abs(i-j)
                for i in range(1,dst+1):
                    sum2 += i
            if sum2 < sum3:
                sum3 = sum2
        return sum3


print(solution(input, "2"))
