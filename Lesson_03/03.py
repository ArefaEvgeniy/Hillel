a = 200

if a < 0:
    res = "negative"
    print("a is negative")
elif a < -100:
    a = a + 20
    print("a < -100")
elif a == 200:
    print("a is 200")
elif a > 100:
    a = a - 20
    print("a > 100")
elif a == 0:
    print("a == 0")
else:
    res = "non-negative"
    print("a is non-negative")
    a = a + 40
print('a:', a)
