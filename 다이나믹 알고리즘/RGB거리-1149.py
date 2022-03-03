n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
R,G,B = (0,1,2)
min_arr = [[0]*3 for _ in range(n)]

for i in range(1,n):
  arr[i][R] += min(arr[i-1][G],arr[i-1][B] )
  arr[i][G] += min(arr[i-1][R],arr[i-1][B] )
  arr[i][B] += min(arr[i-1][R],arr[i-1][G] )
print(min(arr[n-1][R],arr[n-1][G],arr[n-1][B]))