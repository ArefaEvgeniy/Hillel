# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст
# від html-тегів і запише цей текст в інший файл. html-тег завжди починається
# з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що
# між ними. Функція отримує на вхід два параметри – ім'я файлу, який потрібно
# очистити, та ім'я файлу, куди потрібно записати очищений текст. Ім'я файлу,
# куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та
# приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде
# вирішення цієї домашки.
#
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте
# прибрати рядки, в яких немає інформації.


import os


def delete_html_tags(html_file, result_file=None):

    if (result_file is None or not os.path.exists(result_file)
            or not os.path.isfile(result_file)):
        print('Not found result file')
        return

    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.readlines()

    cleaned_html_lst = []
    for line in html:
        if line.count('<') > 1 or line.count('>') > 1:
            lst = line.split('>')
            lst = lst[1].split('<')
            if len(lst[0]) >= 1:
                line = lst[0]
                cleaned_html_lst.append(line)
    cleaned_html = '\n'.join(cleaned_html_lst)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_html)


delete_html_tags('draft.html', result_file='cleaned.txt')
