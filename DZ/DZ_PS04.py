from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
assert "Википедия" in browser.title

def search():
    while True:
        search_box = browser.find_element(By.ID, "searchInput")
        a = input("Введите запрос для Википедии - ")
        search_box.send_keys(a)
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        error_box = browser.find_element(By.TAG_NAME, "b").text
        print(error_box)
        if "Создать страницу" in error_box:
            print("Страница не найдена попробуйте другой запрос")
            browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
            time.sleep(2)
        else:
            vibor_deistv()

def vibor_deistv():
    print(f"Страница найдена! Выберети один из вариантов действия:\n1 - листать параграфы нажимая Enter\n2 - "
          f"выбрать ссылку для перехода на одну из связанных страниц\n3 - Выйти из программы")
    while True:
        b = input("Ведите значение - ")
        if b == "1":
            list_paras()
        elif b == "2":
            goto_link()
        elif b == "3":
            exit()
        else:
            print("Вы ввели недопустимое значение, попробуйте еще раз")

def list_paras():
    parags = browser.find_elements(By.TAG_NAME,"p")
    for prg in parags:
        print(prg.text)
        input()
    print(f"Страница найдена! Выберети один из вариантов действия:\n1 - листать параграфы нажимая Enter\n2 - "
          f"выбрать ссылку для перехода на одну из связанных страниц\n3 - Выйти из программы")


def goto_link():
    links = browser.find_elements(By.CSS_SELECTOR, "a[href*='/wiki/']")
    print(f"Найдено ссылок - {len(links)}")
    for link in links:
        tit = link.get_attribute("title")
        if not tit:
            continue
        print(tit)
        x = input('Хотите перейти по этой ссылке введите "y", если хотите продолжить просмотр ссылок нажмите Enter - ').lower()
        if x == "y":
            browser.get(link.get_attribute('href'))
            vibor_deistv()
        else:
            continue


search()





