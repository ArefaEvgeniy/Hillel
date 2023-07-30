def define(user_text):
    definition_dict = {"": "положительное", "-": "отрицательное", "float": "дробное", "int": "целое"}
    key_sign = ""
    int_or_float = "float"
    if user_text[0] == "-":
        key_sign = "-"
        user_text = user_text[1:]

    if user_text.count(".") > 1 or not user_text.replace(".", "").isdigit():
        return f"Вы ввели не корректное число: {user_text}"

    num = float("".join([key_sign, user_text]))
    if num == 0:
        return "Вы ввели число 0"

    if int(num) == num:
        int_or_float = "int"
        num = int(num)

    return f"Вы ввели {definition_dict[key_sign]} {definition_dict[int_or_float]} число: {num}"


def main():
    while True:
        user_input = input("Enter number or command to quit: ").replace(",", ".")
        if user_input.lower() in ("выход", "exit", "quit", "e", "q"):
            break

        print(define(user_input))


main()