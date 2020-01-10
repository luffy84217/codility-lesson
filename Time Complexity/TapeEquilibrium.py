def solution(A):
    total = sum(A)
    min_diff = 0

    for i in range(len(A)):
        total = total - 2 * A[i]
        diff = abs(total)
        if i == 0:
            min_diff = diff
        elif diff < min_diff:
            min_diff = diff

    return min_diff

    # Hint: see this question as a seesaw problem
    #       P as fulcrum, while P gets greater, some forces move to another side
    #       origin side remove force and another side add force
    #       therefore, diff decreases 2 times force