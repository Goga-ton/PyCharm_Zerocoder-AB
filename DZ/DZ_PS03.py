import requests as rq
from bs4 import BeautifulSoup as bs
from googletrans import Translator

trans = Translator()

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
        word_ru = trans.translate(word, dest='ru')
        opis_ru = trans.translate(opis, dest='ru')

        print(f"значение слова - {opis_ru.text}")
        user = input("Что это за слово? - ")
        if user == word:
            print("Вы угадали")
        else:
            print(f"Ответ НЕ ВЕРНЫЙ, было загадано - ''{word}'' переводиться как: ''{word_ru.text}''")

        play_again = input ("Хотите сыграть еще раз y/n: ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_games()
# get_english_words()

