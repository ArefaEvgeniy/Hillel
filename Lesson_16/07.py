import requests
import time
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_data_by_selenium(url: str) -> str:
    """ Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service(executable_path=r"C:\Program Files\drivers\ChromeDriver\chromedriver-win64\141\chromedriver.exe")
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
        article_list = soup.find_all('article', attrs={'class': 'p__item group'})
        for li in article_list:
            # Пошук тега а
            img = li.find('img', attrs={'class': 'lazy'})
            image = img['data-srcset'].split()[0]
            title = img['title']
            div_link = li.find('div', attrs={'class': 'p__img'})
            link = div_link.find('a', href=True)
            href = link['href']
            old = li.find('span', attrs={'class': 't-bold'})
            old_price = old.text
            new = li.find('div', attrs={'class': 't-sunset'})
            if new:
                new_price = new.text
            else:
                new_price = old_price
            rez.append((title, href, new_price, old_price, image))
    return rez


def create_table() -> bool:
    """створює таблицю video_cards, якщо такої ще немає"""
    sqlite_connection = sqlite3.connect('kasta.db')
    sqlite_create_table_query = '''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                price INTEGER NOT NULL,
                old_price INTEGER NULL,
                image TEXT NOT NULL  
            );'''
    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    return True


def save_to_db(rows) -> None:
    """підключається до бази даних, і записує дані у таблицю video_cards"""
    if create_table():
        sqlite_connection = sqlite3.connect('kasta.db')
        cursor = sqlite_connection.cursor()
        cursor.executemany(
            "INSERT INTO products('title', 'url', 'price', 'old_price', 'image' ) VALUES (?,?,?,?,?)",
            rows)
        sqlite_connection.commit()


def main() -> None:
    """ Головна функція диригент"""
    url = 'https://kasta.ua/uk/market/muzhskie-kurtki/'
    data = []
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
    # data = get_data_by_selenium(url)
    rows = parse_data(data)

    save_to_db(rows)


main()
