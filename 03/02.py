a = 0
b = 34
c = 0

if a > 100:
    print("a is greater than 100")
    c = a - 100
    if a > 200:
        print("a is greater than 200")
    elif a > 150:
        print("a is greater than 150")
    elif a == 0:
        print("a is equal to 0")
elif a == 100:
    print("a is equal to 100")
elif a > 50:
    print("a is greater than 50")
elif a > 10 and a <= 50:
    print("a is greater than 10")
else:
    print("a is not greater than 100")
    c = 100 - a
d = True

print("a:", a)
print("c:", c)
print("d:", d)
