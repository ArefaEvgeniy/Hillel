def my_func(**kwargs):
    print('kwargs:', kwargs)
    # for key in kwargs:
    #     print(f'{key}: {kwargs[key]}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


my_func(d=12, b=2, c=0, a=None, t='RRR')
