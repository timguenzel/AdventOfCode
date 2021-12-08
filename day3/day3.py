with open('input.txt') as file:
    input = file.readlines()

for i in range(len(input)):
    input[i] = input[i].replace('\n','')

def part1(input):
    length = len(input[0])
    index = 0
    gamma,epsilon = "",""

    while index < length:
        ones = 0
        for line in input:
            if line[index] == "1":
                ones += 1

        if ones > len(input)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        index += 1

    return int(gamma, 2) * int(epsilon, 2)


def part2(input):
    oxygen = input
    co2 = input
    index = 0
    while True:
        ones = 0
        zeroes = 0

        for line in oxygen:
            if line[index] == "1":
                ones += 1
            else:
                zeroes += 1

        oxygen2 = oxygen.copy()
        for line in oxygen:
            if ones > zeroes:
                if line[index] != "1":
                    oxygen2.remove(line)
            elif zeroes > ones:
                if line[index] != "0":
                    oxygen2.remove(line)
            else:
                if line[index] != "1":
                    oxygen2.remove(line)
        oxygen = oxygen2

        index += 1

        if len(oxygen) == 1:
            oxygenBits = oxygen[0]
            break

    index = 0
    while True:
        ones = 0
        zeroes = 0

        for line in co2:
            if line[index] == "1":
                ones += 1
            else:
                zeroes += 1

        co2_2 = co2.copy()
        for line in co2:
            if ones > zeroes:
                if line[index] != "0":
                    co2_2.remove(line)
            elif zeroes > ones:
                if line[index] != "1":
                    co2_2.remove(line)
            else:
                if line[index] != "0":
                    co2_2.remove(line)
        co2 = co2_2

        index += 1
        if len(co2) == 1:
            co2Bits = co2[0]
            break

    return int(oxygenBits, 2) * int(co2Bits, 2)

print(part1(input))
