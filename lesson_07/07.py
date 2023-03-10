def hello(name: str = 'Don Joe', age: int = 99) -> str:
    """This is my function"""
    return f'Hello, {name}'


print(hello('Bob', 12))
print(hello())
print(hello.__annotations__)
print(hello.__doc__)
