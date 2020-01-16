def solution(A):
    origin = set(filter(lambda x: x > 0, A))
    all = set()

    if origin == set():
        return 1
    
    for i in range(1, max(origin) + 1):
        all.add(i)

    return max(origin) + 1 if all == origin  else min(all - origin)

    # Note: Python Set difference method costs lots of time therefore lower the performance