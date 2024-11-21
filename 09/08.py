input_list = [1, 2, 3, 4, 5, 6]


def fn(x):
    return x * 5


def fx(x):
    # return x - 4
    return x % 2 != 0


print(list(map(fn, input_list)))
print(list(map(lambda x: x*5, input_list)))

print(list(filter(fx, input_list)))

