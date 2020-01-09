import re

def solution(A):
    arr = []
    for s in str('{0:b}'.format(A)).replace('1', '#1#').split('1'):
        match = re.match(r'^#0+#$', s)
        if match:
            arr.append(s)
    if len(arr) == 0:
        return 0
    else:
        return len(sorted(arr)[-1]) - 2
        
# Tips: replace 1 with #1# to split