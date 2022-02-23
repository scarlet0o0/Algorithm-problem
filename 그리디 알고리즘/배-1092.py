import sys
input = sys.stdin.readline

N = int(input()) 
crane_weight_limit = list(map(int, input().split()))
M = int(input())
boxs_weight = list(map(int, input().split()))
count = 0
crane_weight_limit.sort(reverse =True)
boxs_weight.sort(reverse =True)

if max(crane_weight_limit) < max(boxs_weight):
    count = -1
else:
  while min(crane_weight_limit) < min(boxs_weight):
   del crane_weight_limit[-1]
  while len(boxs_weight) > 0:
    for i in range(len(crane_weight_limit)):
      for idx in range(len(boxs_weight)):
        if crane_weight_limit[i] >= boxs_weight[idx]:
          del boxs_weight[idx]
          break
    count +=1
print(count)