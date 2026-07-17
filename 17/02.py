import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Створюємо об'єкт webdriver для Google Chrome
service = Service(executable_path=r'C:\Program Files\drivers\ChromeDriver\chromedriver-win64\150\chromedriver.exe')
# Загружаю опції для того, щоб їх змінити
chrome_options = Options()
# Додаю посилання на директорії у котрій зберігається профайл хрома
chrome_options.add_argument(f"user-data-dir=C:\Profile")

driver = webdriver.Chrome(service=service, options=chrome_options)
# Відкриваємо веб-сторінку Bing
driver.get("https://www.bing.com")
time.sleep(3)  # Потрібно дочекатися формування сторінки

# Знаходимо поле пошуку за ідентифікатором
import pdb
pdb.set_trace()
search_box = driver.find_element(By.ID, "sb_form_q")

# Вводимо запит "selenium python" в поле пошуку
search_box.send_keys("python 4")


# Натискаємо кнопку пошуку за іменем
search_button = driver.find_element(By.CLASS_NAME, "search")
search_button.click()
# Пауза, щоб побачити результати пошуку
time.sleep(5)

# Закриваємо браузер
driver.quit()
