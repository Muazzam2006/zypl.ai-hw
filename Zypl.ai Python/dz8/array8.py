n = int(input())
ar = [int(input()) for i in range(n)]

res = []
for i in ar:
    if i % 2 != 0:
        res.append(i)
c = len(res)

print(res, "count: ", c)
