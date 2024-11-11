cleaned_string = 'sdsfs   fefkn csd'

words = cleaned_string.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

hashtag = '#' + ''.join(capitalized_words)


hashtag_2 = '#' + cleaned_string.title().replace(' ', '')

import re
