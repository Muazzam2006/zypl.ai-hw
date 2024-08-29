n = int(input())
ar = [int(input()) for i in range(n)]

a = [ar[i] for i in range(n-1, -1, -1) if ar[i] % 2 == 0]
c = len(a)

print(a, c)
