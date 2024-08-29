a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))
k = 0
c = 0
if a > 0:
    k += 1
else:
    c += 1
if b > 0:
    k += 1
else:
    c += 1
if c > 0:
    k += 1
else:
    c += 1
print(f"Amount of positives is: k,  Amount of negatives is c")
