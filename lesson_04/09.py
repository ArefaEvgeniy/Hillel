a = 0

if a > 0:
    b = 1
    if a == 0:
        b = -100
    else:
        b = -10000
else:
    if a < 0:
        b = 0
    else:
        b = -1

print(b)


b2 = 1 if a > 0 else -1
print(b)
