# Welcome to Creacher Keeper
# Python 3 code

from tkinter import *
import tkinter.messagebox
import time
import os

def mainScreen():
    # Window config options
    ms = Tk()
    ms.title("Creature Keeper")
    ms.config(bg="grey")
    ms.geometry("500x750")
    ms.resizable(width=False, height=False)
    ms.pack_propagate(0)
    
    # Placement of items in window
    tLabel = Label(ms, text="Creature Keeper | Dev Edition", font=("Gill Sans", 28), bg="grey")
    tLabel.place(x=250 , y=25, anchor="center")

    frame2 = [PhotoImage(file='images/ball-1.gif', format = 'gif -index %i' %(i)) for i in range(0, 100)]
    
    def update(ind):
        frame = frame2[ind]
        ind += 1
        img.configure(image=frame)
        root.after(100, update, ind)

    img = Label(ms)
    img.place(x=250, y=250, anchor="center")

    ms.after(0, update, 0)
    ms.mainloop()

mainScreen()
