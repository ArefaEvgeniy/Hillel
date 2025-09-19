def func(age, name, **kwargs):
    print('age =', age)
    print('name =', name)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    print('---' * 10)
    

def func_2(*args, **kwargs):
    pass


a = 1
b = 10
c = 33
func(name='Bob', age=15, surname='Black', height=1.47, address='NY', phone='123-456-7890')
func(name='Bob', age=15, surname='Black')
func(name='Bob', age=15)
func(15, 'Alice', surname='Black')
# func(15, 'Alice', 'Black')
