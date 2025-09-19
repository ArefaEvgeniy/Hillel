def func(a, b, d=30, c=40):
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)
    print('---' * 10)


a = 1
b = 10
c = 33
func(b, 15, 55, a)
func(b, 15, 55)
func(100, 200)
func(100, 200, 300)
func(100, 200, 300, 400)


def func():
    a = 10
    b = 20
    c = 30
    d = 40
