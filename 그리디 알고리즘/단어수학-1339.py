import sys
input = sys.stdin.readline

N = int(input())
abc_list = []
abc_list_num = [0 for _ in range(10)]
num = 9
hap = 0

for _ in range(N):
  S = input()[:-1]
  for idx,s in enumerate(S):
    if s in abc_list:
      abc_list_num[abc_list.index(s)]+=10**(len(S)-idx-1)
    else:
      abc_list.append(s)
      abc_list_num[abc_list.index(s)]+=10**(len(S)-idx-1)
abc_list_num.sort(reverse = True)

for val in abc_list_num:
  hap+=val*num
  num-=1
print(hap)