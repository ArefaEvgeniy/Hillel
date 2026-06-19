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
    (4, 44, ['red', 'green', ('mother', [0, 100, 66], 'father',)]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]


def find_word(word, input_list):
    result = False

    for item in input_list:
        if isinstance(item, (str, int)) and str(item) == str(word):
            result = True
            break

        # elif isinstance(item, (tuple, list, set)):
        #     if word in item:
        #         result = True
        #         break

        elif isinstance(item, (tuple, list, set)):
            result = find_word(word, item)
            if result:
                break

    return result


def main():
    while True:
        input_value = input('Enter your world: ')

        if not input_value:
            print('Error input')
            continue

        if find_word(input_value, INPUT_LIST):
            print('Found word')
        else:
            print('Did not find word')

        print('Do you wont exit (Y/Д/Т)')
        if input().upper() in ('Y', 'Д', 'Т'):
            break


main()
