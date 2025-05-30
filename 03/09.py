a = 101

if a == 0:
    c = 100
elif a > 100:
    c = 1000
else:
    c = - 100

print("c_1:", c)

c = 100 if a == 0 else (1000 if a > 100 else -100)
print("c_2:", c)


def sum_1():
    ...


def sum_2():
    ...


sum_1() if a == 0 else sum_2()
