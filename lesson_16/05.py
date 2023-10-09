import pdb


def some_function(a_1, b_1, c_1):
    some_list = list()
    for i in range(a_1):
        # pdb.set_trace()
        some_list.append(i * b_1 / c_1)
        c_1 = b_1 * i
        b_1 = c_1 * i
    return some_list


print(some_function(5, 2, 3))
