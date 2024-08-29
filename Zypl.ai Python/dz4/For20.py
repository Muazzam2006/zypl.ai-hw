a = int(input("Input A: "))
sum_ = 0
f = 1
for i in range(1, a+1):
    f *= i
    sum_ += f
    print(f"{i}: Factorial: {f},  Summa: {sum_}")
