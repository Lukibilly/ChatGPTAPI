import datetime
import openai
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('OPENAI_API_KEY')
openai.api_key = key

def message_embedding(message, engine='text-embedding-ada-002'):
    return openai.Embedding.create(input=message, engine=engine)['data'][0]['embedding'] #Returns normal list

def timestamp_to_datetime(time):
    return datetime.datetime.fromtimestamp(time).strftime("%A, %B %d, %Y at %I:%M%p %Z")
