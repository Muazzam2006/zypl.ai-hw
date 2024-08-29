def digit_count_sum(k):
    c, s = 0, 0
    while k:
        s += k % 10
        c += 1
        k //= 10
    print(c, s)

t = 5
while t != 0:
    digit_count_sum(int(input()))
