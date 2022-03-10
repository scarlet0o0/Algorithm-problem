n = int(input())

#팩토리얼 구하는 함수
def f(n):
    if n <= 1:
        return 1
    return f(n-1)*n

n = str(f(n))
count = 0
for i in range((len(n)-1),-1,-1):
    if n[i] == '0':
        count+=1
    else:
        break

print(count)