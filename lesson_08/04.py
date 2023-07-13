def talk(type='shout'):
    def whisper(word='Да'):
        return word.lower() + '...'

    def shout(word='Да'):
        return word + '!'

    if type == 'shout':
        return shout
    else:
        return whisper


# dd = talk()
# print(dd())

print(talk('whisper')())
