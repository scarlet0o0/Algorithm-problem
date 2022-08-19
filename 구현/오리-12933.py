d = list(input())
arr = [0 for i in range(5)]
dic = {'q':0,'u':1,'a':2,'c':3,'k':4}
n = 0
for ch in d:
    if ch == 'q':
        arr[0] += 1
        if arr[4] >= 1:
            arr[4] -= 1
    elif arr[dic[ch]-1] >= 1:
        arr[dic[ch] - 1] -= 1
        arr[dic[ch]] += 1
    else:
        print(-1)
        break
else:
    if sum(arr[0:4]) >= 1:
        print(-1)
    else:
        print(sum(arr))


