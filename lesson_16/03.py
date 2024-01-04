# Створити свій тип даних, який у себе зберігатиме рядок. Це буде тип, що
# ітерується, але ітеруватися він буде наступним чином: на відміну від рядків
# які ітеруються по літерах, наш об'єкт буде ітеруватися за словами, при чому
# кожне слово він буде повертати з великої першої літери і з маленькими
# іншими, не залежно від того у якому вигляді це слово зберігається у нашому
# рядку. При цьому крапки і коми не виводяться.


class Multer():
    def __init__(self, value):
        self.value = value.split()
        self.count = len(self.value)
        self.current = 0

    def __next__(self):
        if self.count > self.current:
            data = self.value[self.current]
            data = data.title().strip('.').strip(',')
            self.current += 1
            return data
        raise StopIteration


class MyClass(str):
    def __iter__(self):
        return Multer(self)


a = MyClass('МІй ноВий КЛАС, який зберігає РЯДКИ.')

print(a)

for item in a:
    print(item)
