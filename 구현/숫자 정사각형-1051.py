n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]

box_len = max(n, m) - 1
def f(box_len):
    while box_len > -1:
        for i in range(box_len, n):
            for j in range(box_len, m):
                if arr[i-box_len][j-box_len] == arr[i-box_len][j] \
                        and arr[i-box_len][j-box_len] == arr[i][j-box_len] \
                        and arr[i-box_len][j-box_len] == arr[i][j]:
                    return (box_len+1) ** 2
        box_len -= 1
    return -1

print(f(box_len))
