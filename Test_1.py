from googletrans import Translator

trans = Translator()
res = trans.translate("dog", dest="ru" )
print(res.text)