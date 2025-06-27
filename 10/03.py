def outer_function():
    def inner_function(y):
        return x + y

    x = 100
    return inner_function


closure = outer_function()
print(closure(5))
