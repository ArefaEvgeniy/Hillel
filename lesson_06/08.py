# name = 'Tom'
#
#
# def say_hi():
#     def say_go():
#         print('Go', name)
#
#     global name
#     name = 'Bob'
#     print("Hello", name)
#     say_go()
#
#
# say_hi()
# print('Global name:', name)


name = 'Tom'


def say_hi(name):
    def say_go():
        print('Go', name)

    name = 'Bob'
    print("Hello", name)
    say_go()
    return name


name = say_hi(name)
print('Global name:', name)
