import tkinter as tk
from tkinter import messagebox
import json

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

# Functions for dictionary actions
def translate_word():
    french_word = french_word_entry.get().lower()
    if french_word in french_to_english:
        english_word = french_to_english[french_word]
        result_label.config(text=f"The English translation of '{french_word}' is: {english_word}")
    else:
        messagebox.showerror("Error", "Word not found in the dictionary!")

# Function to search the Indian dictionary (case-insensitive)
def search_word(word):
    word = word.capitalize()  # Capitalize to match the dictionary keys
    if word in indian_dict:
        return indian_dict[word]
    else:
        return "Sorry, the word is not found in the dictionary."

# Function to handle language selection
def change_language(language):
    global current_language
    current_language = language
    if current_language == "French":
        french_word_label.pack(pady=10)
        french_word_entry.pack(pady=10)
        translate_button.pack(pady=10)
        result_label.pack(pady=10)
        indian_word_label.pack_forget()
        indian_word_entry.pack_forget()
        search_button.pack_forget()
    elif current_language == "Indian":
        indian_word_label.pack(pady=10)
        indian_word_entry.pack(pady=10)
        search_button.pack(pady=10)
        result_label.pack(pady=10)
        french_word_label.pack_forget()
        french_word_entry.pack_forget()
        translate_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Language Selector App")

# Language selection menu
languages = ["French", "Indian"]
language_var = tk.StringVar()
language_var.set(languages[0])  # Default language is French
language_menu = tk.OptionMenu(root, language_var, *languages, command=change_language)
language_menu.pack(pady=10)

# French to English translation widgets
french_word_label = tk.Label(root, text="Enter a French word:")
french_word_entry = tk.Entry(root)
translate_button = tk.Button(root, text="Translate", command=translate_word)
result_label = tk.Label(root, text="", font=("Helvetica", 12))

# Indian Dictionary search widgets
indian_word_label = tk.Label(root, text="Enter an Indian word (e.g. Namaste):")
indian_word_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=lambda: result_label.config(text=search_word(indian_word_entry.get())))

# Initial language set to French
current_language = "French"
change_language(current_language)

# Run the Tkinter event loop
root.mainloop()
