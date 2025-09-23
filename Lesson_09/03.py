def calculate_area(radius):
    """
    Calculate the area of a circle.
    >>> calculate_area(5)
    78.5
    >>> calculate_area(0)
    0.0
    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    area = 3.14 * radius ** 2
    return area


# calculate_area()
print(calculate_area.__doc__)
