import scrapy


class MobilesSpider(scrapy.Spider):
    name = "mobiles"
    allowed_domains = ["www.mobile.ir"]
    start_urls = ["https://www.mobile.ir/brands/7-apple.aspx"]

    def parse(self, response):
        filename = open("comments_url.txt", 'w')
        links = response.xpath("//div[@class='brandmodels']/a")

        for index, link in enumerate(links):
            phone_link = link.xpath('@href').extract()
            args = (index, phone_link)
            print('The link %d pointing to url %s a' % args)
            specification_to_comments = str(phone_link[0].replace('specifications', 'comments'))
            print(type(specification_to_comments))
            print('the url of comments is {}'.format(specification_to_comments))
            print("__________________________________________________________________")
            # filename.writelines(str(index))
            filename.writelines(specification_to_comments)
            filename.writelines('\n')
        filename.close()