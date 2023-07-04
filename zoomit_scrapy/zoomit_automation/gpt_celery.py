from celery import Celery
from gpt import *
from models import GptResponse
from mongoengine import connect
connection = connect("gpt")
# Create a Celery instance
app = Celery('myapp', broker='redis://localhost:6379/0', backend='mongodb://localhost:27017/gpt')
app.conf.broker_connection_retry_on_startup = True
# Set up the result backend using MongoEngine


# Define a task
@app.task(bind=True)
def labeling(self,comment):
    print("in labeliiiiinbgggggg")
    count=token_count(comment)
    if count <= 1900:
        print(
            "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< start calling api <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        response = analyze_sentiments(comment)
        final_response = convert_response1(response)
        print(final_response)
        if len(final_response.keys()) == 2:
            print("samsung is : ", final_response['Samsung'])
            print("apple is : ", final_response['Apple'])
            print(" bro usage ro negah kon")
            GptResponse.objects.create( comment=comment,apple=final_response['Apple'],samsung=final_response['Samsung'],token=str(count))
            print("start sleep")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            # time.sleep(60)
        else:
            print("#########################################################################")
            print(final_response.keys())
            print("#########################################################################")

        # df['token']=count
    else:
        GptResponse.objects.create(comment=comment, apple="", samsung="",token=str(count))
        # df['token']="no"



