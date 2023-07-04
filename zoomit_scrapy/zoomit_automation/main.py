from zoomit_api import *
from gpt_celery import labeling

def main():
    file = open('C:/Users/ghazal/Desktop/automation/products.txt', 'r')
    while True:
        url = file.readline()
        if not url:
            break
        if url != '\n':

            new_url = str("https://www.zoomit.ir/product/" + url.replace('\n', '') + "/userreviews/")
            print(new_url)
            sku=extract_sku_using_regex(new_url)
            comments=get_comments_with_sku(sku)
            for comment in comments:
                labeling.delay(comment)


if __name__ == "__main__":
    main()