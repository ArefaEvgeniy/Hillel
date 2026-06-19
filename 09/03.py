# def my_func(a, b, data):
# def my_func(a: (int, float, str), b: str, data: frozenset) -> int:
def my_func(a: (int, float, str), b: int, data: list) -> list:
    a = int(a)
    b += 1
    new_data = []
    for item in data:
        new_data.append(item * 2 + a - b)
    return new_data


numbers = [1, 2, 3, 4, 5]
print(my_func(3, 5, numbers))
print(my_func.__annotations__)
