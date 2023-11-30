def talk(bb=None):
    def whisper(word='так'):
        return word.title() + '!'

    if bb is not None:
        bb()

    return whisper


a = talk()
print(a())

print('-' * 50)

print(talk()())


def my_func():
    print('YES')


talk(my_func)


