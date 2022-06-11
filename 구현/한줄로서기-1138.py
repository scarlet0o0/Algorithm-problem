n = int(input())
arr = list(map(int, input().split()))
arr1 = [0 for i in range(n)]

for idx, val in enumerate(arr):
    e = 0
    i = 0
    wi = val
    while wi >= i:
        if arr1[i] > 0:
            e += 1
            wi += 1
        i += 1
    arr1[val + e] = idx + 1
for i in arr1:
    print(i, end=' ')