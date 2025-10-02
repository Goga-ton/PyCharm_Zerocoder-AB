import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Firefox()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

vakans = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VIUF0yM')
parsed_data = []
for vac in vakans:
    try:
        title_element = vac.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_6-0-10')
        title = title_element.text
        link = title_element.get_attribute('href')
        company = vac.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        salary = vac.find_element(By.CSS_SELECTOR, 'div.compensation-labels--vwum2s12fQUurc2J').text


    except:
        print('Произошла ошибка при Парсинге')
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

#если нужен красивый csv то этот блок
with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writ = csv.writer(file)
    writ.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка на вакансию'])
    writ.writerows(parsed_data)

# читаемо в Excel и CSV
df = pd.DataFrame(parsed_data, columns=['Название вакансии', 'Компания', 'Зарплата', 'Ссылка на вакансию'])
# Сохраняем в CSV для Excel
df.to_csv('hh_excel.csv', index=False, encoding='utf-8-sig', sep=';')