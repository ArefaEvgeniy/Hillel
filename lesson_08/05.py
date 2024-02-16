def talk(type='shout'):
    def shout(word='Yes'):
        return word + '!'

    def whisper(word='yes'):
        return word + '...'

    if type == 'shout':
        return shout
    else:
        return whisper


res = talk('44')
print(res('55'))

print(talk()('rrr'))
