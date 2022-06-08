from collections import deque
arr = []

n = int(input())
for i in range(n):
    S = input()
    arr_len = int(input())
    arr = input()
    c = 1
    P = True
    if arr_len == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr[1:-1].split(',')))
    for s in S:
        if arr and s == 'R':
            P = not P
        elif s == 'D':
            if P and arr:
                arr.popleft()
            elif not P and arr:
                arr.pop()
            else:
                c = 0
                break
    if c:
        arr = list(arr)
        if P:
            print(str(arr).replace(' ',''))
        else:
            arr.reverse()
            print(str(arr).replace(' ',''))
    else:
        print('error')

