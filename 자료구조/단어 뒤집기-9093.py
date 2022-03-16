n = int(input())
for _ in range(n):
    arr = list(input().split())
    for st in arr:
        print(st[::-1],end=" ")
 