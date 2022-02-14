L, R = input().split()
c = 0
if(len(R)>len(L)): print(c)
else:
  for n in range(len(L)):
    if int(L[n]) < int(R[n]): break; 
    if L[n] == '8' and R[n] =='8': c+=1
  print(c)