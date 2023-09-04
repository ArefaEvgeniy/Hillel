def summa(e, *args, y, **kwargs):
    print(f'e: {e}')
    print(f'y: {y}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    return 'RRR'


f = 10
a = 5
print(summa(4, 6, 66, 666, t=f, c=99, b=a, y=0))
