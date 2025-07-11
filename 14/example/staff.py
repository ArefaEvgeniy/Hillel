import const


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.status = const.STATUSES[0]


class Pilot(Person):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours


class Stuart(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Outstaff(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Repear(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
