import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
box = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]
v_arr = [[0]*m for _ in range(n)]
queue = deque()

for i in range(m):
    for j in range(n):
        if box[j][i] == 1:
            queue.append((i, j))
            v_arr[j][i] = 1
count = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
val = 0

while queue:
    num = len(queue)
    for _ in range(num):
        tomato_x, tomato_y = queue.popleft()
        box[tomato_y][tomato_x] = count
        val = count-1
        for i in range(4):
            x, y = (tomato_x + dx[i]), (tomato_y + dy[i])
            if m > x > -1 and n > y > -1:
                if box[y][x] == 0 and v_arr[y][x] == 0:
                    v_arr[y][x] = 1
                    queue.append((x,y))
    count += 1

if any(0 in l for l in box):
    print(-1)
elif val == 0:
    print(0)
else:
    print(val)







