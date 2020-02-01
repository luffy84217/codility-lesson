def solution(A):
    A.sort()

    for i in range(len(A) - 2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
            
    return 0

    # Note: since A is sorted A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q] is certain