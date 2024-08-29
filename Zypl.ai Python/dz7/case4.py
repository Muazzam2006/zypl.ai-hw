m = int(input())

if m == 2:
    d = 28
elif m in [4, 6, 9, 11]:
    d = 30
else:
    d = 31

print(d)
