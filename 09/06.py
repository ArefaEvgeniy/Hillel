def my_func(x):
    if x % 2 == 0:
        return int(x ** 2)
    else:
        return int(x ** 0.5)


numbers = [1, 2, 3, 4, 5]
squared_root = map(my_func, numbers)
result = list(squared_root)
print(result)

# my_func_2 = lambda x: int(x ** 2) if x % 2 == 0 else int(x ** 0.5)
squared_root_2 = map(lambda x: int(x ** 2) if x % 2 == 0 else int(x ** 0.5), numbers)
result_2 = list(squared_root_2)
print(result_2)
