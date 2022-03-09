h,m = map(int,input().split())

h -=1 if m < 45 else 0
m =60-(45-m) if m < 45 else m-45
h =23 if h == -1 else h
print(h,m)

