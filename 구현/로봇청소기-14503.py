N, M = map(int, input().split())
r, c, direction = map(int, input().split())
map_arr = []
for i in range(N):
    map_arr.append(list(map(int, input().split())))

x_arr = [0, 1, 0, -1]
y_arr = [-1, 0, 1, 0]
count = 0
map_arr[c][r] = 2
clean_num = 1
# while True:
#     if count < 4:
#         d = (direction + 3) % 4
#         print(map_arr[c + y_arr[d]][r + x_arr[d]],c ,y_arr[d],d,count)
#         if map_arr[c + y_arr[d]][r + x_arr[d]] == 0:
#             count = 0
#             direction = d
#             r, c = r + x_arr[d], c + y_arr[d]
#             print(r, c)
#             clean_num += 1
#             map_arr[c][r] = clean_num
#         else:
#             direction = d
#             count += 1
#     else:
#         count = 0
#         d = (direction + 2) % 4
#         if map_arr[c + y_arr[d]][r + x_arr[d]] == 1:
#             break
#         else:
#             r, c = r + x_arr[d], c + y_arr[d]
# for i in map_arr:
#     print(i)
# print(clean_num)
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

num = 2
while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = num
                num += 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] != 0: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]