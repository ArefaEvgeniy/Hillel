# Написать программу для поиска в списке определённого слова
# При этом список может состоять из разного типа данных
# и иметь не ограниченное число вложенных друг в друга списков или кортежей
# поиск произвести по всем списка и кортежам, в том числе и вложенным

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


def find_word(word, input_list):
    result = False

    for item in input_list:
        if isinstance(item, (str, int)) and str(item) == word:
            result = True
            break
        elif isinstance(item, (tuple, list, dict, set)):
            result = find_word(word, item)
            if result:
                break
    return result


res = find_word(input(), INPUT_LIST)
print(res)
