import random
import time
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)

# Data Arrangement
data = pd.read_csv("./data/french_words.csv")
dictionary_list = [{row["French"]: row["English"]} for (index, row) in data.iterrows()]
french_words = data["French"].to_list()

back_card = PhotoImage(file="./images/card_back.png")
right_btn = PhotoImage(file="./images/right.png")
wrong_btn = PhotoImage(file="./images/wrong.png")




# Change screens
def flip_card(french_word):
    row = data[data.French == french_word]
    card_canvas.itemconfig(card_img, image=back_card)
    image_button = Button(window, image=right_btn, borderwidth=0)
    image_button.grid(row=1, column=0)
    image_button = Button(window, image=wrong_btn, borderwidth=0)
    image_button.grid(row=1, column=1)
    card_canvas.itemconfig(lang_text, text="English")
    card_canvas.itemconfig(word_text, text=row["English"].item())


# Logic
game_on = True
while game_on:
    french_word = random.choice(french_words)
    card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    front_card = PhotoImage(file="./images/card_front.png")
    card_img = card_canvas.create_image(400, 263, image=front_card)
    lang_text = card_canvas.create_text(400, 180, text="French", fill="black", font=("Arial", 30, "bold"))
    word_text = card_canvas.create_text(400, 300, text=french_word, fill="black", font=("Arial", 20, "bold"))
    card_canvas.grid(row=0, column=0, columnspan=2)
    window.after(5000, flip_card, french_word)
    
    game_on = False










# UI setup



window.mainloop()

