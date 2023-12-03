# Зробити програму за допомогою функцій/функцій у якій потрібно буде вгадувати
# число. Алгоритм програми можна зробити будь-яким, на розсуд виконавця.
# Один з варіантів:
# - з допомогою зовнішньої функції random створити довільне число, наприклад
# у діапазоні від 1 до 10.
# - У циклі запропонувати користувачеві вгадати загадане число за певну
# кількість спроб, наприклад 3. Якщо введене число угадано, то повідомити про
# це і запропонувати зіграти заново. Якщо ж не вгадано, то повідомити задумане
# число більше чи менше. Кожен із пунктів можна організувати як окремої
# функції, основний алгоритм можна розбити на ще кілька функцій.
#
# from random import randint


from random import randint

DELIMITER = "." * 120


def intro() -> None:
    print(DELIMITER)
    print("Вітання! Я молодший брат chatGPT і дуже хочу з тобою погратись.")
    print("Правила гри дуже прості:\nЯ загадую число в межах від 1"
           "До 10 включно, а ти його маєш вгадати за 3 спроби.")
    print(DELIMITER)


def generate_data() -> (int, int):
    max_attempts = 3
    return randint(1, 10), max_attempts


def game_process(number: int, max_attempts: int) -> None:
    print("Чудово! Ну що ж поїхали...")

    user_attempts = 0
    while True:
        print(DELIMITER)

        if max_attempts == user_attempts + 1:
            print("УВАГА!!! Остання спроба!!!")
        else:
            print(f"Залишилось спроб: {max_attempts - user_attempts}")

        if user_attempts >= max_attempts:
            print(f"Дуже шкода, але спроби закінчились! Моє число:{number}")
            break

        user_attempts += 1
        user_num = input("Твоє число?")
        if not user_num.isdigit():
            print("Це не число, даремно витратив спробу.")
            continue

        user_num = int(user_num)
        if user_num < number:
            print("Я загадав більше!")
        elif user_num > number:
            print("Я загадав трохи менше!")
        else:
            print(f"Молодець! Ти вгадав число за{user_attempts} "
                  f"спроб{'у'if user_attempts == 1 else 'и'}")
            break
    print(DELIMITER)


def get_exit() -> bool:
    res = False
    user_answer = input("Хочеш вийти?(y/д) ")
    if user_answer.lower() in ('y', 'д'):
        print("Як хочеш... До нових зустрічей!")
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
