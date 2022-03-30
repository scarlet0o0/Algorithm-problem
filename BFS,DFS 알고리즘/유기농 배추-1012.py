import sys
sys.setrecursionlimit(10**8)

t = int(sys.stdin.readline().rstrip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, v_arr, map_arr):
    if len(map_arr) > x >= 0 and len(map_arr[0]) > y >= 0:
        if v_arr[x][y] == 0 and map_arr[x][y] == 1:
            v_arr[x][y] = 1
            for i in range(4):
                bfs(x+dx[i], y+dy[i], v_arr, map_arr)
            return True
    return False

for __ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0]*n for _ in range(m)]
    v_arr = [[0]*n for _ in range(m)]
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        arr[x][y] = 1

    for i in range(m):
        for j in range(n):
            if bfs(i, j, v_arr, arr):
                count += 1
    print(count)










