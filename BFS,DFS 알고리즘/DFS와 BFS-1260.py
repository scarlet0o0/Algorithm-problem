n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]
dfs_arr = [0]*(n+1)
for _ in range(m):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)
for i in range(n+1):
     arr[i].sort()

def dfs(start,v_arr,arr):
    if v_arr[start] != 1:
        print(start,end=" ")
        v_arr[start] = 1
        for i in arr[start]:
            dfs(i,v_arr,arr)

bfs_q = []
bfs_arr = [0]*(n+1)
def bfs(start,v_arr,arr):
    bfs_q.append(start)
    while bfs_q:
        num=bfs_q.pop(0)
        if v_arr[num] != 1:
            print(num,end=" ")
            v_arr[num] = 1
            for i in arr[num]:
                bfs_q.append(i)

dfs(v,dfs_arr,arr)
print()
bfs(v,bfs_arr,arr)
        
        
        