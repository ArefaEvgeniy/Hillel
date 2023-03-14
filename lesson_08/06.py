def talk(type='shout'):
    def shout(word='yes'):
        return word.upper() + '!!!'

    def whisper(word='yes'):
        return word.lower() + '...'

    if type == 'shout':
        return shout
    else:
        return whisper


res = talk()
print(res())

print(talk()('Dima'))
