from mongoengine import *
class GptResponse(DynamicDocument):
    comment=StringField(max_length=1000000)
    apple=StringField(max_length=15)
    samsung=StringField(max_length=15)
    token=StringField(max_length=200)
