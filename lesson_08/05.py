def talk():
    def whisper(word='так'):
        return word.lower() + '...'

    return whisper


dima = talk()
print(dima())
