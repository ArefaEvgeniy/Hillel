def summa(a, b):
    try:
        return a + b
    except TypeError:
        print('Not supported type')
    except Exception:
        print('Something wrong')


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
