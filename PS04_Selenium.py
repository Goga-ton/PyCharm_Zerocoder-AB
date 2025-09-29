# Открытие страниц и их скриншот
from selenium import webdriver

import time

browser = webdriver.Firefox()
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("Hoome.png")
time.sleep(4)
browser.get("https://en.wikipedia.org/wiki/Selenium")
browser.save_screenshot("Selenium.png")
time.sleep(4)
browser.refresh()
browser.quit()


# Вводим в поисковую строку запрос и открываем ссылку на станице результатов поиска

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Кошка")

assert "Кошка — Википедия" in browser.title
time.sleep(2)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()
time.sleep(5)

browser.quit()


# выбирает абзатцы и выводит их по интер и переходит по рандомным ссылкам

from selenium import webdriver
from selenium.webdriver.common.by import By
import random

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Солнечная_система")

# выбирает абзадцы и выводит их по интер, (если блок стр.10-14 разремлен тогда блок стр.17-27 должен быть заремлен и наоборот)
# parags = browser.find_elements(By.TAG_NAME, "p")
#
# for prg in parags:
#     print(prg.text)
#     input()

# переходит по рандомным ссылкам (если блОк стр.17-27 разремлен тогда БЛОК стр.10-14 должен быть заремлен и наоборот)
stat = []
for elm in browser.find_elements(By.TAG_NAME, "div"):
    cl = elm.get_attribute("class")
    if cl =="hatnote navigation-not-searchable ts-main":
        stat.append(elm)

print(stat)

stat = random.choice(stat)
link = stat.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)