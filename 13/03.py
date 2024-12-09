try:
    a = 10
    b = [1, 0, 3]
    print('start')

    # c = a / b[5]
    print('more')
    print(a / b[1])
except (ValueError, TypeError):
    c = ' '
except IndexError:
    c = None
except ZeroDivisionError:
    c = 0
except LookupError:
    c = -1
except SyntaxError:
    c = 100
except Exception as err:
    print(err)
    c = 1

print(c)

print('end')
