def outer_function(x):
    def inner_function(y):
        return (x + y) ** z + s

    z = 2
    return inner_function


s = 3
closure = outer_function(10)
result = closure(5)
print(result)  # Вивід: 15
