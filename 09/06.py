def my_square(x):
    return x**2


def square_tri_1(h, c):
    return 0.5 * h * c


square = lambda x: x**2
square_tri_2 = lambda h, c: 0.5 * h * c

print(my_square(101))
print(square(101))
