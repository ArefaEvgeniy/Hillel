def my_func():
    try:
        a = 10
        b = [0, 5]
        print('start function')

        c = a / b
        print('more')
    except ZeroDivisionError:
        c = 0
    else:
        print('ELSE')
    finally:
        print('finally')

    print('end function')

    return c


print('start')

try:
    rez = my_func()
except TypeError:
    rez = 'wrong'

print('rez:', rez)
print('end')
