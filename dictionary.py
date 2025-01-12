import tkinter as tk
from tkinter import messagebox

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

# Function to handle translation
def translate_word():
    french_word = french_word_entry.get().lower()
    if french_word in french_to_english:
        english_word = french_to_english[french_word]
        result_label.config(text=f"The English translation of '{french_word}' is: {english_word}")
    else:
        messagebox.showerror("Error", "Word not found in the dictionary!")



# Set up the Tkinter window
root = tk.Tk()
root.title("French to English Translator")

# Create UI elements
french_word_label = tk.Label(root, text="Enter a French word:")
french_word_label.pack(pady=10)

french_word_entry = tk.Entry(root)
french_word_entry.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
