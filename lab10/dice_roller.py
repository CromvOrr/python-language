# 10.1
import tkinter as tk
from PIL import Image, ImageTk
import random


def load_images():
    images = []
    for i in range(1, 7):
        image = Image.open(f"rolls/roll_{i}.png").resize((100, 100))
        images.append(ImageTk.PhotoImage(image))
    return images


def roll_dice(label, images):
    result = random.randint(0, 5)
    label.config(image=images[result])


window = tk.Tk()
window.title("Dice Roller")
window.geometry("300x300")
window.configure(bg="white")

dice_images = load_images()

title_label = tk.Label(window, text="Roll the Dice!", font=("Roboto", 16), bg="white")
title_label.pack(pady=10)

roll_button = tk.Button(window, text="Roll", font=("Roboto", 12), bg="pink",
                        command=lambda: roll_dice(dice_label, dice_images))
roll_button.pack(pady=10)

dice_label = tk.Label(window, bg="white")
dice_label.pack(pady=20)

window.mainloop()
