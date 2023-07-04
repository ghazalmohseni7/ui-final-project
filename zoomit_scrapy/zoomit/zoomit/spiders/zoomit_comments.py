import scrapy
import re

class ZoomitCommentsSpider(scrapy.Spider):
    name = 'zoomit_comments'
    allowed_domains = ['www.zoomit.ir']
    start_urls = ['http://www.zoomit.ir/']

    def start_requests(self):
        urls = []
        self.start_urls = ['http://www.zoomit.ir/']
        file=open('C:/Users/ghazal/Desktop/zommit_scrapy/zoomit/zoomit/spiders/products.txt', 'r')
        while True:
            url = file.readline()
            if not url:
                break
            if url != '\n':
                print(url)
                new_url = str("https://www.zoomit.ir/product/" + url.replace('\n', '')+"/userreviews/")
                urls.append(new_url)
                # print(new_url)
                # print("////////////////////////////////////////////////////////////////////")
            yield scrapy.Request(url=urls[0], callback=self.parse)
            # for url in urls:
            #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # results = response.xpath("//p[@data-bind='html: body']")
        # results = response.xpath("//div[contains(@class, 'user-review__comment-text')]/p").getall()
        # p_tag = response.xpath('//p')
        # text = p_tag.extract_first()
        # match = re.search(r'data-org="([^"]+)"', text)
        # if match:
        #     org_text = match.group(1)
        #     print( {'org_text': org_text})
        # else:
        #     print({'org_text': None})
        # p_tags = response.css('div.user-review__comment-text p[data-bind="html: body"]')  # Select all the <p> tags inside the specified class
        # for p_tag in p_tags:
        #     print(p_tag)
        #     p_tag_text = p_tag.css('::text').get()  # Extract the text content of each <p> tag
        #     print(p_tag_text)
        print("gpt waaaaaay ")
        h1_text = response.css('p[data-bind="html: body"] ').extract()
        print(h1_text)
        print("h1")




        ul_element = response.xpath('//ul')  # Replace with the appropriate XPath to select the <ul> element
        p_elements = ul_element.xpath('.//p/text()').getall() # XPath to select all <p> elements within the <ul> element

        # Extract the text from each <p> element
        for p_element in p_elements:
            print(p_element)
            text = p_element.xpath('normalize-space()').get()
            print(text)

        print("gpt waaaaaay ")









        results=response.xpath("//div[@class='user-review__cooments']").css('p').css('::text').get()


        print("*" * 20)
        print(results)
        print("*" * 20)
        for result in results:
            print(result)
            print("*" * 20)
            text = result.css('p')
            print(text)
            print("*" * 20)
        # results=response.xpath("//div[@class='user-review__comment-text']")
        # for result in results:
        #     text =result.xpath("string()").get()
        #     print(text)
        # print("*"*20)
        # print(response.url)
        # print(result)
        # print("*" * 20)
