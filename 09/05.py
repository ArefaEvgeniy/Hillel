def my_func(x, y, z):
    if x < 10:
        res = y + z
    else:
        res = y * z
    return x * res


square = lambda x, y, z: x * (y + z) if x < 10 else x * (y * z)

a = 5
print(square(a, 3, 4))
print(my_func(a, 3, 4))
