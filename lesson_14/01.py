# Створити свій клас даних на базі list(). Додати можливість віднімати та
# складати два об'єкти нового типу даних так, щоб при відніманні з першого
# видалялись тільки ті елементи, котрі є у второго списку, а при додаванні
# до першого списку додавались тільки ті елементи зі второго списку, котрих
# не має в першому.


class MyList(list):

    def __add__(self, other):
        new = self[:]
        for item in other:
            if item not in new:
                new.append(item)
        return new

    def __sub__(self, other):
        new = self[:]
        for item in other:
            if item in new:
                new.remove(item)
        return new


a = MyList((1, 2, '44', 'father'))
b = MyList((4, 1, 'mother', 2, 4))

c = a + b
d = a - b
print(a)
print(b)
print(c)
print(d)
