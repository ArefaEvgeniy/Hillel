def shout(word='Да'):
    return word + '!'


scream = shout

del shout

print(scream())
