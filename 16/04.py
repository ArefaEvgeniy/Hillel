from bs4 import BeautifulSoup

# Створюємо об'єкт Beautiful Soup з HTML-рядка
html = """
<html><body><h1>Заголовок</h1>
<p>Перший абзац</p>
<p>Другий абзац</p>
<h2>New 1</h2>
<h1>New 2</h1>
<h2>New 3</h2>
<h3>New 4</h3>
<h5>New 5</h5>
<h2>New 6</h2>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")

# Знаходимо усі теги <p>
paragraphs = soup.find_all("h2")

# Виводимо текстовий вміст кожного тега <p>
for p in paragraphs:
    print(p.get_text())
