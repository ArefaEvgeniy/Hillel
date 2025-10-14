class PositiveValue:

    def __init__(self):
        self.val = None

    def __get__(self, instance_self, instance_class):
        if self.val > 100:
            return self.val - 100
        return self.val

    def __set__(self, instance_self, value):
        if value < 0:
            value = abs(value)
        self.val = value


class Box:
    x = PositiveValue()
    y = PositiveValue()
    z = PositiveValue()

    def __init__(self, x, y, z, name='', color='white'):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.color = color


box = Box(1, 2, 3)
print(box.x, box.y, box.z) # виведе 1

box.x = -6  # ValueError
print(box.x, box.y, box.z)


box_2 = Box(1, 120, 99)
print(box_2.x, box_2.y, box_2.z)
