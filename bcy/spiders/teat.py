import scrapy


class TeatSpider(scrapy.Spider):
    name = 'teat'
    # allowed_domains = ['teat.cn']
    start_urls = ['http://bcy.net/item/detail/6892354076277742600']

    def parse(self, response):
        print('+++++++++++++++++++++++++++')
        print(response.body)
        jpg=response.xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/article/div[1]/div[2]/div[2]/div/div/img')
        print(jpg)

        f=open('yyye.html','wb')
        f.write(response.body)

        # yield scrapy.Request(url='http://bcy.net/item/detail/689235407627774260')
