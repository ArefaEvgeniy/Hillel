def summa(a, b):
    try:
        return a + b
    except TypeError:
        print('Not supported type')
    except Exception:
        print('Somathing ia wrong')
    return None


def minus(a, b):
    return a - b
