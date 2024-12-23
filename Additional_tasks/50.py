# Написати на Python програму, яка дізнається погоду у заданому місті.
# В інтернеті велика кількість сервісів, що "віддають" погоду через т.зв.
# REST API. Працюємо із сервісом Weather API. (Цей сервіс безкоштовний, але 
# потрібна реєстрація і є обмеження на кількість запитів від одного користувача
# в день). Зайдите за посиланням: https://www.weatherapi.com/  зареєструйтеся, 
# та скопіюйте і збережіть згенерований API Key, він стане в нагоді пізніше.
# Інтерактивний експлорер: https://www.weatherapi.com/api-explorer.aspx
# для того, щоб зрозуміти у якому вигляді треба робити запроси і у якому вигляді
# приходе відповідь.
#
# Перш, ніж писати програму, потрібно зареєструватися на сайті та знайти API Key
# який потрібно відправляти з кожним запитом на сервер.
# Для того, щоб робити запити треба використовувати метод get() модуля requests.
# Його треба з початку встановити за допомогою pip install requests


import requests
import json

API_Key = '<your_API_KEY>'  # треба вставити замість <your_API_KEY> свій згенерований API Key
request_api = 'http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no'


while True:
    city = input('Введіть назву міста: ')
    response = requests.get(request_api.format(API_Key, city))

    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            print('Місто:', data['location']['name'])
            print('Країна:', data['location']['country'])
            print(f"Розташування, широта: {data['location']['lat']}, довгота: {data['location']['lon']}")
            print('Часовий пояс:', data['location']['tz_id'])
            print('Температура:', data['current']['temp_c'])
            print('-' * 100)
        except (KeyError, json.decoder.JSONDecodeError):
            print('Не вірний формат відповіді:', response.text)
    else:
        print('Помилка, статус відповіді:', response.status_code)

    if input('Бажаєте вийти? (Y/Д): ').upper() in ('Y', 'Д'):
        break
