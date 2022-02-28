N = int(input())
time_list = []
count = 0
for _ in range(N):
  num_list = list(map(int, input().split()))
  time_list.append(num_list)
time_list.sort()
min_li = time_list[0]
count +=1
for i in range(1,len(time_list)):
  if min_li[1] <= time_list[i][0]:
    min_li = time_list[i]
    count +=1
  elif min_li[1] > time_list[i][1]:
    min_li = time_list[i]
    continue

print(count)