class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


def my_func(name):
    print(f"My function says hello to {name}!")


a_1 = MyClass("Alice")
print(a_1.greet())  # Output: Hello, Alice!
print(a_1.name)  # Output: Alice

a_2 = MyClass("Bob")
print(a_2.greet())  # Output: Hello, Bob!

a_2.my_func = my_func
a_2.my_func("Charlie")
