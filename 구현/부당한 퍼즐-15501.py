n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int,input().split()))
idx1, idx2 = 0, 0
for val in arr2:
    if val == arr1[idx1]:
        break
    idx2 += 1

idx_arr= [1,-1]
i = 0
if n != 1:
    if arr2[(idx2+1)%n] == arr1[idx1+1]:
        i = 0
    elif arr2[(idx2+1)%n] == arr1[-1]:
        i = 1

n1 = n
while n > 0:
    if arr2[idx2%n1] != arr1[idx1]:
        print("bad puzzle")
        break
    idx1 += idx_arr[i]
    idx2 += 1
    n -= 1
else:
    print("good puzzle")



