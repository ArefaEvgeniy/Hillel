f = open('example.txt', 'w')
...
f.close()


f = open('example.txt', 'w')
try:
    ...
finally:
    f.close()


with open('example.txt', 'w') as f:
    ...
