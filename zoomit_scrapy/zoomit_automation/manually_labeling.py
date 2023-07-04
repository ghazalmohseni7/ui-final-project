import pandas as pd
from mongoengine import *
from models import GptResponse
import json
connection=connect("gpt")

results=json.loads(GptResponse.objects().to_json())
count=len(results)
samusng_manually=[]
apple_maually=[]
comment=[]
apple=[]
samsung=[]
token=[]
df = pd.DataFrame()
for record in results:
    comment.append(record["comment"])
    apple.append(record["apple"])
    samsung.append(record["samsung"])
    token.append(record["token"])
    samusng_manually.append("")
    apple_maually.append("")
    # input()
    print(record["comment"])
    print("/"*20)
    print("/"*20)
    print("/"*20)


print(len(comment))
print(len(samsung))
print(len(apple))
print(len(token))
print(len(samusng_manually))
print(len(apple_maually))
data={"comment" :comment,
      "samsung":samsung,
      "apple":apple,
      "token":token,
      "samsung/manually":samusng_manually,
     "apple/manually": apple_maually}

df = pd.DataFrame(data)
df.to_csv("C:/Users/ghazal/Desktop/automation/zoomit.csv",index=False)

# samsung/manually
# apple/manually