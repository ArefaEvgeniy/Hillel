a = [1, 2, 4, 0]


def func(b):
    for item in b:
        print(item)
    b.append(99)
    return b


def func_2(d):
    print(d)


b = func(a[:])
print('a:', a)
func_2(b)
