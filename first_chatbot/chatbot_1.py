import time
from custom_openai import *


def main():
    clear_console()
    params = init_params()
    type="assistant"
    messages = init_messages(type)

    while True:        
        new_message = input('\nUSER: ')
        # Check if reset needed
        if(new_message == "reset"):
            messages = init_messages(type)
            clear_console()
            continue
        add_message(messages, "user", new_message)

        answer = get_completion(params, messages)
        answer_content = answer['choices'][0]['message']['content']
        print("\nCHATBOT: ",answer_content)

        add_message(messages, "system", answer_content)

if __name__ == '__main__':
    main()