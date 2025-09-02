a = 100

if a < 0:
    res = "negative"
    print("a is negative")
    if a < -100:
        a = a + 20
        print("a < -100")
    a = -a
else:
    res = "non-negative"
    print("a is non-negative")
    if a > 100:
        a = a - 20
        print("a > 100")
    else:
        a = a + 40
print('a:', a)
