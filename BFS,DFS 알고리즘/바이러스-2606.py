n = int(input())
v = int(input())
arr = [[] for _ in range(n+1)] 
for _ in range(v):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)

print(n,v,arr)

q = []
v_arr = [0]*(n+1)

def bfs(v_arr,arr):
    count = -1
    q.append(1)
    while q:
        num = q.pop(0)
        if v_arr[num] != 1:
            print(num)
            count += 1
            v_arr[num] = 1
            for i in arr[num]:
                q.append(i)
    return count

print(bfs(v_arr,arr))

