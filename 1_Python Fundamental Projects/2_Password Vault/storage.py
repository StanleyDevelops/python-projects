import json

filename = "Password_storage.json"

def load_data():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_data(data):
    try:
        with open(filename, "w") as file:
            return json.dump(data, file, indent=4)
    except IOError:
        return f"File Couldn't be saved."