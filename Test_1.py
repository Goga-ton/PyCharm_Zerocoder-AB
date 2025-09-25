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

