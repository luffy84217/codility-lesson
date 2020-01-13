def solution(A):
    array = sorted(A)
    
    for i in range(len(A)):
        if i + 1 != array[i]:
            return 0
    return 1

    # Note: sorting time complexity MUST be O(nlogn) or better