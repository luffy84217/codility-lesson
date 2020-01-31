def solution(A):
    A.sort()
    seen = None
    result = []
    
    for value in A:
        if value == seen:
            continue
        else:
            seen = value
            result.append(value)
    
    return len(result)