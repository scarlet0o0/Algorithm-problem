INF = -1
n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]
dfs_arr = [0]*(n+1)
for _ in range(m):
    i,j = map(int,input().split())
    arr[i].append(j)
for i in range(n+1):
    arr[i].append(INF)

print(n,m,v)
print(arr)

def dfs(x):
    for i in arr[x]:
        if dfs_arr[i] == 0 and i != INF:
            dfs_arr[i] = 1
            print(i)
            dfs(i)
        else:
            break 
print(v)
dfs(v)

bfs_q = []
bfs_arr = [0]*(n+1)
def bfs(x):
    for i in arr[x]:
        if bfs_arr[i] == i != INF:
            bfs_q.append(i)
        
        
        