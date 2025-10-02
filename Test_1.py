import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Настройки Chrome для стабильности
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

try:
    print("Запускаю браузер...")
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Устанавливаем короткие таймауты
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(5)

    print("Загружаю страницу...")
    driver.get("https://www.divan.ru/category/svet")
    print("Страница загружена!")

    # Даем время на загрузку контента
    time.sleep(5)

    # Простой поиск элементов
    print("Ищу товары...")
    svets = driver.find_elements(By.CSS_SELECTOR, '[class*="ProductCard"]')
    print(f"Найдено элементов: {len(svets)}")

    # Если не нашли по одному селектору, пробуем другие
    if not svets:
        svets = driver.find_elements(By.CLASS_NAME, 'ProductCard_info__c9Z_4')
    if not svets:
        svets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid*="product"]')

    print(f"Итого найдено товаров: {len(svets)}")

    parsed_svets = []
    success_count = 0

    for i, sv in enumerate(svets[:10]):  # Ограничимся 10 товарами для теста
        try:
            print(f"Обрабатываю товар {i + 1}...")

            # Название - универсальный поиск
            name_elements = sv.find_elements(By.CSS_SELECTOR, 'span, a')
            name = "Не найдено"
            for elem in name_elements:
                text = elem.text.strip()
                if text and len(text) > 5:  # Ищем осмысленный текст
                    name = text
                    break

            # Цена - ищем числа и символы валют
            price_elements = sv.find_elements(By.CSS_SELECTOR, 'span, div')
            price = "Не найдена"
            for elem in price_elements:
                text = elem.text.strip()
                if any(char.isdigit() for char in text) and ('руб' in text.lower() or '₽' in text):
                    price = text
                    break

            # Ссылка
            link_elements = sv.find_elements(By.TAG_NAME, 'a')
            real_link = "Не найдена"
            for link_elem in link_elements:
                href = link_elem.get_attribute('href')
                if href and 'divan.ru' in href:
                    real_link = href
                    break

            if name != "Не найдено" and price != "Не найдена":
                parsed_svets.append([name, price, real_link])
                success_count += 1
                print(f"✓ Успешно: {name}")
            else:
                print(f"✗ Пропущен: недостаточно данных")

        except Exception as e:
            print(f"✗ Ошибка в товаре {i + 1}: {str(e)[:50]}...")
            continue

    print(f"\nОбработка завершена. Успешно: {success_count}/{len(svets)}")

    # Сохраняем данные
    if parsed_svets:
        sv = pd.DataFrame(parsed_svets, columns=['Наименование', 'Цена', 'Ссылка'])
        sv.to_csv('Svetiliki.csv', index=False, encoding='utf-8-sig', sep=';')
        print(f"✅ Сохранено в Svetiliki.csv")
    else:
        print("❌ Нет данных для сохранения")

except Exception as e:
    print(f"❌ Критическая ошибка: {e}")

finally:
    try:
        driver.quit()
        print("Браузер закрыт")
    except:
        pass