def add_numbers(x: int, y: int, z: str = '') -> None:
    """
    Add two numbers.
    :param x: First number.
    :param y: Second number.
    :param z: A string to print.
    :return: None.
    """
    print(z, end=" ")
    print(x + y)
    return x + y


a = 23.88
if isinstance(a, (int, float)):
    print("a is an integer")
else:
    print("a is not an integer")
add_numbers("23", "45", "The sum is:")
add_numbers(1, 2)
