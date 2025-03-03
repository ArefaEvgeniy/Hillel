text = """dfkgjhdfkj 
dsagdrsg res sadrkln lszdxfb nvdfkj nbgf
dfnkki rthjnkfdfgb"""

text_2 = "FGsgjkhkjk kjhkjghb\nДруга строка\nTherd line\nLast line\n"

file = open('Example.txt', 'w')
file.write(text_2)
file.close()

f = open('Example.txt', 'rb')
try:
    data = f.read()
finally:
    f.close()

print(data)
print(type(data))
print(data.decode("Windows-1251"))
