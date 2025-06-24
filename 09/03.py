def calculate_area(radius: int | float = 0):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """

    area = bool(radius)
    # area = 3.14 * radius ** 2
    return area


print(calculate_area("55.99"))
print(calculate_area())
print(calculate_area.__annotations__)
