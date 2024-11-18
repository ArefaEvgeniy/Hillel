def example_function(x, y, z):
    print(x, y, z)


def example_function_2(x, y, z, *args):
    print('x:', x)
    print('y:', y)
    print('z:', z)
    print('args:', args)


d = (1, 2, 3)
example_function(*d)
# example_function(1, 2, 3)

a = [1, 2, 3, 55, 23, 667, 8]
s = {1: 'a', 'b': 2, 'c': 'd', 'z': 4}
example_function_2(*a)
example_function_2(*d)
example_function_2(*s)
example_function_2(*s.values())
