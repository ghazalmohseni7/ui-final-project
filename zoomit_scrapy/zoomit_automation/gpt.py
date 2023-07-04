import tiktoken
import time
import openai

def token_count(text):
    print("counting tokens")

    encoding = tiktoken.get_encoding("cl100k_base")
      # encoding = tiktoken.get_encoding("p50k_base")
      # print(encoding)
      # print(encoding.encode(text))
      # print(type(encoding.encode(text)))
    num_tokens = len(encoding.encode(text))
    return num_tokens


def convert_response1(response):
    sentiment = response['choices'][0]["message"]['content']

    lines = sentiment.split('\n')
    dictionary = {}
    for line in lines:
        if "Target 1" in line or "Apple" in line:
            print("اپل موجوده ")
            if 'Neutral' in line:
                dictionary["Apple"] = "Neutral"
            if "Disagree" in line:
                dictionary["Apple"] = "Disagree"
            if "Agree" in line:
                dictionary["Apple"] = "Agree"
        else:
            print("اپل موجود نیست")
        if "Target 2" in line or "Samsung" in line:
            print("سامسونگ موجوده ")
            if 'Neutral' in line:
                dictionary["Samsung"] = "Neutral"
            if "Disagree" in line:
                dictionary["Samsung"] = "Disagree"
            if "Agree" in line:
                dictionary["Samsung"] = "Agree"
        else:
            print("سامسونگ موجود نیست")
    return dictionary



# Set up your OpenAI API key
openai.api_key = "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"
prompt='''Label the sentiment of the following text towards Apple and Samsung. Provide two labels, one for each target:

Target 1: Apple
Target 2: Samsung

For each target, choose one of the following labels:
- Agree: If the text expresses a positive sentiment towards the target.
- Disagree: If the text expresses a negative sentiment towards the target.
- Neutral: If the text does not express any sentiment towards the target.

Text : {}
'''

def analyze_sentiments(text):
    print("analyze_sentiments")
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ {"role": "user", "content": prompt.format(text)}, ]
    )
    time.sleep(60)
    return response
