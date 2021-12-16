with open("input.txt") as f:
    input = list(map(lambda x: x.replace('\n',''),f.readlines()))

def solution(input):
    chunk = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<"
    }
    scores = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    score = 0
    input2 = input.copy()
    for line in input:
        chunks = []
        for char in line:
            if char not in chunk:
                chunks.append(char)
            else:
                if chunks[-1] == chunk[char]:
                    chunks.pop()
                else:
                    score += scores[char]
                    input2.remove(line)
                    break
        chunks.clear()

    chunk_2 = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    scores_2 = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    cArray = []
    score_2 = 0
    fin = []
    for line in input2:
        for char in line:
            if char not in chunk:
                chunks.append(char)
            else:
                if chunks[-1] == chunk[char]:
                    chunks.pop()
        for c in range(len(chunks)-1,-1,-1):
            cArray.append(chunk_2[chunks[c]])

        for c in cArray:
            score_2 *= 5
            score_2 += scores_2[c]

        fin.append(score_2)
        score_2 = 0
        chunks.clear()
        cArray.clear()
    fin = sorted(fin)
    fin = fin[len(fin)//2]


    return score, fin

print(solution(input)[0])
print(solution(input)[1])
