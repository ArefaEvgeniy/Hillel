name = "Yehhen"


# def func1():
#     global name
#     name = "Bob"
#     print("Hello, " + name + "!")


# def func2():
#     print("Ciao, " + name + "!")


def func1():
    name = "Bob"
    print("Hello, " + name + "!")
    return name


def func2(name):
    print("Ciao, " + name + "!")


print("Hello, " + name + "!")
name = func1()
func2(name)
