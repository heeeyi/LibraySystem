from tkinter import *
from tkinter import messagebox
import tkinter
import pymysql

#NOTICE: SIZE PARAMETERS MAY WORK DIFFERENTLY FOR WINDOW & MAC
#SO NOTE THE SIZE DIFFERENCE IN THE COMMENT

window = Tk()
window.title("Book Aquisition")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                bg = "grey",
                bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "For New Book Acquisition,\nPlease Enter Required Information Below:",
        fg = "black", 
        width = 65,
        font = 10, #WINDOWS: 8
        height = 4, #WINDOWS: 3
        bd = 3, 
        bg = "turquoise").grid(
            row = 0, column = 0,
            padx = 1, pady = 1)

#Create the middle frame
body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()

#FOR WINDOWS ALL THE pady = 5
field1 = Label(body_frame, text = "Accession Number",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 0, column = 0, padx = 5, pady = 10) 
entry1 = Entry(body_frame).grid(
    row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Title",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 1, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame).grid(
    row = 1, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "Authors",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 2, column = 0, padx = 5, pady = 10)
entry3 = Entry(body_frame).grid(
    row = 2, column = 1, padx = 5, pady = 10)

field4 = Label(body_frame, text = "ISBN",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 3, column = 0, padx = 5, pady = 10)
entry4 = Entry(body_frame).grid(
    row = 3, column = 1, padx = 5, pady = 10)

field5 = Label(body_frame, text = "Publisher",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 4, column = 0, padx = 5, pady = 10)
entry5 = Entry(body_frame).grid(
    row = 4, column = 1, padx = 5, pady = 10)

field6 = Label(body_frame, text = "Publication Year",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 5, column = 0, padx = 5, pady = 10)
entry6 = Entry(body_frame).grid(
    row = 5, column = 1, padx = 5, pady = 10)

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)


SUCCESS_STATE = False
#Now can arbitrarily vary this for testing
#Later use mySQL response to decide


def clicked():
    if SUCCESS_STATE:
        def messageWindow():
            win = Toplevel()
            win.title('Success')
            message = "New Book Added Into Library"
            Label(win, text=message).pack()
            Button(win, text='Back to Acquisition Function', command=win.destroy).pack()
        messageWindow()

    else:
        def messageWindow():
            win = Toplevel()
            win.title('Error')
            message = "Book already added; Duplicate, Missing or Incomplete fields."
            Label(win, text=message).pack()
            Button(win, text='Back to Acquisition Function', command=win.destroy).pack()
        messageWindow()


#FOR WINDOWS ALL pady = 1
create_btn = Button(bottom_frame,
                    text = "Add New Book",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise",
                    command = clicked).grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to Books Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)

    
window.mainloop()