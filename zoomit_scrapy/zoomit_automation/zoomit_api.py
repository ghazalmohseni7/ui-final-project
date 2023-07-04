import requests
import json
import re


# url = "https://www.zoomit.ir/product/xiaomi-redmi-note-9-pro/"
#
# response = requests.get(url)
#
# print(response.text)
# print("****************************************************")
# print("****************************************************")
# print("****************************************************")
# print("****************************************************")
# x=response.text
# print(type(x))
import re
def extract_sku_using_regex(url):
    print("extracting sku")
    response = requests.get(url)
    input_string=response.text
    pattern = r'"sku":"(\d+)"'
    match = re.search(pattern, input_string)
    if match:
        sku = match.group(1)
        return sku
    else:
        return None

# sku=extract_sku_using_regex("https://www.zoomit.ir/product/samsung-galaxy-a32-5g/")
# print(sku)
def get_comments_with_sku(sku):
    all_comments=[]
    print("getting comment with sku")
    url_with_sku = f"https://www.zoomit.ir/comment/product/get/{sku}/page/1/"

    sku_response= requests.get(url_with_sku)
    comments=json.loads(sku_response.text)
    # print(comments)
    each_comment=comments['comments']
    for comment in each_comment:
        print(comment)
        # print(type(comment))
        # print(comment['message'])
        # r'<.*?>|\[title\].*?\[/title\]|\[\*\].*?\[\/\*\]'
        updated_string = re.sub(r'\[.*?\]|<.*?>', ' ', comment['message'])
        updated_string = updated_string.replace(".", " ")
        print(updated_string)
        all_comments.append(updated_string)
        # now you can call api
        print("-------------------------------------------------------------------")
        print("-------------------------------------------------------------------")
        print("-------------------------------------------------------------------")
    return all_comments


# get_comments_with_sku(sku)