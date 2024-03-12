class FoundException(Exception):
    def __init__(self, message='d має бути більшим за 10'):
        super().__init__(message)


a = 10
b = 20
c = [15, 12, None]

d = a / (b - c[1] - 5)
if d < 10:
    raise FoundException()
