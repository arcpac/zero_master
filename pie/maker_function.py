def sentence_maker(phrase):
    interogatives = ("how", "what", "why")
    sentence = phrase.capitalize()

    if phrase.startswith(interogatives):
        return "{}?".format(sentence)
    else:
        return "{}?".format(sentence)
        
print(sentence_maker("how are you"))