import requests
import sqlite3
from bs4 import BeautifulSoup


def parse_data(data: str) -> list:
    """ Функція парсингу даних з хтмл документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
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
            # rez.append({
            #     'title': title, 'href': href, 'price': price,
            #     'old_price': old_price
            # })
            # Для збереження в БД, нам потрібний список кортежів.
            rez.append((title, href, price, old_price))
    return rez


def create_table() -> bool:
    """створює таблицю video_cards, якщо такої ще немає"""
    sqlite_connection = sqlite3.connect('cards.db')
    sqlite_create_table_query = '''
            CREATE TABLE IF NOT EXISTS video_cards (
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
        sqlite_connection = sqlite3.connect('cards.db')
        cursor = sqlite_connection.cursor()
        cursor.executemany(
            "INSERT INTO video_cards('title', 'url', 'price', 'old_price' ) VALUES (?,?,?,?)",
            rows)
        sqlite_connection.commit()


def main() -> None:
    """ Головна функція диригент"""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        # data = get_data_by_selenium(url)
        rows = parse_data(data)
        # save_to_csv(rows)
        save_to_db(rows)


main()
