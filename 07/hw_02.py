# На вхід функції correct_sentence передається два речення. Необхідно
# повернути їх виправлену копію так, щоб вони завжди починалися з великої
# літери та закінчувалися крапкою. Зверніть увагу, що не всі виправлення
# необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не
# потрібно, це буде помилкою
#
# Вхідні аргументи: string.
# Вихідні аргументи: string.
#
#
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
#      pass
#
#
# correct_sentence("greetings, friends") -> "Greetings, friends."
# correct_sentence("hello") -> "Hello."
# correct_sentence("Greetings. Friends") -> "Greetings. Friends."
# correct_sentence("Greetings, friends.") -> "Greetings, friends."
# correct_sentence("greetings, friends.") -> "Greetings, friends."


def correct_sentence(text: str) -> str:
    return (text[0].capitalize() + text[1:]).rstrip(".") + "."


result = correct_sentence("greetings, friends.")

print(result)
