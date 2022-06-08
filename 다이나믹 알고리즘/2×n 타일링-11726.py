n = int(input())
num1 = 0
num2 = 1
for i in range(1,n+1):
    num1,num2 =num2,(num1+num2)%10007
print(num2)