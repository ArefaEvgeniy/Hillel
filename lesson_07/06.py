def func(name: str, age: int = 12) -> str:
    """
    DFge eg nek fle
    d gkndklsfdgn bkdlsn f
    d dglkngklns lsd fngls;ms dnkvd sl
    dghndskadfvblf;dmfnb
    """
    print('Hello,', name)
    print('Age:', age)
    return f'Hello, {name}'


func('Tom', 70)
print(func.__annotations__)
print(func.__doc__)
