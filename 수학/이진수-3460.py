t = int(input())
arr = [int(input()) for i in range(t)]

for val in arr:
    for idx, num in enumerate(reversed(bin(val))):
        if num == '1':
            print(str(idx), end=' ')
    print()
