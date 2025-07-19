import json 

def load(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        with open(file_name, "w") as file:
            json.dump([], file)
        return []

def save(file_name, lst):
    with open(file_name, "w") as file:
        return json.dump(lst, file, indent=4)


def menu(habar, diapazon):

    while True:
        try:
            tanlov = int(input(habar))
            assert tanlov in diapazon
            return tanlov
        except:
            print("Xato. Qayta kiriting")