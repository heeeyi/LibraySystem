#Page of membership update main page:
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Membership Update")
window.geometry("600x500")

top_frame = Frame(window, width = 500, height = 50)
top_frame.pack(side = TOP)

enter_label = Label(
    top_frame,
    text = "To Update Member, Please Enter Membership ID:",
    fg = "black", width = 65,
    font = 10, height = 4,
    bd = 3, bg = "turquoise").grid(
        row = 0, column = 0, padx = 1, pady = 1)

body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()

field = Label(
    body_frame, text = "Membership ID", font = 10,
    width = 20, height = 2, bd = 2, bg = "lightblue")
field.grid(row = 0, column = 0, padx = 5, pady = 40)
entry = Entry(body_frame)
entry.grid(row = 0, column = 1, padx = 5, pady = 40)

def retrieve_info():
    MemID = str(entry.get())
    print(MemID)
    #Supposed to be using this to retrieve in MySQL
    #Now just print out

def clicked():
    retrieve_info()

bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

update_btn = Button(
    bottom_frame, text = "Update Member",
    fg = "black", width = 25, height = 3,
    font = 10, bd = 3, bg = "turquoise", command = clicked).grid(
        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(
    bottom_frame, text = "Back to Membership Menu",
    fg = "black", width = 25, height = 3,
    font = 10, bd = 3, bg = "turquoise").grid(
        row = 0, column = 1, padx = 10, pady = 10)
window.mainloop()
