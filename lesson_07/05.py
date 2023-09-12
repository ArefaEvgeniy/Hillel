def my_func(a: int, b: int = 10) -> float:
    return int(a / b)


print(my_func(2300))
print(my_func.__annotations__)
