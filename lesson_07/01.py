def area(b, h):
    return 0.5 * b * h


a = 10 * 45 - 666 + area(10, 5)

area_2 = lambda b, h: 0.5 * b * h
a_2 = 10 * 45 - 666 + area_2(10, 5)

print(a)
print(a_2)
