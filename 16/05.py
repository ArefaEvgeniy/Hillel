import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_data_by_selenium(url: str) -> str:
    """ Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service(executable_path=r"C:\Program Files\drivers\ChromeDriver\chromedriver-win64\chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir=C:\Profile")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(3)
    data = driver.page_source
    driver.quit()
    return data


def parse_data(data: str) -> list:
    """ Функція парсингу даних з хтмл документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
            # Пошук зображення
            img = li.find('img', attrs={'loading': 'lazy'})
            image = img['src']
            # Пошук тега а
            a = li.find('a', attrs={'class': 'ng-star-inserted'})
            # Беремо у тега а атрибут href
            href = a['href']
            # За допомогою атрибуту текст, забираємо всю текстову
            # інформацію, що міститься в цьому тегу
            title = li.find('span', attrs={'class': 'goods-tile__title'}).text
            old = li.find('div', attrs={'class': 'goods-tile__price--old'})
            price = li.find('div', attrs={'class': 'goods-tile__price'})
            # Стара ціна є не у всіх, тому потрібно зробити дефолтне значення
            old_price = ''
            if old:
                # Якщо контейнер із старою ціною є
                old = old.text
                # І в цьому контейнер є інфа
                if old:
                    # Забираємо лише те, що є цифрами та формуємо значення ціни
                    old_price = int(''.join(c for c in old if c.isdigit()))
            # Звичайна ціна є скрізь, тому формуємо значення
            price = int(''.join(c for c in price.text if c.isdigit()))
            # Результат за кожною відеокартою записуємо у вигляді словника
            rez.append({
                'title': title, 'image': image, 'href': href, 'price': price, 'old_price': old_price
            })
    return rez


def main() -> None:
    """ Головна функція диригент"""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/'
    data = requests.get(url).text
    # data = get_data_by_selenium(url)
    rows = parse_data(data)
    for item in rows:
        print(f"Відеокартка: {item['title']}")
        print(f"Зображення: {item['image']}")
        print(f"Посилання: {item['href']}")
        print(f"Ціна: {item['price']}")
        print(f"Стара ціна: {item['old_price']}")
        print('-' * 100)


if __name__ == '__main__':
    main()
