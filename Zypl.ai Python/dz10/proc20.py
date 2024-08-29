import math

def TriangleP(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    p = a + 2 * b
    return p

a1, h1 = float(input().split())
a2, h2 = float(input().split())
a3, h3 = float(input().split())

print(TriangleP(a1, h1))
print(TriangleP(a2, h2))
print(TriangleP(a3, h3))
