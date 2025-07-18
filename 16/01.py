import requests

response = requests.get('https://kasta.ua/uk/market/muzhskie-kurtki/')


if response.status_code == 200:
    print(response.content.decode())
