import requests

# Виконуємо GET-запит до веб-сайту Bing
response = requests.get("https://www.bing.com")

# Перевіряємо, чи запит був успішним
if response.status_code == 200:
    # Виводимо текст html документу
    print(response.text.encode('utf-8'))
