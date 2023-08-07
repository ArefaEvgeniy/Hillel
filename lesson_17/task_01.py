def summa(a, b=0):
    try:
        return a + b
    except TypeError:
        print('Not supprted type')
    except Exception:
        print('Something wrong')
    return None


def mines(a, b):
    return a - b


# if __name__ == "__main__":
#     import doctest
#     doctest.testfile('1.txt')
