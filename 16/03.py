import requests

# Виконуємо GET-запит до веб-сайту Bing
response = requests.get("https://kasta.ua/?main=men")

# Перевіряємо, чи запит був успішним
if response.status_code == 200:
    # Виводимо текст html документу
    print(response.text)
