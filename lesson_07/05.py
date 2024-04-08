def hello(age: int, name: str | int) -> list[int]:
    """
    This is my first function.
    dsgdfbhfd
    dfs dsffhs lkj srlkd gjn.
    """
    print(f'Hello, {name}')
    return list(range(age))


hello(34, 77)
print(hello.__annotations__)
print(hello.__doc__)
