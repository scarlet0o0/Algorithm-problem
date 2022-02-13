n = int(input())

n =1000-n
coin_list = [500,100,50,10,5,1]
count = 0

for num in coin_list:
  count += n//num
  n = n%num
  if n == 0:
    break

print(count)