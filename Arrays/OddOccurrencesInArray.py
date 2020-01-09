def solution(A):
    dic = {}

    for value in A:
        dic.setdefault(str(value), 0)
        dic[str(value)] = dic[str(value)] + 1
    for key, count in dic.items():
        if count == 1:
        return key

# note: record every integer in array and count