def func(**kwargs):
    print('kwargs:', kwargs)


a = 30
func()
print('-' * 50)
func(a=20, c=10, b=0, d=a)
