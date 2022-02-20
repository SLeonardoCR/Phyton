import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def iterate(word):
    iterate = data[word]
    for item in iterate:
        print("  %s" % item)
    return ""

def search(word):
    word = word.lower()
    wordt = word.title()
    wordu = word.upper()
    if word in data:
        iterate(word)
        return ""
    elif word=="-exit":
        print("---Saliendo---")
        exit()
    elif (get_close_matches(wordt, data.keys())[0]) == word.title():
        iterate(wordt)
        return ""
    elif (get_close_matches(wordu, data.keys())[0]) == word.upper():
        iterate(wordu)
        return ""
    elif len(get_close_matches(word, data.keys())) > 0:
        UserInput = input("-----\n-Tal vez te refieres a %s [Y/N]-  " % get_close_matches(word, data.keys())[0])
        if UserInput.lower() == "y":
            iterate(get_close_matches(word, data.keys())[0])
            return ""
        elif UserInput.lower() == "n":
            return "---No se encontró ninguna palabra---"
        else:
            return "---Entrada -%s- no conocida---" % UserInput
    else:
        return "---No se encontró ninguna palabra---"

UserInput = input("---HOLA! Ingresa una palabra a buscar---\n\n\t")

while True:
    print(search(UserInput))
    UserInput = input("-----\n\t")
