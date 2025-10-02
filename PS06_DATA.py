# Очистка данных
import requests
from bs4 import BeautifulSoup

url = "https://"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all('tr') # записывем сюда все ряды
data = []
for row in rows: #перебираем ряды
    cols = row.find_all('td') # ищем колонки они же ячейки
    cleaned_cols = [col.text.strip() for col in cols] # перебираем ячейки и очищяем от пробелов
    data.append(cleaned_cols) # доббавляем значение всех ячеек одной строки в список, т.к. при следующем круге
                              # переменная замениться на данные из второй строки
print(data)


# Преобразование (предположи что мы достали информацию из списка и у нас список внутри списка)

data = [
    ['100', '200', '300'],
    ['400', '500', '600']
]

numbers = []
for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)
print(numbers)


# Фильтрация данных

data = [
    [100, 200, 300],
    [400, 500, 600],
    [150, 130, 140]
]
list = []

for row in data:
    for item in row:
        if item > 190:
            list.append(item)
print(list)