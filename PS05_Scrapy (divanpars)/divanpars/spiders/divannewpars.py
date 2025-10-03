import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k') # создает список всех найденых элекментов и записывает в divans
        for divan in divans:
            yield {'name' : divan.css('div.lsooF span::text').get(),
                   'prise' : divan.css('div.pY3d2 span::text').get(),
                   'url' : divan.css('a').attrib['href']
            }








