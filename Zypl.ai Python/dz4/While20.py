n = int(input("Input N: "))
k = False
while n > 0:
    if n % 10 == 2:
        k = True
        break
    else:
        n //= 10

#print(k)
m = [1, 3, 4, 3]
print(m.index(3))
