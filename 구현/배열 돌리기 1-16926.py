import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

while r > 0:
    width, length = m, n
    x, y = 0, 0
    temp = arr[y][x]
    while width != 0 and length != 0:
        temp = arr[y][x]
        for i in range(length-1):
            y += 1
            arr[y][x], temp = temp, arr[y][x]
        for i in range(width-1):
            x += 1
            arr[y][x], temp = temp, arr[y][x]
        for i in range(length-1):
            y -= 1
            arr[y][x], temp = temp, arr[y][x]
        for i in range(width-1):
            x -= 1
            arr[y][x], temp = temp, arr[y][x]
        x, y = x + 1, y+1
        width, length = width-2, length-2
    r -= 1
for i in arr:
    print(' '.join(map(str,i)))





