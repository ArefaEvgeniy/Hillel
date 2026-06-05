str_2 = 'restart  The   Zen of Python. by "TIM"                Petenrs'

print(str_2.strip(' rs'))

print(str_2.split('y'))
print(str_2.split('en'))
new_list = str_2.split()
print(new_list)

new_str = ' '.join(new_list)
print(new_str)
