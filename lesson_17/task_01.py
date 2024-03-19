def summa(a, b):
    try:
        return a + b if isinstance(a, str) else round(a + b, 3)
    except TypeError:
        print('Not supported type')
    except Exception:
        print('Something wrong')

    return None


def mines(a, b):
    return a - b
