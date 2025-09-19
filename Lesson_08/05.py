def func(a, b, *args):
    print('a =', a)
    print('b =', b)
    for item in args:
        print(item, end=' ')
    print()
    print('---' * 10)


a = 1
b = 10
c = 33
func(b, 15, 55, a, c, a, a, 0)
func(b, 15, 55)
func(100, 200)
