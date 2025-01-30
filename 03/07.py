a = 50


if a == 0:
    c_1 = 100
elif a > 0:
    c_1 = 300
else:
    c_1 = 200


c_2 = 100 if a == 0 else (300 if a > 0 else 200)

print('c_1 =', c_1)
print('c_2 =', c_2)
