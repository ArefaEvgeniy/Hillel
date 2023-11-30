# генерація випадкового числа
# введення та валідація числа користувача
# порівнювати числа і щось видавати

from random import randint


def generate_secret_number(min_number, max_number):
    return randint(min_number, max_number)


def return_answer():
    res = False
    answer = input('Do you wont exit? (Y/N): ')
    if answer.upper() == 'Y':
        res = True

    return res


def main():
    min_number = 1
    max_number = 10
    max_attempts = 3

    while True:
        secret_number = generate_secret_number(min_number, max_number)

        for attempt in enumerate(1, max_attempts + 1):
            user_number = input_number()
            result = check_number(secret_number, user_number)

            if result:
                show_congratilation(attempt)
                break
            else:
                show_wrong(max_attempts - attempt + 1)
        else:
            swow_lose(secret_number)

        if return_answer():
            break


main()
