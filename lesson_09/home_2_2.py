def func(val):
    ret = "Вы ввели "
    val = val.replace(",", ".")
    if not val.replace("-", "", 1).replace(".", "", 1).strip().isdigit():
        ret += "не корректное число: " + val
    elif val.strip() == "0":
        ret += "ноль"
    else:
        ret += "отрицательное " if "-" in val else "положительное "
        ret += "целое число: " if "." not in val else "дробное число: "
        ret += val
    return ret


while True:
    e = input("Введите число либо значение для выхода: ").lower()
    if e == "выход" or e == "exit" or e == "quit" or e == "e" or e == "q":
        break
    else:
        print(func(e))