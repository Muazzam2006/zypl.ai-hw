import math
x1 = float(input("Input X1: "))
y1 = float(input("Input Y1: "))
x2 = float(input("Input X2: "))
y2 = float(input("Input Y2: "))
p = pow((x2 - x1), 2) + pow((y2 - y1), 2)
s = math.sqrt(p)
print(f"Distance between points is: {s}")
