import time
import openai
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('OPENAI_API_KEY')
openai.api_key = key


def main():
    while True:
        new_message = input('\nUSER: ')
        timestamp = time()

if __name__ == 'main':
    main()