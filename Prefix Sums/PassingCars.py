def solution(A):
    zeros = 0
    result = 0

    for i in A:
        if i == 0:
            zeros += 1
        else:
            result += zeros

    return -1 if result > 1000000000 else result

    # Note: Although it says the pairs of passing cars are (0, 1), (0, 3), (0, 4), (2, 3), (2, 4)
    # Don't be confused by it. Prefix sums of zeros (1, 0), (3, 0), (3, 2), (4, 0), (4, 2)