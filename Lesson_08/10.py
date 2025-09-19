def func_1(height, name, surname, age):
    print('age =', age)
    print('name =', name)
    print('surname =', surname)
    print('height =', height)
    print('---' * 10)


def func_2(a, *args):
    print('args: ', args)
    print('---' * 10)


a = (1.88, 'Bob', 'Black', 18)
func_1(a[0], a[1], a[2], a[3])
func_1(*a)
func_2(*a)

b = {'name': 'Bob', 'age': 18, 'height': 1.88, 'surname': 'Black'}
func_1(b['height'], b['name'], b['surname'], b['age'])
func_1(**b)  # func_1(name='Bob', age=18, height=1.88, surname='Black')
