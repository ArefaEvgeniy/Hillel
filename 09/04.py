def calculate_area(length: float = 0.0, width: float = 0.0) -> float:
    """
    Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    area = length * width
    return area


res = calculate_area(12, 55)
print(res)

print(calculate_area.__annotations__)
