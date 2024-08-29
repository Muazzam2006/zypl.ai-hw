def triangle_ps(a):
    return 3 * a, a * a * 3 ** 0.5 / 4

t = 5
while t != 0:
    n = float(input())
    print(triangle_ps(n))
    t -= 1