def area(b, h):
    return 0.5 * b * h


area_2 = lambda b, h: 0.5 * b * h

print(area(5, 3))
print((lambda b, h: 0.5 * b * h)(5, 3))
print(area_2(5, 3))
