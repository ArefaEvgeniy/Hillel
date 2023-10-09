# Створити свій тип даних, який у себе зберігатиме рядок. Це буде тип,
# що ітерується, але ітеруватися він буде наступним чином: на відміну від
# рядків які ітеруються по літерах, наш об'єкт буде ітеруватися за словами,
# при чому кожне слово він буде повертати з великої першої літери і з
# маленькими іншими, не залежно від того у якому вигляді це слово
# зберігається у нашому рядку. При цьому крапки і коми не виводяться.


class MyIter():
    def __init__(self, value):
        self.value = value.split()
        self.current = 0
        self.count = len(value.split())

    def __next__(self):
        if self.count > self.current:
            data = self.value[self.current]
            data = data.title().strip('.').strip(',')
            self.current += 1
            return data
        raise StopIteration


class MyClass:
    def __init__(self, data=''):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = ''
            if len(data) > 0:
                temp = []
                for item in data:
                    temp.append(str(item))
                self.data = ' '.join(temp)

    def __str__(self):
        return self.data

    def __iter__(self):
        return MyIter(self.data)


# ['ee', 'word', 44, True]
# ['ee', 'word', '44', 'True']
# 'ee word 44 True'

a = MyClass('МІЙ новий КЛАС, який розбиває РядкИ на слова')
print(a)

for item in a:
    print(item)


print('-' * 100)


class MyClass_2:
    def __init__(self, data=''):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = ''
            if len(data) > 0:
                temp = []
                for item in data:
                    temp.append(str(item))
                self.data = ' '.join(temp)
        self.current = 0
        self.count = len(self.data.split())

    def __next__(self):
        if self.count > self.current:
            data = self.data.split()[self.current]
            data = data.title().strip('.').strip(',')
            self.current += 1
            return data
        raise StopIteration

    def __str__(self):
        return self.data

    def __iter__(self):
        return self


a = MyClass_2('МІЙ новий КЛАС, який розбиває РядкИ на слова')
print(a)

for item in a:
    print(item)
