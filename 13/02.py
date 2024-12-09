class My_Except(Exception):
    pass


a = 10
b = '0'
print('start')
try:
    raise My_Except
    c = a / b
    print('more')
except IndexError:
    c = None
except (ValueError, TypeError):
    c = ' '
except ZeroDivisionError:
    c = 0
except SyntaxError:
    c = 100
except My_Except:
    c = -100
print(c)

print('end')
