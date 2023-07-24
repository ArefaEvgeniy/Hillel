class Dog:
    def __init__(self, name, age, weight):
        self.__name = name  # private
        self._age = age  # protected
        self.weight = weight  # public

    def get_age(self):
        print(self._age)

    def get_name(self):
        print(self.__name)

    def __save(self):
        ...

    def my_save(self):
        ...
        self.__save()


dog = Dog('Rem', 8, 2.4)
print(dog.weight)
print(dog._age)
dog.get_age()
dog.get_name()

print(dog._Dog__name)
