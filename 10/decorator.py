# Написати 2 декоратора, котрі будуть видавити:
# </----------\>
# помідори
# --шинка--
# ~салат~
# <\______/>
# При цьому перший декоратор буде загортати шинку у овочі,
# а другий у булочку


def vagitables(func):
    def wrapper():
        print("помідори")
        func()
        print("~салат~")

    return wrapper


def bread(func):
    def wrapper():
        print("</----------\>")
        func()
        print("<\__________/>")

    return wrapper


@bread
@vagitables
def sandwich(food="--шинка--"):
    print(food)


sandwich()
