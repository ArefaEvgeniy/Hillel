def get_talk(type='shout'):
    def shout(word='Yes'):
        return word.upper() + '!'

    def whisper(word='Yes'):
        return word.lower() + '...'

    if type == 'shout':
        return shout
    else:
        return whisper


print(get_talk('vlad')('no'))
