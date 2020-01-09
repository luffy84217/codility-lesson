def solution(A, K):
    for i in range(K):
        A.insert(0, A.pop())
    return A

# note: given input array might be empty