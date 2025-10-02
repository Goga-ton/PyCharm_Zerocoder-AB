import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(45)

    print("Пытаюсь загрузить страницу...")
    driver.get("https://www.divan.ru/novorossijsk/category/svet")
    print("Страница успешно загружена!")

    # Явное ожидание элементов
    wait = WebDriverWait(driver, 15)
    svets = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ProductCard_info__c9Z_4')))
    print(f"Найдено товаров: {len(svets)}")

    parsed_svets = []
    for i, sv in enumerate(svets):
        try:
            name = sv.find_element(By.CSS_SELECTOR, 'a span').text
            price = sv.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU").text
            link = sv.find_element(By.TAG_NAME, 'link').get_attribute('href')

            # if link and link.startswith('/'):
            #     real_link = "https://www.divan.ru" + link
            # else:
            #     real_link = link

            parsed_svets.append([name, price, link])
            print(f"{i + 1}. Обработан: {name}")

        except Exception as e:
            print(f'Ошибка при парсинге товара {i + 1}: {e}')
            continue

    driver.quit()

    # Сохраняем данные
    if parsed_svets:
        sv = pd.DataFrame(parsed_svets, columns=['Наименование', 'Цена', 'Ссылка'])
        sv.to_csv('Svetiliki.csv', index=False, encoding='utf-8-sig', sep=';')
        print(f"Успешно сохранено {len(parsed_svets)} товаров")
    else:
        print("Нет данных для сохранения")

except Exception as e:
    print(f"Критическая ошибка: {e}")
    try:
        driver.quit()
    except:
        pass