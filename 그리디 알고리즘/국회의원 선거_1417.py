N = int(input())
N_num = int(input())
cadidate_num_list = []
for _ in range(N-1):
  cadidate_num_list.append(int(input()))
count = 0

while N > 1:
  max_p = max(cadidate_num_list)
  if N_num <= max_p:
    cadidate_num_list[cadidate_num_list.index(max_p)] -=1
    N_num += 1
    count +=1
  else:
    break
print(count)