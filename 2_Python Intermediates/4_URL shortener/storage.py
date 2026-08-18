import json

filename = "urls.json"

def load_data():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
    
def save_data(data):
    try:
        with open(filename, "w") as file:
            json.dump(data,file, indent = 4)
    except IOError:
        print("Error: File couln't be saved!")

    
