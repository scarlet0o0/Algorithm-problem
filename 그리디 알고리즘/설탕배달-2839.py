N = int(input())

count = 0
N1 = N// 5 

#5로 나눈 값이 가장 큰걸 찾는다
for num in range(N1,-1,-1):
  val = N
  count = 0
  val -= num*5
  count += num
  if val == 0:
    break
  if val % 3 == 0:
    count += val//3
    val = 0
    break
 
# 5로 나눈 나머지가 3으로 나누어 지는지 확인
if val == 0:
  print(count)
else:
  print(-1)
