def func():
    a = 12
    b = 33
    c = 0

    try:
        print('func START')
        print((a + b) / c)
        print('CONTINUE')
    except TypeError:
        if ((type(a) == str and a.isdigit() and type(b) == int) or
                (type(a) == int and type(b) == str and b.isdigit())):
            print(int(a) + int(b))
        else:
            print(str(a) + str(b))
    # except ZeroDivisionError:
    #     print('Не можна ділити на нуль')

    print('func END')


print('START')
try:
    func()
except ZeroDivisionError:
    print('Не можна ділити на нуль 2')
print('END')
