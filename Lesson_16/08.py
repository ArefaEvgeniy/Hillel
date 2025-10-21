def func1():
    print("Ви вибрали пункт 1")


def func2():
    print("Ви вибрали пункт 2")


def func3():
    print("Ви вибрали пункт 3")


def func4():
    print("Ви вибрали пункт 4")


def func5():
    print("Невірний пункт меню. Спробуйте ще раз.")


answer_dict = {"1": func1, "2": func2, "3": func3, "4": func4}
while True:
    answer = input("Введіть пункт меню: ")

    answer_dict.get(answer, func5)()

    # if answer == "1":
    #     func1()
    # elif answer == "2":
    #     func2()
    # elif answer == "3":
    #     func3()
    # elif answer == "4":
    #     func4()
    # else:
    #     print("Невірний пункт меню. Спробуйте ще раз.")
