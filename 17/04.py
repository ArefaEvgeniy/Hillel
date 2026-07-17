from bs4 import BeautifulSoup

# Створюємо об'єкт Beautiful Soup з HTML-рядка
html = """
<html>
    <body>
        <h1>Заголовок</h1>
        <p>Перший абзац</p>
        <p>Другий абзац</p>
        <h2>New</h2>
        <div class="section">
            <h1>Used</h1>
            <p>Третій абзац</p>
            <h3>Like New</h3>
            <h1>Refurbished</h1>
            <a href="https://example.com">Посилання</a>
            <a href="https://example.org">Інше посилання</a>
        </div>
        <div>
            <h1>New</h1>
                <div>
                    <p>Четвертий абзац</p>
                </div>
        </div>
    </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

# Знаходимо усі теги <p>
paragraphs = soup.find_all("p")

# Виводимо текстовий вміст кожного тега <p>
for p in paragraphs:
    print(p.get_text())

print("-------------------")

links = soup.find_all("a")
for link in links:
    print(link['href'])
