import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(45)

print("Пытаюсь загрузить страницу...")
url = "https://www.divan.ru/novorossijsk/category/svet"
driver.get(url)
print("Страница успешно загружена!")
time.sleep(15)  # Увеличил время ожидания


svets = driver.find_elements(By.CLASS_NAME, 'ProductCard_info__c9Z_4')
parsed_svets = []
for sv in svets:
    try:
        name = sv.find_element(By.CSS_SELECTOR, 'a span').text
        prise = sv.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU").text # уточнить что первый объект
        link = sv.find_element(By.TAG_NAME, 'link').get_attribute('href')

    except:
        print('Произошла ошибка при Парсинге')
        continue

    parsed_svets.append([name, prise, link])

driver.quit()

print(parsed_svets)

# читаемо в Excel и CSV
sv = pd.DataFrame(parsed_svets, columns=['Наименование', 'Цена', 'Ссылка'])
# Сохраняем в CSV для Excel
sv.to_csv('Svetiliki.csv', index=False, encoding='utf-8-sig', sep=';')
print("Файл создан!")