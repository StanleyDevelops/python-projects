import json

filename = "ToDoList.json"

def load_data():
    try:
        with open(filename, "r") as file: 
            return json.load(file)               # if created already, loads file
    except (FileNotFoundError, json.decoder.JSONDecodeError):     
        return []          # return empty json with list for the first time


def save_data(data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent= 4)
    except IOError:
        print("Error: File couldn't be saved!")
