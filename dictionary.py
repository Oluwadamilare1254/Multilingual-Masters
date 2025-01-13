import tkinter as tk
from tkinter import messagebox, StringVar
from tkinter import Tk, Entry, Button, Label

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
    "Namaste": "A traditional Indian greeting, often meaning 'I bow to the divine '.",
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

# Create the main window
root = Tk()
root.title("Language Selector App")
root.geometry('600x300')

# Result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Language selection menu
languages = ["French", "Indian", "Ogoni"]
language_var = StringVar()
language_var.set(languages[0])  # Default language is French
language_menu = tk.OptionMenu(root, language_var, *languages)
language_menu.pack(pady=10)

# French to English translation widgets
french_word_label = Label(root, text="Enter a French word:")
french_word_entry = Entry(root)
translate_button = Button(root, text="Translate", command=lambda: translate_word("French"))
french_word_label.pack_forget()
french_word_entry.pack_forget()
translate_button.pack_forget()

# Indian Dictionary search widgets
indian_word_label = Label(root, text="Enter an Indian word (e.g. Namaste):")
indian_word_entry = Entry(root)
search_button = Button(root, text="Search", command=lambda: search_word("Indian"))
indian_word_label.pack_forget()
indian_word_entry.pack_forget()
search_button.pack_forget()

# Ogoni Dictionary search widgets
ogoni_word_label = Label(root, text="Enter an Ogoni word (e.g. bari):")
ogoni_word_entry = Entry(root)
ogoni_search_button = Button(root, text="Search", command=lambda: search_word("Ogoni"))
ogoni_word_label.pack_forget()
ogoni_word_entry.pack_forget()
ogoni_search_button.pack_forget()

# Update the interface based on language selection
def update_interface():
    language = language_var.get()
    
    # Clear previous results and widgets
    result_label.config(text="")
    clear_widgets()
    
    # Show relevant widgets based on the selected language
    if language == "French":
        french_word_label.pack()
        french_word_entry.pack()
        translate_button.pack()
    elif language == "Indian":
        indian_word_label.pack()
        indian_word_entry.pack()
        search_button.pack()
    elif language == "Ogoni":
        ogoni_word_label.pack()
        ogoni_word_entry.pack()
        ogoni_search_button.pack()

# Clear widgets before showing relevant ones
def clear_widgets():
    french_word_label.pack_forget()
    french_word_entry.pack_forget()
    translate_button.pack_forget()
    
    indian_word_label.pack_forget()
    indian_word_entry.pack_forget()
    search_button.pack_forget()
    
    ogoni_word_label.pack_forget()
    ogoni_word_entry.pack_forget()
    ogoni_search_button.pack_forget()

# Translate French to English function
def translate_word(language):
    if language == "French":
        french_word = french_word_entry.get().lower()
        if french_word in french_to_english:
            result_label.config(text=f"{french_word} in English is {french_to_english[french_word]}")
        else:
            result_label.config(text="Word not found in French dictionary.")

# Search Indian Dictionary function
def search_word(language):
    if language == "Indian":
        indian_word = indian_word_entry.get().capitalize()
        if indian_word in indian_dict:
            result_label.config(text=f"{indian_word}: {indian_dict[indian_word]}")
        else:
            result_label.config(text="Word not found in Indian dictionary.")
    elif language == "Ogoni":
        ogoni_word = ogoni_word_entry.get().lower()
        if ogoni_word in ogoni_dictionary:
            result_label.config(text=f"{ogoni_word}: {ogoni_dictionary[ogoni_word]}")
        else:
            result_label.config(text="Word not found in Ogoni dictionary.")

# Bind the language selection change to update the interface
language_var.trace("w", lambda *args: update_interface())

# Initial call to set up the interface
update_interface()

# Run the application
root.mainloop()
