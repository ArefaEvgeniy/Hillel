# За допомогою функції filter() з котрежу слів відфільтрувати тільки ті,
# які є поліндромами (які однаково читаються в обидві сторони), регістр
# літер не враховувати.

inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')
polindroms = list(filter(lambda word: word.lower() == word[::-1].lower(), inputdata))
print(polindroms)
