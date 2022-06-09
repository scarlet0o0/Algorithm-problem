from collections import deque

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
apple_num = int(input())
for i in range(apple_num):
    y, x = map(int,input().split(' '))
    arr[y-1][x-1] = 2
k = int(input())
time_d = deque()
for i in range(k):
    t, q = input().split(' ')
    time_d.append([int(t), q])

timd_count = 0
x_arr = [1,0,-1,0]
y_arr = [0,-1,0,1]
wi = 0
p_x,p_y = 0,0
d_r = deque()
d_r.append([p_x, p_y])
while timd_count < 10000:
    if time_d and time_d[0][0] == timd_count:
        if time_d[0][1] == 'D':
            wi -= 1
            if wi < 0:
                wi = 3
        elif time_d[0][1] == 'L':
            wi += 1
            if wi > 3:
                wi = 0
        time_d.popleft()
    #print(wi)
    p_x, p_y = p_x+x_arr[wi], p_y+y_arr[wi]
    d_r.append([p_y, p_x])
    if p_x > n-1 or p_x < 0 or p_y > n-1 or p_y < 0:
        break
    if arr[p_y][p_x] ==1:
        break
    if arr[p_y][p_x] == 2:
        arr[p_y][p_x] = 1
    else:
        r_wi = d_r.popleft()
        arr[r_wi[0]][r_wi[1]] = 0
        if arr[p_y][p_x] == 1:
            break
        else:
            arr[p_y][p_x] = 1
    timd_count += 1
    # print(timd_count)
    # for i in arr:
    #     print(i)
    # print()
print(timd_count+1)








