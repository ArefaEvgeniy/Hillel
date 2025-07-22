def func_1():
    print('Func_1')


def func_2():
    print('Func_2')


def func_3():
    print('Func_3')


def func_4():
    print('Func_4')


def func_5():
    print('Func_5')


def func_else():
    print('No function')


choices = {"1": func_1, "2": func_2, "3": func_3, "4": func_4, "5": func_5}

number = input("Enter your choice: ")
choices.get(number, func_else)()

# if number == "1":
#     func_1()
# elif number == "2":
#     func_2()
# elif number == "3":
#     func_3()
# elif number == "4":
#     func_4()
# elif number == "5":
#     func_5()
# else:
#     print("No function")



name = "Ivan"
surname = ""
sex = ""
age = 33

print(f"{name} {surname} {sex} {age}")

values = [str(i) for i in (name, surname, sex, age) if i]
print(" ".join(values))
