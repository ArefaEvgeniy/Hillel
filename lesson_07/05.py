def func(a):
    print('a before:', a)
    a.append(0)
    a.append(1)
    print('a after:', a)


d = [5, 6, 7, 8]
print('d before func:', d)
func(d[:])
print('d after func:', d)
