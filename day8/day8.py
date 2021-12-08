with open('input.txt') as f:
    input = list(map(lambda x: x.replace('\n',''),f.readlines()))

for i in range(len(input)):
    input[i] = input[i].split(' | ')

for i in input:
    i[0] = i[0].split(' ')
    i[1] = i[1].split(' ')

def solution(input):
    sum = 0
    for i in input:
        for j in i[1]:
            if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
                sum += 1
    sum2 = 0
    for i in input:
        segments = ['' for i in range(10)]
        sevenSegments = [0 for i in range(7)]
        ###STEP 1###
        for j in i[0]:
            if len(j) == 2:
                segments[1] = j
            elif len(j) == 3:
                segments[7] = j
            elif len(j) == 4:
                segments[4] = j
            elif len(j) == 7:
                segments[8] = j
        ###STEP 2###
        for x in segments[7]:
            if x not in segments[1]:
                sevenSegments[0] = x
        for x in segments[4]:
            inAll = True
            for j in i[0]:
                if len(j) == 5:
                    if inAll == False:
                        pass
                    elif x in j:
                        inAll = True
                    else:
                        inAll = False
            if inAll == True:
                sevenSegments[3] = x
                for z in segments[4]:
                    if z not in segments[1] and z != x:
                        sevenSegments[1]=z
                break
        for j in i[0]:
            if len(j) == 5:
                for x in j:
                    if x not in sevenSegments:
                        inAll = True
                        for z in i[0]:
                            if len(z) == 5:
                                if inAll == False:
                                    pass
                                elif x in z:
                                    inAll = True
                                else:
                                    inAll = False
                        if inAll == True:
                            sevenSegments[6] = x
                            break
                break
        for j in i[0]:
            inAll = True
            if len(j) == 5:
                for x in segments[1]:
                    if inAll == False:
                        pass
                    elif x in j:
                        inAll = True
                    else:
                        inAll = False
                if inAll == True:
                    segments[3] = j
                    break
        for j in i[0]:
            if len(j) == 5:
                if sevenSegments[1] in j:
                    segments[5] = j
                    for x in segments[1]:
                        if x in j:
                            sevenSegments[5] = x
        for j in i[0]:
            if len(j) == 5:
                if j not in segments:
                    segments[2] = j
                    for x in segments[1]:
                        if x in j:
                            sevenSegments[2] = x
        for x in segments[8]:
            if x not in sevenSegments:
                sevenSegments[4] = x
        segments[0] = sevenSegments[0] + sevenSegments[1] +sevenSegments[2] +sevenSegments[4] +sevenSegments[5] +sevenSegments[6]
        segments[6] = sevenSegments[0] + sevenSegments[1] +sevenSegments[3] +sevenSegments[4] +sevenSegments[5] +sevenSegments[6]
        segments[9] = sevenSegments[0] + sevenSegments[1] +sevenSegments[2] +sevenSegments[3] +sevenSegments[5] +sevenSegments[6]
        nums = ""
        for j in i[1]:
            for x in range(len(segments)):
                if len(j) == len(segments[x]):
                    inAll = False
                    for z in j:
                        if z in segments[x]:
                            inAll = True
                        else:
                            inAll = False
                            break
                    if inAll == True:
                        nums += str(x)
                        break
        sum2 += int(nums)
    return sum, sum2

print("part 1: ",solution(input)[0])
print("part 2: ",solution(input)[1])
