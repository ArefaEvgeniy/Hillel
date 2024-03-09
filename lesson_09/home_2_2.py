def func(val):
    ret = "Вы ввели "
    val = val.replace(",", ".").strip()
    if not val.replace("-", "", 1).replace(".", "", 1).strip().isdigit():
        ret += " не правильне число " + val
    elif val == "0" or (val.replace("-", "", 1).replace(".", "", 1).isdigit()
                        and int(val.replace("-", "", 1).replace(".", "", 1)) == 0):
        ret += "нуль"
    else:
        ret += "від'ємне " if "-" in val else "позитивне "
        ret += "ціле число: " if "." not in val else "дробове число: "
        ret += val
    return ret


def main():
    while True:
        e = input("Введить число або значення виходу: ").lower()
        if e == "выход" or e == "exit" or e == "quit" or e == "e" or e == "q":
            break
        else:
            print(func(e))


main()
