N = int(input())
num_list = list(map(int, input().split()))

i = 0
hap = 0
for num in num_list:
  min_num = num
  for index in range(i,N):
    if min_num > num_list[index]:
      num_list[i] = num_list[index]
      num_list[index] = min_num
      min_num = num_list[i]
  hap += min_num*(N-i)
  i +=1

print(hap)