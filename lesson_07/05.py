a = [7, 5, 3, 6]


def func(d):
    print('input d:', d)
    d.append(0)
    d.append(99)
    print('new d:', d)


print('a before func:', a)
func(a[:])
print('a after func:', a)
