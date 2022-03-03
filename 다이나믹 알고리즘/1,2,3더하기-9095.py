n = int(input())
input_arr = [int(input()) for _ in range(n)]
num=max(input_arr)
arr=[0]*(num+1)
arr[1] = 1
arr[2] = 1
arr[3] = 1
for i in range(1,num+1):
  if i > 1:
    arr[i] += arr[i-1]
  if i > 2:
    arr[i] += arr[i-2]
  if i > 3:
    arr[i] += arr[i-3]
for i in input_arr:
  print(arr[i])