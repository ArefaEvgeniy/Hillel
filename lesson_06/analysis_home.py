Name = input('Введите имя ')
while True:
    Age = input("Введите возраст ")
    Age = int(Age)
    if Age < 0 or Age == 0 or not str(Age).isnumeric():
        print("Ошибка, повторите ввод")
    elif Age < 10:
        print(f"Привет, шкет {Name}")
    elif Age <= 18:
        print(f"Как жизнь {Name}")
    elif Age < 100:
        print(f"Что желаете {Name}")
    else:
        print(f"{Name} вы лжете - в наше время столько не живут...")
    Exit = input(r"Желаете выйти Д\Н: ")
    if Exit.lower() == "д":
        break
