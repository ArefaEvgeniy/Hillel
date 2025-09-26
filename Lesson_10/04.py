def func(a='shout'):
    def shout(world='world'):
        return f'HELLO, {world.upper()}!'

    def whisper(world='world'):
        return f'hello, {world}...'

    if a == 'shout':
        return shout
    else:
        return whisper


res = func('shout')
print(res)
print(res('misha'))
print(func('whisper')('Olexandr'))
