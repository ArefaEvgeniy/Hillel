def func(a=None):
    if a is None:
        a = []
    a.append(len(a))
    return a


list_1 = [3, 7, 9]
list_1 = func(list_1)
print(list_1)

list_2 = [2, 5]
list_2 = func(list_2)
print(list_2)

list_3 = func()
print(list_3)

list_4 = [1, 1, 1, 1]
list_4 = func(list_4)
print(list_4)

list_5 = func()
print(list_5)

list_6 = func()
print(list_6)
