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




# UI setup
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
card_canvas.create_image(400, 263, image=front_card)
card_canvas.grid(row=0, column=0, columnspan=2)

right_btn = PhotoImage(file="./images/right.png")
image_button = Button(window, image=right_btn, borderwidth=0)
image_button.grid(row=1, column=0)

wrong_btn = PhotoImage(file="./images/wrong.png")
image_button = Button(window, image=wrong_btn, borderwidth=0)
image_button.grid(row=1, column=1)


window.mainloop()

