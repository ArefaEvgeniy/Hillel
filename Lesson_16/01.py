import requests

res = requests.get('https://kasta.ua/?main=men')
# print(res.status_code)
# print(res.headers)

if res.status_code == 200:
    print(res.content.decode('utf-8'))
