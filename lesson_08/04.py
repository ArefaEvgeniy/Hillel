def shout(word='так'):
    return word.title() + '!'


print(shout('да'))
print(shout)

a = shout

print(a('yes'))

del shout

print(a())
