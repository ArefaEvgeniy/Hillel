# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди
# менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з
# усім набором потрібних букв
#
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA


import string

ascii_str = string.ascii_letters
user_letters = input("Enter a range of letters in the format 'a-z': ")

first_letter_index = ascii_str.index(user_letters[0])
second_letter_index = ascii_str.index(user_letters[-1])
print(ascii_str[first_letter_index:(second_letter_index + 1)])
