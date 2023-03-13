from helper_functions import open_file

def init_chat_messages(type = "assistant", init_message = None):
    messages = []

    if type == "custom":
        if init_message == None: raise ValueError("Custom message to be initialized didn't receive init_message!")
        add_chat_message(messages, "system", init_message)
    
    add_chat_message(messages, "system", get_bot_blueprint(type))
    
    return messages

def add_chat_message(messages, role, content):
    messages.append({"role" : role, "content" : content})

def add_chat_messages(messages, roles, contents):
    for (role, content) in zip(roles, contents):
        add_chat_message(messages, role, content)

def get_bot_blueprint(filename, filepath = "first_chatbot\\init_content\\"):
    finalpath = filepath + filename + ".txt"
    fileinfo = open_file(finalpath)
    return fileinfo