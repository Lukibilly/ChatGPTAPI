import time
from api_functions import *
from bot_functions import *
from helper_functions import *


def main():
    clear_console()
    params = init_params(max_tokens=1000)
    type="sentiment"
    messages = init_chat_messages(type)


    while True:
        new_message = input('\nUSER: ')

        # Check if reset needed
        if(new_message == "reset"):
            messages = init_chat_messages(type)
            clear_console()
            continue

        # Get answer from openai API
        add_chat_message(messages, "user", new_message)        
        answer = get_chat_completion(params, messages)
        answer_content = answer['choices'][0]['message']['content']
        print("\nCHATBOT: ",answer_content)

        # Add answer to messages
        add_chat_message(messages, "system", answer_content)

if __name__ == '__main__':
    main()