def solution(X, A):
    leaves = set([])

    for time in range(len(A)):
        leaves.add(A[time])
        if len(leaves) == X:
            return time
    
    return -1

    # Hint: try set to solute
    # Note: line 10 I tried difference method to check but it's O(len(s))