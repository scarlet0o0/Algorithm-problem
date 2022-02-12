N,K=input().split()
N = int(N)
K = int(K)
money= K
coin_list = []
count = 0
for _ in range(N):
  n=int(input())
  coin_list.append(n)

coin_list.sort(reverse = True)
#print(coin_list)

for idx,val in enumerate(coin_list):
  if (money < val):
    pass
  count +=money // val
  money = money % val
  #for coin2 in range(idx,N):
print(count)