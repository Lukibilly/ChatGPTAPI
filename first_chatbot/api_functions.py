import datetime
import openai
import pinecone
import os
import json

openai.api_key = os.getenv('OPENAI_API_KEY')
pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment="us-west1-gcp"
)
if "chatbot1" not in pinecone.list_indexes():
    pinecone.create_index('chatbot1', 1536)
database = pinecone.Index('chatbot1')


def init_params(
    model = "gpt-3.5-turbo",
    temperature = 0.7,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0
):
    """ Default parameters for openai API"""
    openai_params = {}
    openai_params['model'] = model
    openai_params['temperature'] = temperature
    openai_params['max_tokens'] = max_tokens
    openai_params['top_p'] = top_p
    openai_params['frequency_penalty'] = frequency_penalty
    openai_params['presence_penalty'] = presence_penalty
    return openai_params
    
def get_chat_completion(params, messages):
    """ GET Chat Answer from openai API"""
    response = openai.ChatCompletion.create(
        model = params['model'],
        messages = messages,
        max_tokens = params['max_tokens'],
        temperature = params['temperature'],
        top_p = params['top_p']
    )

    return response

def get_code_completion(params, prompt):
    """ GET Code from openai API"""
    response = openai.Completion.create(
        model = params['model'],
        prompt = prompt,
        max_tokens = params['max_tokens'],
        temperature = params['temperature'],
        top_p = params['top_p'],
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
    )

    return response

def message_to_embeddingvector(message, engine='text-embedding-ada-002'):
    """ GET Embedding vector from openai API"""
    return openai.Embedding.create(input=message, engine=engine)['data'][0]['embedding'] #Returns normal list

