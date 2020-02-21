import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes and N if no: " %get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "This word does not exist"
        else:
            return "We did not understand your entry"

    else:
        return "This word does not exist"

word = input("Enter Word: ")


print(translate(word))