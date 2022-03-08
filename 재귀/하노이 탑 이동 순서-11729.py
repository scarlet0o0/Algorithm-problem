n = int(input())

def hanoi_tower1(num):
    if num >1:
        return 2*hanoi_tower1(num-1)+1
    return 1
def hanoi_tower2(n,m,num):
    if num == 1:
        print(n,m)
        return 0
    else:
        hanoi_tower2(n,6-n-m,num-1)
        print(n,m) 
        hanoi_tower2(6-n-m,m,num-1)


print(hanoi_tower1(n))
hanoi_tower2(1,3,n)

    