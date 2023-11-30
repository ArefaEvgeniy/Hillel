# Написать декоратор, который выдаст:
# </----------\>
# помидоры
# --ветчина--
# ~салат~
# <\______/>


def bread(func):
    def wraper(*args, **kwargs):
        print('</----------\>')
        result = func(*args, **kwargs)
        print('<\______/>')
        return result

    return wraper


def ingedients(func):
    def wraper(*args, **kwargs):
        print('#помидоры#')
        result = func(*args, **kwargs)
        print('~салат~')
        return result

    return wraper


@bread
@ingedients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()

