def power234(a):
    return a ** 2, a ** 3, a ** 4

t = 5
while t != 0:
    n = int(input())
    print(power234(n))
    t -= 1
