import sys
n = int(input())
arr = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s.split()[0] == 'push':
        num = int(s.split()[1])
        arr.append(num)
    elif s == 'pop':
        if not arr:
            print(-1)
        else:
            del_num=arr.pop()
            print(del_num) 
    elif s == 'size':
        print(len(arr))
    elif s == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif s == 'top':
        if not arr:
            print(-1)
        else:
            print(arr[-1])