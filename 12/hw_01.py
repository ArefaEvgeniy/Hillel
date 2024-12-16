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


import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        text_html = file.read()

    def get_cleaned_text(cleaned_text=''):
        in_tag = False
        for char in text_html:
            if char == '<':
                in_tag = True
            elif char == '>':
                in_tag = False
            elif not in_tag:
                cleaned_text += char
        return cleaned_text

    def get_text_without_empty_lines(cleaned_text):
        lines = cleaned_text.splitlines()
        non_empty_lines = [line.strip() for line in lines if line.strip()]
        final_text = '\n'.join(non_empty_lines)
        return final_text

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(get_text_without_empty_lines(get_cleaned_text()))


delete_html_tags('draft.html')
