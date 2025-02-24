def square_1(x, y):
    return x**2 * y[3]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_2 = lambda x, y: x**2 * y[3]
print(square_1(5, a))
print(square_2(5, a))
