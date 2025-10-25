# Дана послідовність слів. Написати функцію, яка повертає послідовність 
# слів, в якій у словах довжини 3 всі літери великі, а всі слова, що 
# починаються на "q" або "f" виключені. Використовувати ланцюжки.
# Приклад: ["The", "quick", "brown", "fox"] -> ["THE", "brown"]


def funk2(words_list):
    return map(
        lambda x: x.upper() if len(x) == 3 else x, 
        filter(lambda x: not x.startswith(('q', 'f')), words_list)
    )


words = ["The", "quick", "brown", "fox"]

print(list(funk2(words)))
