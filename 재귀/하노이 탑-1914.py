n = int(input())
arr = []


def h(s, m, e, n):
    if n == 1:

        print(str(s) + " " + str(e))
        return
    h(s, e, m, n-1)

    print(str(s) + " " + str(e))
    h(m, s, e, n-1)

print(2**n-1)
if n <=20:
    h(1,2,3,n)


