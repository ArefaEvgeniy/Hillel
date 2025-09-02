a = 200

if a < 0:
    res = "negative"
    print("a is negative")

if a < -100:
    a = a + 20
    print("a < -100")

if a > 100:
    a = a - 20
    print("a > 100")

if a == 0:
    print("a == 0")
else:
    res = "non-negative"
    print("a is non-negative")
    a = a + 40

print('a:', a)
