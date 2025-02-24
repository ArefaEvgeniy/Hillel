def add_numbers(my_list: list, x: int, y: int = 0) -> str:
    my_list.pop()
    return str(x + y)


print(add_numbers([1, 2, 3], 12, 45))
print(add_numbers.__annotations__)
