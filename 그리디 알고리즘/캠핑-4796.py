camping = []
while True:
  N = list(map(int,input().split()))
  camping.append(N)
  if N[0] == 0 and N[1] == 0 and N[2] == 0:
    break
hap = 0
count = 1
for L, P, V in camping:
  if (L == 0):
    break
  n1 = V // P
  n2 = V % P
  hap = n1 * L
  if n2 < L :
    hap += n2
  else:
    hap += L
  print("Case "+str(count)+":",hap)
  count +=1