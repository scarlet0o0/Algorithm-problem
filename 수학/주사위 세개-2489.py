arr = list(map(int,input().split()))

if arr[0] == arr[1] and  arr[1] == arr[2] and arr[0] == arr[1]:
    print(arr[0]*1000+10000)
elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
    if arr[0] == arr[1]:
        print(arr[0]*100+1000)
    if arr[0] == arr[2]:
        print(arr[0]*100+1000)
    if arr[1] == arr[2]:
        print(arr[1]*100+1000)
else:
    print(max(arr)*100)