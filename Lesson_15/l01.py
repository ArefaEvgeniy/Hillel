class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


if __name__ == "__main__":
    test_person = Person("Doe Joe", 33)
    print(test_person.name)
    print(test_person.age)
    print(test_person.greet())
    print('__name__:', __name__)
