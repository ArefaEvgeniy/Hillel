import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Створюємо об'єкт webdriver для Google Chrome
service = Service(executable_path=r"C:\Program Files\drivers\ChromeDriver\chromedriver-win64\141\chromedriver.exe")

# Загружаю опції для того, щоб їх змінити
chrome_options = Options()
# Додаю посилання на директорії у котрій зберігається профайл хрома
chrome_options.add_argument(f"user-data-dir=C:\Profile")

driver = webdriver.Chrome(service=service, options=chrome_options)
# Відкриваємо веб-сторінку Bing
driver.get("https://kasta.ua/")
time.sleep(2)  # Потрібно дочекатися формування сторінки

# Знаходимо поле пошуку за ідентифікатором
search_box = driver.find_element(By.CLASS_NAME, "input-box")
# Вводимо запит "selenium python" в поле пошуку
search_box.send_keys("куртка")
time.sleep(4)

# Натискаємо кнопку пошуку за іменем
search_button = driver.find_element(By.CLASS_NAME, "search__btn")
time.sleep(2)
search_button.click()

# Перемикаюсь на нове вікно
chwd = driver.window_handles
driver.switch_to.window(chwd[-1])

# Пауза, щоб побачити результати пошуку
time.sleep(2)


# Закриваємо браузер
driver.quit()
