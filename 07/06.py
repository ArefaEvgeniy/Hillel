def func(a=1, b=100):
    c = (a - b) / a * b
    return c


a = 10
b = 15
z = func(a=b, b=a)

print(func(10, 15))

print(func(98, 10))

print(func(10, 15))

print(func(b=10))

print(func(10))

print(func())

print(z + 2)
