import sqlite3

# Створюємо з'єднання з файлом бази даних SQLite
conn = sqlite3.connect("books.db")

# Створюємо курсор для виконання команд SQL
cur = conn.cursor()

# # Створюємо таблицю books з чотирма стовпцями
# cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")
#
# # Додаємо три записи до таблиці books
# cur.execute("INSERT INTO books VALUES (1, 'Гайдамаки', 'Тарас Шевченко', 1841)")
# cur.execute("INSERT INTO books VALUES (2, 'Гаррі Поттер і філософський камінь', 'Джоан Роулінг', 1997)")
# cur.execute("INSERT INTO books VALUES (3, 'Шерлок Холмс', 'Артур Конан Дойл', 1892)")
#
# # Зберігаємо зміни в базі даних
# conn.commit()
#
# Робимо запит до таблиці books, щоб отримати усі книги, написані після 1900 року
cur.execute("SELECT * FROM books WHERE year > 1850")

# Отримуємо усі рядки результату запиту
rows = cur.fetchall()

# Виводимо кожен рядок на екран
for row in rows:
	print(row)
#
# Закриваємо з'єднання з базою даних
conn.close()
