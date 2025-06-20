def func_1(e, w, a):
    print('e:', e)
    print('w:', w)
    print('a:', a)


a = {'w': 5, 'a': 3, 'e': 2134}
func_1(**a)  # ** -> w=5, a=3, e=2134      * -> ('w', 'a', 'e')
