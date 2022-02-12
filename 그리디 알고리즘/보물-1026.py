N=int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
hap = 0

A_list.sort()
B_list.sort(reverse = True)
for idx in range(N):
  hap+=A_list[idx]*B_list[idx]
print(hap)