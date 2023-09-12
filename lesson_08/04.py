def my_func(world):
    return world + "!"


# print(my_func)

dima = my_func

print(dima('RRR'))

del my_func

print(dima('RRR'))
