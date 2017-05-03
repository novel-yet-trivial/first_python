#!/usr/bin/env python3

# Welcome to Creature Keeper
# Python 3 code

import tkinter as tk
from image_label import ImageLabel
import tkinter.messagebox
import time
import os

def mainScreen():
    # Window config options
    ms = tk.Tk()
    ms.title("Creature Keeper")
    ms.config(bg="grey")
    ms.geometry("500x750")
    ms.resizable(width=False, height=False)
    ms.pack_propagate(0)

    # Placement of items in window
    tLabel = tk.Label(ms, text="Creature Keeper | Dev Edition", font=("Gill Sans", 28), bg="grey")
    tLabel.place(x=250 , y=25, anchor="center")

    img = ImageLabel(ms)
    img.load('images/ball-1.gif')
    img.place(x=250, y=250, anchor="center")

    ms.mainloop()

mainScreen()
