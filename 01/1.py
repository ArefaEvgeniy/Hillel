# import math
import requests
from math import pi


print("Hellow, worlds")
print(pi)

response = requests.get('https://shop.flixbus.ua/')
print(response.status_code)
print(response.text)

a = 90
print(a)

b = a - 44
