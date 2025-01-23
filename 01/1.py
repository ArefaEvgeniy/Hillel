# import math
import requests
from math import pi


print("Hellow, world")
print(pi)

response = requests.get('https://shop.flixbus.ua/')
print(response.status_code)
print(response.text)
