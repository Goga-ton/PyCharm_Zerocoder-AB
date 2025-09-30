import scrapy


class SvetLightSpider(scrapy.Spider):
    name = "svet_Light"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/svet"]

    def parse(self, response):
        svets = response.css('div.WdR1o')
        for svet in svets:
            yield {'name' : svet.css('div.lsooF span::text').get(),
                   'prise' : svet.css('div.pY3d2 span::text').get(),
                   'url' : svet.css('a').attrib['href']

            }
        next_pages = response.css('a.PaginationLink::attr(href)').getall()

        for next_page in next_pages:
            # Формируем полный URL
            next_page_url = response.urljoin(next_page)
            # Переходим на следующую страницу
            yield scrapy.Request(url=next_page_url, callback=self.parse)