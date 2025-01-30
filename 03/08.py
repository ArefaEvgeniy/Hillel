a = 50
c_1 = None


if a > 0 or a < 10:
    c_1 = 100
# elif a > 10 and a < 20:
elif 10 < a < 20:
    c_1 = 200
elif a > 20:
    c_1 = 300
else:
    c_1 = 0

print('c_1 =', c_1)
