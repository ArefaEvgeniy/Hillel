# Написати програму для пошуку у списку певного слова
# При цьому список може складатися з різних типів даних
# і мати не обмежену кількість вкладених один в одного списків або кортежів
# пошук зробити по всіх списках і кортежах, у тому числі і вкладених

INPUT_LIST = [
    1,
    '2',
    'cat',
    99,
    'dog',
    ['white', 'blue', 'black'],
    (4, 44, ['red', 'green', ('mother', 'father')]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]


def find_word(word, input_list):
    res = False

    for item in input_list:
        if isinstance(item, (str, int)) and str(item) == word:
            res = True
            break
        elif isinstance(item, (list, tuple, set)):
            res = find_word(word, item)
            if res:
                break

    return res


def main():
    while True:
        input_word = input('Enter your word: ')

        if not input_word:
            continue

        if find_word(input_word, INPUT_LIST):
            print('Word found')
        else:
            print('Word did not find')

        print('Do you wont exit? (Y/N)')
        if input().upper == 'Y':
            break


main()
