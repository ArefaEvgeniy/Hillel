class MyClass:
    def __init__(self, name="MyClass"):
        self.name = name

    def greet(self):
        return f"Hello from {self.name}!"


if __name__ == "__main__":
    my_class_instance = MyClass()
    print(my_class_instance.greet())
