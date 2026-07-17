import requests

res = requests.get('https://kasta.ua/uk/search/?q=%D1%88%D0%BE%D1%80%D1%82%D0%B8')
print(res.status_code)
print(res.headers)

if res.status_code == 200:
    print(res.content.decode())
