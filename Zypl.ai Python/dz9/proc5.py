def rect_ps(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    print(2 * (a + b), a * b)

t = 5
while t != 0:
    rect_ps(*map(float, input().split()))
    t -= 1