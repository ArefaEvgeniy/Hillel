def example_function(arg3, arg1, arg4, **kwargs):
    print('arg1:', arg1)
    print('arg4:', arg4)
    print('arg3:', arg3)
    print('kwargs:', kwargs)


kwargs = {'arg1': 1, 'arg3': 3, 'arg2': 2, 'arg4': 4}
example_function(**kwargs)
# example_function(arg1=1, arg3=3, arg2=2)
