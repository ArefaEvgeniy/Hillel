import time
import sqlite3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_data_by_selenium(url: str) -> str:
    """ Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service(executable_path=r"C:\Program Files\drivers\ChromeDriver\chromedriver-win64\138\chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir=C:\Profile")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(3)
    data = driver.page_source
    driver.quit()
    return data


def get_data_by_requests(url: str) -> str:
    return requests.get(url).content.decode()


def parse_data(data: str) -> list:
    """ Функція парсингу даних з хтмл документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        list_elements = soup.find_all('div', attrs={'class': 'product_item'})
        for item in list_elements:
            link_div = item.find('div', attrs={'class': 'p__img'})
            link = link_div.find('a')
            href = link['href']
            full_href = 'https://kasta.ua' + href
            title = item.find('header', attrs={'class': 'p__info_name'}).text

            try:
                old_price = item.find('span', attrs={'class': 'product_item__old-cost'}).text
            except AttributeError:
                old_price = ""

            price = item.find('span', attrs={'class': 'product_item__new-cost'}).text
            rez.append((title, full_href, price, old_price))
    return rez


def create_table() -> bool:
    """створює таблицю video_cards, якщо такої ще немає"""
    sqlite_connection = sqlite3.connect('kurtki.db')
    sqlite_create_table_query = '''
            CREATE TABLE IF NOT EXISTS kurtki (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                price INTEGER NOT NULL,
                old_price INTEGER NULL            
            );'''
    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    return True


def save_to_db(rows) -> None:
    """підключається до бази даних, і записує дані у таблицю video_cards"""
    if create_table():
        sqlite_connection = sqlite3.connect('kurtki.db')
        cursor = sqlite_connection.cursor()
        cursor.executemany(
            "INSERT INTO kurtki('title', 'url', 'price', 'old_price' ) VALUES (?,?,?,?)",
            rows)
        sqlite_connection.commit()


def print_data(rows):
    for item in rows:
        print(f"Товар: {item['title']}")
        print(f"Посилання: {item['href']}")
        print(f"Ціна: {item['price']}")
        print(f"Стара ціна: {item['old_price']}")
        print('-' * 100)


def main() -> None:
    """ Головна функція диригент"""
    url = 'https://kasta.ua/uk/market/muzhskie-kurtki/'
    data = get_data_by_requests(url)
    # data = get_data_by_selenium(url)
    rows = parse_data(data)
    # print_data(rows)
    create_table()
    save_to_db(rows)


if __name__ == '__main__':
    main()
