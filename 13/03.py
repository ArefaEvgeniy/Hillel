def my_func(b):
    try:
        a = 100
        print('process')
        c = a / b
        print('continue')
    except IndexError:
        print('INDEX')
        c = 0
    except LookupError:
        print('LookupError')
        c = 100
    # except (ZeroDivisionError, TypeError) as err:
    #     c = 99
    except TypeError:
        c = ""

    print('end function')
    return c


print('START')
try:
    res = my_func(0)
    print('CONTINUE')
except ZeroDivisionError:
    res = 99
print(res)
print('END')
