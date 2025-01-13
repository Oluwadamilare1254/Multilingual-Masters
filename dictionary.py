import tkinter as tk
from tkinter import StringVar, Tk, Entry, Button, Label

# French to English dictionary
french_to_english = {
    "bonjour": "hello",
    "merci": "thank you",
    "amour": "love",
    "maison": "house",
    "chat": "cat",
    "chien": "dog",
    "voiture": "car",
    "arbre": "tree",
    "fleur": "flower",
    "école": "school",
    "livre": "book",
    "voix": "voice",
    "porte": "door",
    "soleil": "sun",
    "lune": "moon",
    "mer": "sea",
    "montagne": "mountain",
    "rue": "street",
    "ciel": "sky",
    "ami": "friend"
}

# Indian dictionary
indian_dict = {
    "Namaste": "A traditional Indian greeting, often meaning 'I bow to the divine'.",
    "Atithi": "A Sanskrit word meaning 'guest', based on the belief that 'the guest is God'.",
    "Satyagraha": "A philosophy of non-violent resistance, famously associated with Mahatma Gandhi.",
    "Guru": "A spiritual teacher or mentor, especially in Indian religions like Hinduism, Buddhism, and Sikhism.",
    "Dharma": "A key concept in Indian religions, referring to duty, law, righteousness, or moral order.",
    "Karma": "The belief that one's actions (good or bad) determine future consequences, central to Hinduism, Buddhism, and Jainism.",
    "Yoga": "A spiritual, mental, and physical practice originating from India, aimed at achieving spiritual union and self-realization.",
    "Swaraj": "Self-rule or self-governance, famously advocated by Mahatma Gandhi in the Indian independence movement.",
    "Mahatma": "A title meaning 'great soul', most famously used for Mahatma Gandhi, a leader of India's independence movement.",
    "Pukka": "A word of Hindi origin meaning authentic, genuine, or of high quality. Used in British English as well.",
    "Bindi": "A decorative mark worn on the forehead, often associated with Hindu culture, representing the 'third eye'.",
    "Veda": "Ancient sacred texts of India, considered the foundation of Hindu religious knowledge and wisdom.",
    "Mandala": "A geometric figure representing the universe, used in Hinduism and Buddhism as a symbol of meditation and cosmic unity.",
    "Raga": "A traditional melodic framework in Indian classical music, each raga is associated with specific emotions and times of day.",
    "Sari": "A traditional Indian garment worn by women, usually consisting of a long piece of cloth draped elegantly around the body.",
    "Diwali": "A major Hindu festival known as the 'Festival of Lights', celebrating the victory of good over evil and light over darkness.",
    "Durga": "A Hindu goddess associated with strength, protection, and motherhood, often depicted riding a lion or tiger.",
    "Ayurveda": "An ancient system of natural healing and medicine that originated in India, focusing on balance in the body, mind, and spirit.",
    "Chai": "A popular Indian beverage made with tea, milk, sugar, and spices like cardamom, cinnamon, and ginger."
}

# Ogoni dictionary
ogoni_dictionary = {
    'bari': 'god',
    'kah-bay': 'hello',
    'mee keh': 'how are you',
    'meh-neh': 'fish',
    'soh-noh': 'cassava',
    'mii gbaa': 'i am fine',
    'taataa': 'three',
    'loo': 'yes',
    'kpeh neh': 'chicken',
    'tah eh neh': 'cow',
    'keh tah bah': 'your welcome',
    'loo kah bay': 'good morning',
    'tah keh': 'elder sibling',
    'soh koh': 'snake',
    'keh keh tah': 'younger sibling',
    'koh noh': 'yam',
    'nay neh': 'four',
    'keh neh keh': 'whats your name',
    'keh ngah': 'sweet',
    'mee mee ree': 'water'
}

# Spanish dictionary
spanish_dict = {
    "hola": "hello",
    "amor": "love",
    "mundo": "world",
    "casa": "house",
    "perro": "dog",
    "gato": "cat",
    "feliz": "happy",
    "triste": "sad",
    "gracias": "thank you",
    "libro": "book",
    "agua": "water",
    "sol": "sun"
}

# Create the main window
root = Tk()
root.title("Language Selector App")
root.geometry('600x300')

# Result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Language selection menu
languages = ["French", "Indian", "Ogoni", "Spanish"]
language_var = StringVar()
language_var.set(languages[0])  # Default language is French
language_menu = tk.OptionMenu(root, language_var, *languages)
language_menu.pack(pady=10)

# Entry widgets for each language
word_label = Label(root, text="")
word_entry = Entry(root)
search_button = Button(root, text="", command=lambda: search_word(language_var.get()))

# Update the interface based on language selection
def update_interface():
    language = language_var.get()
    
    # Clear previous results and widgets
    result_label.config(text="")
    word_label.pack_forget()
    word_entry.pack_forget()
    search_button.pack_forget()
    
    # Show relevant widgets based on the selected language
    if language == "French":
        word_label.config(text="Enter a French word:")
        search_button.config(text="Translate")
        word_label.pack()
        word_entry.pack()
        search_button.pack()
    elif language == "Indian":
        word_label.config(text="Enter an Indian word (e.g. Namaste):")
        search_button.config(text="Search")
        word_label.pack()
        word_entry.pack()
        search_button.pack()
    elif language == "Ogoni":
        word_label.config(text="Enter an Ogoni word (e.g. bari):")
        search_button.config(text="Search")
        word_label.pack()
        word_entry.pack()
        search_button.pack()
    elif language == "Spanish":
        word_label.config(text="Enter a Spanish word:")
        search_button.config(text="Translate")
        word_label.pack()
        word_entry.pack()
        search_button.pack()

# Search word function
def search_word(language):
    word = word_entry.get().lower()
    if language == "French":
        dictionary = french_to_english
        result = dictionary.get(word, "Word not found in French dictionary.")
        result_label.config(text=f"{word} in English is {result}")
    elif language == "Indian":
        dictionary = indian_dict
        result = dictionary.get(word.capitalize(), "Word not found in Indian dictionary.")
        result_label.config(text=f"{word.capitalize()}: {result}")
    elif language == "Ogoni":
        dictionary = ogoni_dictionary
        result = dictionary.get(word, "Word not found in Ogoni dictionary.")
        result_label.config(text=f"{word}: {result}")
    elif language == "Spanish":
        dictionary = spanish_dict
        result = dictionary.get(word, "Word not found in Spanish dictionary.")
        result_label.config(text=f"{word} in English is {result}")

# Bind the language selection change to update the interface
language_var.trace("w", lambda *args: update_interface())

# Initial call to set up the interface
update_interface()

# Run the application
root.mainloop()
