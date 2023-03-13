import os
import datetime
import json

def timestamp_to_datetime(time):
    return datetime.datetime.fromtimestamp(time).strftime("%A, %B %d, %Y at %I:%M%p %Z")

def clear_console():    
    os.system('cls' if os.name == 'nt' else 'clear')

def open_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def save_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(filepath, content):
    with open(filepath, 'w') as file:
        json.dump(content, file)
