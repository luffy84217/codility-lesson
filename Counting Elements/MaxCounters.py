def solution(N, A):
    result = [None]*N
    final_floor = 0
    curr_max = 0

    for counterNum in A:
        if counterNum == N+1:
            final_floor = curr_max
            result = [None]*N
        else:
            if result[counterNum-1] == None:
                result[counterNum-1] = 1
            else:
                result[counterNum-1] += 1
            if curr_max < final_floor+result[counterNum-1]:
                curr_max = final_floor+result[counterNum-1]
    
    for i in range(N):
        if result[i] == None:
            result[i] = 0
        result[i] += final_floor
    
    return result
    
    # def solution(N, A):
    # counter = [0] * N
    
    # for i in A:
    #   if i == N + 1:
    #       counter = [max(counter)] * N
    #   else:
    #       counter[i - 1] += 1
    
    # return counter