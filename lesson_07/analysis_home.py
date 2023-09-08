# VARIANT 1

import random


def more_num():
    print('Наше число більше ;) Спробуй ще!')
    print(50 * '-')


def less_num():
    print('Наше число менше ;) Спробуй ще!')
    print(50 * '-')


def vanga():
    print('Да ти Ванга! Вгадано!')


def sproba(i):
    print('Спроба №%s. Введіть число від 1 до 10:' % (i))


answer = ''
while True:
    num_1 = random.randint(1, 10)
    #print(num_1)
    print('Ми загадали ціле число від  1 до  10 :)\nУ тебе є 3 спроби вгадати, яке саме ;)')
    print(50 * '-')

    i=1
    while i<4:
         sproba(i)
         attemp = int(input())
         i = i + 1
         if attemp < num_1:
            more_num()
         elif attemp > num_1:
            less_num()
         else:
            vanga()
            break

    print('Пограємо ще? (Так)')
    answer =input().upper()
    if answer != 'ТАК':
       break




# VARIANT 2

import random


def get_random(x, b):
    random_int = random.randint(x, b)
    return random_int


random_num = get_random(1, 3)
user_attempts = 3
while user_attempts > 0:
    user_input = int(input("Guess the number from 1 to 3: "))
    if user_input == random_num:
        user_quest = input("You Win!! Do you like to play again? Y/N ").upper()
        if user_quest == 'Y':
            random_num = get_random(1, 3)
            user_attempts = 3
            continue
        else:
            break
    else:
        user_attempts -= 1
        print(f"You didn't guess you have {user_attempts} more attempts.", )
        if user_attempts == 0:
            print("You loose. Will be better next time.")
        elif user_attempts > user_input:
            print("You give me a minor value.")
        else:
            print("You give me a highest value")




# VARIANT 3

import random


def main():
    random_num = get_random(1, 2)
    user_attempts = 3

    while user_attempts > 0:
        input_user = start_input()
        check_win = win_user(input_user, random_num)
        if check_win:
            exit_user = req_exit(check_win)
            if exit_user:
                random_num = get_random(1, 2)
                user_attempts = 3
                continue
            else:
                break
        else:
            user_att = att_user(user_attempts)
            user_attempts = user_att


def get_random(x, b):  # Get random:
    random_int = random.randint(x, b)
    return random_int


def req_exit(x):  # Check of exit:
    upper_req = x.upper()
    if upper_req == 'Y':
        return True


def start_input():  # Get the number from user:
    user_input = int(input("Guess the number from 1 to 2 👌: "))
    return user_input


def win_user(x, y):  # Check if won:
    if x == y:
        user_quest = input("You Win 😊!! Do you like to play again? Y/N ")
        return user_quest


def att_user(x):  # Check Attempt:
    x -= 1
    print(f"You didn't guess you have {x} more attempts.")
    if x == 0:
        print("You loose 🥺. Don't worry you can try again 😊.")
    return x


main()
