with open("input2.txt") as f:
    input = ''.join(list(map(lambda x: bin(int(x,16))[2:].zfill(4),f.readline())))

def solution(input,versions,sbpckts = 0, sblength = 0, value = []):
    if input == "" or int(input,2) == 0:
        return versions, value
    print(input)
    version = int(input[:3],2)
    versions.append(version)
    packetID = int(input[3:6],2)
    input = input[6:]
    if packetID == 4:
        while sbpckts > 0:
            for i in range(0,len(input),5):
                if input[i] == "0":
                    sbpckts -= 1
                    print(sbpckts)
                    value.append(int(input[i + 1:5], 2))
                    input = input[i+5:]
                value.append(int(input[i + 1:5], 2))

        while sblength > 0:
            for i in range(0,len(input),5):
                if input[i] == "0":
                    sblength -= (i+5)
                    value.append(int(input[i + 1:5], 2))
                    input = input[i+5:]
                value.append(int(input[i + 1:5], 2))
        solution(input,versions,value=value)
        return versions, value
        '''else:
            for i in range(0,len(input),5):
                if input[i] == "0":
                    input = input[i+5:]
                    value.append(int(input[i + 1:5], 2))
                    solution(input, versions, value=value)
                    return versions, value
                value.append(int(input[i + 1:5], 2))'''
    else:
        if input[0] == "0":
            subLength = int(input[1:16],2)
            input = input[16:]
            values = solution(input, versions, sblength=subLength)[1]
        else:
            subPackets = int(input[1:12],2)
            input = input[12:]
            values = solution(input,versions,sbpckts=subPackets)[1]
        if packetID == 0:
            ans = sum(values)
        elif packetID == 1:
            ans = 1
            for val in values:
                ans *= val
        elif packetID == 2:
            ans = min(values)
        elif packetID == 3:
            ans = max(values)
        elif packetID == 5:
            ans = int(values[0] > values[1])
        elif packetID == 6:
            ans = int(values[0] < values[1])
        elif packetID == 7:
            ans = int(values[0] == values[1])
        values.clear()
        values.append(ans)
        return versions, values

print(solution(input,[])[1])
