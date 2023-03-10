a = [8, 5, 4, 5]


def func(d):
    print('d before:', d)
    d.append(99)
    print('d after:', d)


print('a before:', a)
func(a[:])
print('a after:', a)
