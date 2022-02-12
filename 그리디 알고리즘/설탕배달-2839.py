N = int(input())

count = 0
N1 = N// 5 

for num in range(N1,-1,-1):
  NN = N
  count = 0
  NN -= num*5
  count += num
  if NN == 0:
    break
  if NN % 3 == 0:
    count += NN//3
    NN = 0
    break
 

if NN == 0:
  print(count)
else:
  print(-1)