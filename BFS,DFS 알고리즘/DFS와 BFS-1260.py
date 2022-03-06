from tkinter import N


n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    arr[i].append(j)
    
print(n,m,v)
print(arr)

def dfs(x):
    for i in arr[x]:
        print(i)
        dfs(i)
print(dfs)