def AddRightDigit(D, K):
    k = int(f"{K}{D}")
    return k

K = int(input())
D1 = int(input())
D2 = int(input())

K = AddRightDigit(D1, K)
print(D1, K)

K = AddRightDigit(D2, K)
print(D2, K)
