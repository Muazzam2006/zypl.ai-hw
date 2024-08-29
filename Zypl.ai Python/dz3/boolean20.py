a = int(input())
b = a // 100
c = (a // 10) % 10
d = a % 10
m = b != c and c != d and d != b
print(m)
