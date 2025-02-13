from collections import defaultdict

defdict = defaultdict(lambda: 100)


print(defdict['d'])
print(defdict)
defdict.update({'e': 1, 't': [1, 2, 3]})
print(defdict)
print(defdict['e'])
print(defdict['f'])
print(defdict)
