def shout(word='Yes'):
    return word + '!'


scream = shout
print(shout())
print(scream())

del shout
print(scream())
print(scream)
