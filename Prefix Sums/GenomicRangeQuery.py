def solution(S, P, Q):
    seen = []
    result = []

    for type in S:
        if type == 'A':
            seen.append([1, 0, 0, 0])
        elif type == 'C':
            seen.append([0, 1, 0, 0])
        elif type == 'G':
            seen.append([0, 0, 1, 0])
        elif type == 'T':
            seen.append([0, 0, 0, 1])

    for i in range(len(seen)):
        if i == len(seen) - 1:
            break
        else:
            for j in range(4):
                seen[i + 1][j] += seen [i][j]

    seen.insert(0, [0, 0, 0, 0])
    
    for idx in range(len(P)):
        temp = []

        for j in range(4):
            temp.append(seen[Q[idx] + 1][j] - seen[P[idx]][j])

        if temp[0] != 0:
            result.append(1)
        elif temp[1] != 0:
            result.append(2)
        elif temp[2] != 0:
            result.append(3)
        elif temp[3] != 0:
            result.append(4)

    return result

    # hint: record their occurance and prefix their sum and substract