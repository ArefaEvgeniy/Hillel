class Myclass:
    def __init__(self, name):
        self.name = name

    def __greet__(self):
        return f"Hello, {self.name}!"

    def greet(self):
        return self.__greet__()

    @staticmethod
    def hello(a, b):
        return a + b


a_1 = Myclass("Alice")
print(a_1.greet())
print(Myclass.hello(12, 45))
print(a_1.hello(8, 9))
