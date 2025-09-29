# Lesson-1 (ссылки)
from bs4 import BeautifulSoup as bs
import requests as rq
import pprint as pr

# url = "http://quotes.toscrape.com/"

res= rq.get("http://quotes.toscrape.com/")
print(res.content)
html = res.text

soup = bs(html, 'html.parser')

links = soup.find_all('a')
# pr.pprint(links)
for link in links:
    print(link.get('href'))


# Lesson-2 (поиск по тегам и классам)

import requests as rq
from bs4 import BeautifulSoup as bs

url = "http://quotes.toscrape.com/"

# res = rq.get(url)
html = rq.get(url).text
soup = bs(html, "html.parser")

tex = soup.find_all("span", class_="text")
avt = soup.find_all("small", class_="author")
for i in range(len(tex)):
    print(f"Цитата номер - {i+1} {tex[i].text}. \nАвтор: {avt[i].text}\n")
    # print(tex[i].text)
    # print(avt[i].text)


# Lesson-3 (поиск по словам)
import requests as rq
from bs4 import BeautifulSoup as bs

def get_english_words():
    url = "https://randomword.com/"
    try:
        res = rq.get(url)
        # print(res.text)
        sp = bs(res.content, "html.parser")
        english_word = sp.find("div", id="random_word").text
        word_definition = sp.find("div", id="random_word_definition").text
        return{'eng_w':english_word,
               'w_def':word_definition
        }

    except:
        print("Произошла ошибка")

def word_games():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("eng_w")
        opis = word_dict.get("w_def")

        print(f"значение слова - {opis}")
        user = input("Что это за слово? - ")
        if user == word:
            print("Вы угадали")
        else:
            print(f"Ответ НЕ ВЕРНЫЙ, было загадано - {word}")

        play_again = input ("Хотите сыграть еще раз y/n: ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_games()
# get_english_words()