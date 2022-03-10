n = int(input())
arr = list(map(int,input().split()))

m = max(arr)
idx = arr.index(m)

for i in range(n):
    arr[i] =arr[i] /m*100

val=sum(arr)/n
print(val)
    
