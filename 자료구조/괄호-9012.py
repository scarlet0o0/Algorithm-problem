n = int(input())

for _ in range(n):
    arr = list(input())
    stack1 = []
    for i in arr:
        if i == '(':
            stack1.append(i)
        elif i == ')':
            if not stack1:
                stack1.append(i)
                break
            else:
                stack1.pop()
    if stack1: 
        print('NO')
    else:
        print('YES')
        



