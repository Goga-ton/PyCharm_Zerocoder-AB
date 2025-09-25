#lesson1

import requests
import pprint
response = requests.get("https://api.github.com")

print(response.status_code)
print(response.ok)
if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

# print(response.text)
# print(response.content)
print(response.json())
pprint.pprint(response.json())


#lesson2

import requests
import requests
import pprint

find = {
    'q':'JavaScript'
}

response = requests.get("https://api.github.com/search/repositories", params=find)

response_json = response.json() # создаем переменную

pprint.pprint(response_json)
print(f"Количество репозиториев с использованием json: {response_json['total_count']}")


#lesson3

import requests

img = 'https://st.fl.ru/users/io/iosipova2013/foto/f_94865c228a43c0d7.jpeg'

response = requests.get(img) # отправили запрос по ссылке, только вместо ссылки в ковычках переменная

with open("PS02_picture.jpg", "wb") as file: file.write(response.content) # Открываем/создаем файл и помещаем в него картинку


#lesson4

import requests

url = 'https://jsonplaceholder.typicode.com/posts'

dataSP = {
    "tittle" : "Тестовый post запрос",
    "body" : "Тестовый контент post запроса",
    "userID" : 2
}

response = requests.post(url, data = dataSP)

print(response.status_code)

print(f'ответ - {response.json()}')
