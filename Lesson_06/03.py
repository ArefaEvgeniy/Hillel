str_1 = "Hello"
str_2 = "Привіт"

code_str = str_2.encode("utf-8")
print(code_str)
print(code_str.decode("utf-16"))
print(code_str.decode("latin-1"))
print(code_str.decode("utf-8"))
