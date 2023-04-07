a = input()
b = input()

c = None
try:
    c = int(a) / int(b)
    print('After')
except ZeroDivisionError:
    c = 0
except ValueError:
    c = None
except Exception as err:
    print(err)
else:
    print("else")
finally:
    print('finally')

print(f'Result: {c}')
