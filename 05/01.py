str_1 = "The Zen of Python's, by \"Tim\" Peters.\nNew \tline"
# s_1 = "The Zen of Python's, by "
# s_2 = '"Tim" Peters'
# str_1 = s_1 + s_2
str_2 = 'The Zen of Python. by "Tim" Peters'

print(str_1)
print(id(str_1))
print(str_2)
print(id(str_2))

a = "Hello, World!"
b = "RR\".\nR"

print(a + b)

print(len(b))

str_3 = r'"\n" - newline'
print(str_3)

str_4 = """The Zen of Python's, by "Tim" Peters.
New line is represented by, and tab is represented by.
Second line of the string.
"""

print(str_4)
