n = int(input())
m_arr = [list(map(int, list(input()))) for _ in range(n)]
v_arr = [[0]*n for _ in range(n)]

def bfs(x,y,v_arr,m_arr):
    hap = 0
    if v_arr[x][y] == 0 and m_arr[x][y] == 1:
        hap += 1
        v_arr[x][y] = 1
        if x != 0:
            hap += bfs(x - 1, y,v_arr,m_arr)
        if x != n -1:
            hap += bfs(x+1, y,v_arr,m_arr)
        if y != 0:
            hap += bfs(x, y - 1,v_arr,m_arr)
        if y != n-1:
            hap += bfs(x, y+1,v_arr,m_arr)

        return hap
    return 0

val = []
for x in range(n):
    for y in range(n):
         num = bfs(x,y,v_arr,m_arr)
         if num > 0:
             val.append(num)
val.sort()
print(len(val))
for v in val:
    print(v)

