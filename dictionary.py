# create a dictionary

Language={
    "bonjour":"hello",
    "merci":"thank you",
    "amour":"love",
    "chat":"cat",
    "chein":"dog",
    "maison":"house",
    "voiture":"car",
    "ecole":"school",
    "livre":"book",
    "arbree":"tree",
    "fleur":"flower",
    "oiseau":"bird",
    "soleil":"sun",
    "lune":"moon",
    "mer":"sea",
    }

def search_word(word):
    word = word.lower() # convert input to lowercase to make it case-insensitive
    if word in Language:
        return Language[word]
    else:
        return "word not found in dictionary"


print(search_word("chat"))