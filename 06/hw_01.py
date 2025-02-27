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

def check(my_variable):
    import string

    string_letters = my_variable

    letters = string.ascii_letters

    first, second = string_letters.split('-')
    first_index = letters.index(first)
    second_index = letters.index(second)

    print(letters[first_index:second_index + 1])


check("a-c")
print()
check("a-a")
print()
check("s-H")
print()
check("a-A")
print()
