from bs4 import BeautifulSoup

# Створюємо об'єкт Beautiful Soup з HTML-рядка
html = """
<html><body><h1>Заголовок</h1>
<h2>New_1</h2>
<p>Перший абзац</p>
<h3>New_2</h3>
<h4>New_3</h4>
<h2>New_4</h2>
<h5>New_5</h5>
<p>Другий абзац</p>
<h2>New</h2>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")

# Знаходимо усі теги <p>
paragraphs = soup.find_all("h2")

# Виводимо текстовий вміст кожного тега <p>
for p in paragraphs:
    print(p.get_text())
