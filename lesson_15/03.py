a = 10
b = 20
c = [15, 12, None]


print('before')
d = a / (b - c[1] - 5)
print('after')

if d < 10:
    raise TypeError('d має бути більшим за 10')

print(d)
