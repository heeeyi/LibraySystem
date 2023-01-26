from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('1750 * 1000')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)

window.mainloop()
    
