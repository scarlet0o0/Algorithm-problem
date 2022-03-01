from itertools import combinations

N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home_arr = [(i+1,j+1) for i, a in enumerate(arr) for j, val in enumerate(a) if val == 1]
chicken_arr = [(i+1,j+1) for i, a in enumerate(arr) for j, val in enumerate(a) if val == 2]

pick_chicken=list(combinations(chicken_arr,M))
result=[0]*len(pick_chicken)

for i in home_arr:
  for j in range(len(pick_chicken)):
    a=100
    for k in pick_chicken[j]:
      temp=abs(i[0]-k[0])+abs(i[1]-k[1])
      a=min(a,temp)
    result[j]+=a

print(min(result))