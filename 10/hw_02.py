# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
# При розв'язанні задачі зверніть увагу на наступні моменти:
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок.
#
# def first_word(text):
#     """ Пошук першого слова """
#     pass
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


def first_word(text: str) -> str:
    """
    Returns the first word from the given text.
    A word may contain letters and apostrophes.

    :param text: The input string.
    :return: The first word.
    """
    for symbol in text:
        if not symbol.isalpha() and symbol != "'":
            text = text.replace(symbol, " ")
    words = text.split()
    return words[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word(" \($<Об'єкт&100%>_completed!)") == "Об'єкт", 'Test7'
print('OK')
