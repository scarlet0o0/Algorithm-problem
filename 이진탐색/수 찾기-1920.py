import sys

n = int(input())
arr1 = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

for i in arr2:
    if i in arr1:
        print(1)
    else:
        print(0)
