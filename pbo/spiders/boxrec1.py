import scrapy
import time
import random

class Boxrec1Spider(scrapy.Spider):
    name = "boxrec1"

    def start_requests(self):
        urls = [
            'https://boxrec.com/',
            'https://boxrec.com/en/ratings',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        b_url = "https://boxrec.com/en/ratings"
        url_p="https://boxrec.com"
        for page in range(0, 24500, 50):
            r_url = f"{b_url}?offset={page}"
            table_data = response.xpath("//table[@class='dataTable']")
            profile_links = table_data.xpath("//a[@class='personLink']/@href").getall()
            for i in profile_links:
                pf = url_p + i
                yield scrapy.Request(url=pf, callback=self.parse_add_page)
                time.sleep(random.randint(1,6))
            yield scrapy.Request(url=r_url, callback=self.parse)

    def parse_add_page(self, response):

        yield {
            
            "Name": response.xpath("normalize-space(//td[@class='defaultTitleAlign']/h1)").get(),
            "picture_link": response.css("img.photoBorder ::attr(src)").get(),
            "Wikipedia_Link":response.xpath("(//a[@rel='nofollow'])[1]/@href").get(),
            "division": response.xpath("normalize-space(//td[@class='rowLabel'][contains(b, 'division')]/following-sibling::td)").get(),
            "rating": response.xpath("count(//tr[td[@class='rowLabel'][contains(b, 'rating')]]//i)").get(),
            "bouts": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'bouts')]]/td[2])").get(),
            "rounds": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'rounds')]]/td[2])").get(),
            "KOs": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'KOs')]]/td[2])").get(),
            "Career": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'career')]]/td[2])").get(),
            "Debut": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'debut')]]/td[2])").get(),
            "vada": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'vada')]]/td[2])").get(),
            "titles": response.xpath("//tr[td[@class='rowLabel'][contains(b, 'titles')]]/td[2]//a/text()").get(),
            "ID": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'ID#')]]/td[2])").get(),
            "Birth Name": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'birth name')]]/td[2])").get(),
            "sex": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'sex')]]/td[2])").get(),
            "Alias": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'alias')]]/td[2])").get(),
            "Age": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'age')]]/td[2])").get(),
            "Nationality": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'nationality')]]/td[2])").get(),
            "Stance": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'stance')]]/td[2])").get(),
            "Height": response.xpath("//tr[td[@class='rowLabel'][contains(b, 'height')]]/td[2]/text()").get(),
            "Reach": response.xpath("//tr[td[@class='rowLabel'][contains(b, 'reach')]]/td[2]/text()").get(),
            "Residence": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'residence')]]/td[2])").get(),
            "Birth Place": response.xpath("normalize-space(//tr[td[@class='rowLabel'][contains(b, 'birth place')]]/td[2])").get(),
            "Win": response.css(".bgW ::text").get(),
            "Lose": response.css(".bgL ::text").get(),
            "Draw": response.css(".bgD ::text").get(),
        }

