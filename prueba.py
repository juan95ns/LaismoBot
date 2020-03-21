import json

USERS = ["wenga28", "Juan9Pan"]
WORDS = ["la", "le", "lo"]

def check_name(author):
    found = False
    for item in USERS:
        if author == item:
            found = True

    return found

def check_laismo(msg):
    laismo = False
    for item in WORDS:
        if item in msg:
            laismo = True
    
    return laismo

def add_laismo(author):
    r_file = open("stats.json", "r")
    json_object = json.load(r_file)
    r_file.close()

    json_object[author] = json_object[author] + 1
    
    w_file = open("stats.json", "w")
    json.dump(json_object, w_file)
    w_file.close()
