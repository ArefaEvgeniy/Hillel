def apply_operation(operation, data):
    result = []
    for item in data:
        result.append(operation(item))
    return result


def square(x):
    return x ** 2


def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]


squared_numbers = apply_operation(square, numbers)
doubled_numbers = apply_operation(double, numbers)

print(squared_numbers)  # [1, 4, 9, 16, 25]
print(doubled_numbers)   # [2, 4, 6, 8, 10]
