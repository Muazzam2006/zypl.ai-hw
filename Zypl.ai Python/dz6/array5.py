n = int(input())
f = [1, 1]

for i in range(2, n):
    a = f[i - 2] + f[i - 1]
    f.append(a)

print(f)
