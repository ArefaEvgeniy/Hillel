def func1():
    print("Ви вибрали пункт 1")


def func2():
    print("Ви вибрали пункт 2")


def func3():
    print("Ви вибрали пункт 3")


def func4():
    print("Ви вибрали пункт 4")


def func5():
    print("Ви вибрали пункт 5")


def func6():
    print("Ви вибрали пункт 6")


def func7():
    print("Невірний пункт меню. Спробуйте ще раз.")


func_variants = {"1": func1, "2": func2, "3": func3, "4": func4, "5": func5, "6": func6}
while True:
    answer = input("Введіть пункт меню: ")
    func_variants.get(answer, func7)()

    # if answer == "1":
    #     func1()
    # elif answer == "2":
    #     func2()
    # elif answer == "3":
    #     func3()
    # elif answer == "4":
    #     func4()
    # elif answer == "5":
    #     func5()
    # elif answer == "6":
    #     func6()
    # else:
    #     print("Невірний пункт меню. Спробуйте ще раз.")
