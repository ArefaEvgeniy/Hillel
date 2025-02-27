def func(choice='shout'):
    def shout(word='yes'):
        print(f"{word.title()}!")

    def wishper(word='no'):
        print(f"{word.lower()}...")

    if choice == 'shout':
        return shout
    else:
        return wishper


a = func('rr')
a('DARIA')

func('wishper')('Nikita')
func('shout')('nick')    # Nick!
func()('nick')    # Nick!
