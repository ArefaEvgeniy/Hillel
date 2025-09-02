a = 100

if a < 0:
    res = 'negative'
else:
    res = 'non-negative'
print('res:  ', res)


res_2 = 'negative' if a < 0 else 'non-negative'
print('res_2:', res_2)

print('negative') if a < 0 else print('non-negative')
