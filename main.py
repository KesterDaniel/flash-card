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

# Cards and buttons
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
right_btn = PhotoImage(file="./images/right.png")
wrong_btn = PhotoImage(file="./images/wrong.png")


# Button functions
def right_answer():
    french_words.remove(chosen_word)
    if len(french_words) > 0:
        game_on()
    else:
        card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        card_img = card.create_image(400, 263, image=front_card)
        text = card.create_text(400, 180, text="You have exhausted all flash cards", fill="black",
                                font=("Arial", 30, "bold"))
        card.grid(row=0, column=0, columnspan=2)


def wrong_answer():
    game_on()


# Flip Card
def flip_card(french_word_to_reveal, card_canvas, card_img, lang_text, word_text):
    row = data[data.French == french_word_to_reveal]
    card_canvas.itemconfig(card_img, image=back_card)
    card_canvas.itemconfig(lang_text, text="English")
    card_canvas.itemconfig(word_text, text=row["English"].item())


# Logic
def game_on():
    global chosen_word
    french_word = random.choice(french_words)
    chosen_word = french_word
    card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_img = card_canvas.create_image(400, 263, image=front_card)
    lang_text = card_canvas.create_text(400, 180, text="French", fill="black", font=("Arial", 30, "bold"))
    word_text = card_canvas.create_text(400, 300, text=french_word, fill="black", font=("Arial", 20, "bold"))
    card_canvas.grid(row=0, column=0, columnspan=2)
    right_button = Button(window, image=right_btn, borderwidth=0, command=right_answer)
    right_button.grid(row=1, column=0)
    wrong_button = Button(window, image=wrong_btn, borderwidth=0, command=wrong_answer)
    wrong_button.grid(row=1, column=1)
    window.after(5000, flip_card, french_word, card_canvas, card_img, lang_text, word_text)


game_on()

window.mainloop()
