# Сделать программу в виде функций в которой нужно будет угадывать число.

from random import randint


from random import randint

DELIMITER = "." * 120


def intro() -> None:
    print(DELIMITER)
    print("Привет! Я младший брат chatGPT и очень хочу с тобой поиграть ...")
    print("Правила игры очень просты:\nЯ загадываю число в пределах от 1 "
          "до 10 включительно, а ты его должен угадать за 3 попытки.")
    print(DELIMITER)


def generate_data() -> (int, int):
    max_attempts = 3
    return randint(1, 10), max_attempts


def game_process(number: int, max_attempts: int) -> None:
    print("Отлично! Ну что ж поехали ... ")

    user_attempts = 0
    while True:
        print(DELIMITER)

        if max_attempts == user_attempts + 1:
            print("ВНИМАНИЕ!!! Последняя попытка!!!")
        else:
            print(f"Осталось попыток: {max_attempts - user_attempts}")

        if user_attempts >= max_attempts:
            print(f"Очень жаль, но попытки закончились!!! Мое число: {number}")
            break

        user_attempts += 1
        user_num = input("Твое число? ")
        if not user_num.isdigit():
            print("Это не число, зря потратил попытку.")
            continue

        user_num = int(user_num)
        if user_num < number:
            print("Я загадал побольше число!")
        elif user_num > number:
            print("Я загадал поменьше число!")
        else:
            print(f"Молодец! Ты угадал число за {user_attempts} "
                  f"попытк{'у'if user_attempts == 1 else 'и'}")
            break
    print(DELIMITER)


def get_exit() -> bool:
    res = False
    user_answer = input("Хочешь выйти? (y/д) ")
    if user_answer.lower() in ('y', 'д'):
        print("Как хочешь... До новых встреч!")
        print(DELIMITER)
        res = True
    return res


def main():
    while True:
        intro()
        number, max_attempts = generate_data()
        game_process(number, max_attempts)
        if get_exit():
            break


main()
