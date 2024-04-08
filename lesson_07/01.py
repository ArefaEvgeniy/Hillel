def area(b, h):
    return b * h / 2


area_2 = lambda b, h: b * h / 2

print(area(3, 4))
print((lambda b, h: b * h / 2)(3, 5))
print(area_2(3, 4))
