m = int(input())
n = int(input())

mt = []
for i in range(m):
    r = [int(input()) for j in range(n)]
    mt.append(r)

k = int(input()) - 1

if 0 <= k < m:
    print(mt[k])
