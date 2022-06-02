x, y = input().split(' ')
length = 0
if len(x) == len(y):
    for c1, c2 in zip(x,y):
        if c1 != c2:
            length += 1
else:
    m1 = 0
    for i in range(len(y)-len(x)+1):
        m2 = 0
        for j in range(len(x)):
            if y[i+j] == x[j]:
                m2 += 1
            m1 = max(m1, m2)
    length = len(x)-m1

print(length)
