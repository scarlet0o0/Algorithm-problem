arr = [True for i in range(10001)]

for i in range(1,10001):
    hap = i + sum(map(int,list(str(i))))
    if hap < 10001:
        arr[hap] = False
for idx,val in enumerate(arr):
    if idx == 0:
        continue
    if val:
        print(idx)