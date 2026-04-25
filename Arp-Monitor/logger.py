import json, os

FILE = "data.json"

def load():
    if not os.path.exists(FILE):
        return []
    try:
        return json.load(open(FILE, "r"))
    except:
        return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def write(entry):
    data = load()
    data.append(entry)
    save(data)

def log(msg):
    write({"type": "LOG", "message": msg})

def alert(msg):
    write({"type": "ALERT", "message": msg})
    write({"type": "LOG", "message": "ALERT: " + msg})

print("LOG YAZILIYOR")
