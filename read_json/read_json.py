import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Do you mean %s? Y or N?" % get_close_matches(word, data.keys())[0])
        if response == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "That doesn't exists."
    else:
        return "Word doesn't exists."
    
word = input("enter word: ")

result = translate(word)

# Display description
if len(result) > 1:
    for desc in result:
        print(desc)
else:
   print(result) 