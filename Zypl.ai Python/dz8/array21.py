n = int(input())

ar = [int(input()) for i in range(n)]

k = int(input()) - 1
l = int(input()) - 1

if 0 <= k <= l < n:
    s = ar[k:l+1]
    a = sum(s) / len(s)
    print(a)
