import scrapy
import csv
import re


class CommentsSpider(scrapy.Spider):
    name = "comments"
    allowed_domains = ["www.mobile.ir"]
    start_urls = ["http://www.mobile.ir/"]

    def start_requests(self):
        urls = []
        self.start_urls = ['https://www.mobile.ir/']
        file = open('./comments_url.txt', 'r')
        while True:
            url = file.readline()
            if not url:
                break
            if url != '\n':
                # print("ok")
                new_url = str("https://www.mobile.ir" + url.replace('\n', ''))
                urls.append(new_url)
                # print(new_url)
        # print(urls)
        yield scrapy.Request(url=urls[0],callback=self.parse)
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ff = open("commentspage.html", "w", encoding="utf-8")
        # ff.write(str(response.body, encoding="utf-8"))
        result = response.xpath('//div[@class="comment "]/div[@class="padd"]/text()').getall()
        ff.write(',,,,,,,'.join(result))
        ff.close()
        url = response.url
        length_url = len(url)
        if "tablets" in url:
            filename = "comments-{}.txt".format(url[39:(length_url - 5)])
            csv_filename = "comments-{}.csv".format(url[39:(length_url - 5)])
        elif "phones" in url:
            filename = "comments-{}.txt".format(url[38:(length_url - 5)])
            csv_filename = "comments-{}.csv".format(url[38:(length_url - 5)])
        print("NNNNNNNNNNNNNNNNNNN", filename)
        print("urlsssssssssssss", url)
        f = open(filename, "a", encoding="utf-8-sig")
        comments = response.xpath('//div[@class="comment "]/div[@class="padd"]').getall()
        # print("//////////////////////////////")
        # print(type(comments))
        # for x in comments:
        #   print(x)
        #   print("*****************************")
        f.write(',,,,,,, '.join(comments))
        f.close()
        # comments=list(map(lambda x: x.replace("\r\n", ""), comments))
        # comments = list(map(lambda x: x.replace("<br>", ""), comments))
        # with open('hole1.csv', 'a', newline='') as csvfile:
        #   # Create a writer object
        #   writer = csv.writer(csvfile)

        #   # Write each element of the list to a separate row
        #   for item in comments:
        #       print("items : ",item)
        #       pattern = re.compile(r'<.*?>')
        #       text_content = re.sub(pattern, '', item)
        #       print("after re leve : ",text_content)
        #       print("///////",[text_content])
        #       string=[text_content]
        #       print("encdoe utf-8 : ",string.encode('utf-8'))
        #       writer.writerow([text_content])
        for item in comments:
            print("items : ", item)
            # pattern = re.compile(r'<.*?>')
            pattern = re.compile(r'<.*?>|[\r\n]')
            text_content = re.sub(pattern, '', item)
            print("after re leve : ", text_content)
            print("///////", [text_content])
            string = [text_content]
            print("encdoe utf-8 : ", string.encode('utf-8'))
            print("encode  utf-8-sig ", string.encode('utf-8-sig'))
            print("//////////////////////////////")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
