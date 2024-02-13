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
    result = False

    for item in input_list:
        if isinstance(item, (str, int)):
            if word == str(item):
                result = True
                break

        if isinstance(item, (list, tuple, set)):
            result = find_word(word, item)
            if result:
                break

    return result


def main():
    while True:
        input_word = input('Enter your word: ')

        if not input_word:
            print('Repeat enter')
            continue

        if find_word(input_word, INPUT_LIST):
            print('Found word')
        else:
            print('Did not find word')

        print('Do you wont exit?')
        if input().upper() == 'Y':
            break


main()
