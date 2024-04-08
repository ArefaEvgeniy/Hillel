# Написати програму для пошуку у списку певного слова при цьому список може
# складатися з різних типів даних і мати не обмежену кількість вкладених один
# в одного списків або кортежів пошук зробити по всіх списках і кортежах, у
# тому числі і вкладених

INPUT_LIST = [
    1,
    '2',
    'cat',
    99,
    'dog',
    (4, 44, ['red', 'green', ('mother', 'father',)]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]

target = 'big'


def find_word(word, input_list):
    result = False

    for item in input_list:
        if isinstance(item, (str, int, float)) and str(item) == str(word):
            result = True
            break

        if isinstance(item, (tuple, list, set)):
            result = find_word(word, item)
            if result:
                break

    return result


print(find_word(target, INPUT_LIST))
