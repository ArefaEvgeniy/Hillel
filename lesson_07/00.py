def func(a):
    def func2(c):
        print(c.title())

    print('START')
    func2(a)
    print(a)


def func3(a):
    func2(a)


func('RRRR')
func2('RRRR')