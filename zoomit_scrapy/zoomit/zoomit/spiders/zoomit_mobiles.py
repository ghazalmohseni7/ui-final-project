import scrapy


class ZoomitMobilesSpider(scrapy.Spider):
    name = 'zoomit_mobiles'
    allowed_domains = ['www.zoomit.ir']
    start_urls = ['https://www.zoomit.ir/product/list/mobile/samsung/apple/']

    def parse(self, response):
        filename=open("zommit_phones.txt","a")
        links=response.xpath("//span[@class='productEnglishTitle']")
        for link in links:
            mobile_name=str(link.xpath("text()").get())
            if type(mobile_name)==str:
                mobile_names=mobile_name.lower()
                mobile=mobile_names.replace(" ","-")
                filename.writelines(mobile)
                filename.writelines('\n')
            # yield mobile

        pages_links = response.xpath("//nav[@class='pagingNav']").xpath("//a[@href='#']")
        pages=len(pages_links)-2

        for i in range(2,pages+1):
            page_number = f'page/{i}/'
            next_page_url = "https://www.zoomit.ir/product/list/mobile/samsung/apple/"+page_number
            yield scrapy.Request(url=next_page_url, callback=self.parse)