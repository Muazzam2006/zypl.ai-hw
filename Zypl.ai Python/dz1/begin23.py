a = float(input("Input A: "))
b = float(input("Input B: "))
c = float(input("Input C: "))

d = b
b = a
a = c
c = d

print(f"A: {-a},  B: {-b},  C: {-c}")
