name = "Yehhen"


def func1():
    def func2():
        name = "Nick"
        print("Hello, " + name + "!")

    global name
    name = "Bob"
    print("Hello, " + name + "!")
    func2()


def func2(name):
    print("Hello, " + name + "!")


print("Hello, " + name + "!")
func1()
func2(name)
