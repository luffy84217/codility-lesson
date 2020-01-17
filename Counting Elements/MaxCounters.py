def solution(N, A):
    result = [0] * N
    count = [0] * N
    curr_max = 0
    acc_max = 0
    
    for num in A:
        if num == N + 1:
            acc_max += curr_max
            count = [0] * N
            curr_max = 0
            continue
        count[num - 1] += 1
        curr_max = max(count)

    for i in range(len(result)):
        result[i] = acc_max + count[i]

    return result
    
    # def solution(N, A):
    # counter = [0] * N
    
    # for i in A:
    #   if i == N + 1:
    #       counter = [max(counter)] * N
    #   else:
    #       counter[i - 1] += 1
    
    # return counter