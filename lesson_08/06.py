def talk(type='shout'):
    def whisper(word='так'):
        return word.lower() + '...'

    def shout(word='так'):
        return word.title() + '!'

    if type == 'shout':
        return shout
    else:
        return whisper


# dima = talk('RRR')
# print(dima('rrr'))

print(talk('wer')('Ура'))
