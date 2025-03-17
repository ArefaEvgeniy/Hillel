# from test.start import func
# from test.start import MyClass
# from test.start import MyClass, func
from test import start
from test_2.start_2 import func as func_2

start.func()
# func()
func_2()

obj = start.MyClass()
# MyClass()
print(obj)
