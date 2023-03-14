def shout(word='Yes'):
    print(f'{word}!!!')


shout()

scream = shout
print(scream)

scream()

print('-' * 100)

del shout

scream()

del scream

