a = [int(input()) for i in range(10)]

a10 = a[-1]

res = 0
for i in a[:-1]:
    if i < a10:
        res = i
        break

print(res)
