def say_hi(name: str, d: int = 99) -> str:
    """
    Моя функция
    kkjdfkj sdf ds
    sdfgkjdfnkds sd dsf jsd
    dsgbfkjdlsf sd jbndflk dfbfd
    """
    return f'Hello, {str(name)}, {str(d)}'


print(say_hi('Vasia', 44))
print(say_hi.__annotations__)
print(say_hi.__doc__)
