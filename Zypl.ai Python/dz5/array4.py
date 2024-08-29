n = int(input())
a = int(input())
d = int(input())

res = []
for i in range(n):
    res.append(a * (d ** i))
print(res)
