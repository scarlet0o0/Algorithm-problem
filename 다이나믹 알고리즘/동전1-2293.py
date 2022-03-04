n,k = map(int,input().split())

arr = []
for _ in range(n):
    num=int(input())
    if k >= num:
        arr.append(num)

arr.sort()
arr1 = [0]*k
for i in range(len(arr)):
    coin = arr[i]
    arr2 = [0]*k
    for j in range(0,k):
        if i >0 :
            if (j+1) == coin:
                arr2[j] += arr1[j]+1
            elif (j+1) > coin:
                arr2[j] +=arr1[j] + arr2[j-coin]
            else:
                arr2[j] +=arr1[j]
        else:
            if (j+1) % coin == 0: 
                arr2[j] =1
    arr1 = arr2

print(arr1[k-1])
        
         
            
        