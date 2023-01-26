#Page of membership creation
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Membership Creation")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                    bg = "grey",
                    bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "To Create Member,\nPlease Enter Requested Information Below: ",
        fg = "black",
        width = 60,
        font = 8,
        height = 3,
        bd = 3, 
        bg = "turquoise").grid(
            row = 0, column = 0,
            padx = 1, pady = 1)

#Create the middle frame
body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()

field1 = Label(body_frame, text = "Membership ID",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field1.grid(row = 0, column = 0, padx = 5, pady = 10)
entry1 = Entry(body_frame)
entry1.grid(row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Name",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field2.grid(row = 1, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame)
entry2.grid(row = 1, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "Faculty",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field3.grid(row = 2, column = 0, padx = 5, pady = 10)
entry3 = Entry(body_frame)
entry3.grid(row = 2, column = 1, padx = 5, pady = 10)

field4 = Label(body_frame, text = "Phone Number",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field4.grid(row = 3, column = 0, padx = 5, pady = 10)
entry4 = Entry(body_frame)
entry4.grid(row = 3, column = 1, padx = 5, pady = 10)

field5 = Label(body_frame, text = "Email Address",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field5.grid(row = 4, column = 0, padx = 5, pady = 10)
entry5 = Entry(body_frame)
entry5.grid(row = 4, column = 1, padx = 5, pady = 10)

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

SUCCESS_STATE = True

def retrieve_info():
    MemID = str(entry1.get())
    Name = str(entry2.get())
    Faculty = str(entry3.get())
    Phone = str(entry4.get())
    Email = str(entry5.get())
    print(MemID, Name, Faculty, Phone, Email)
    #Supposed to be adding these to MySQL
    #Now just print out in the shell

def messageWindow1():
    win = Toplevel() #Open another window on top of the current one
    win.geometry("300x200")
    win.title("Success")
    message = "ALS Membership Created."
    Label(win, text = message).pack(side = TOP, pady = 10)
    Button(win, text = "Back to Create Function",
            command = win.destroy).pack(side = BOTTOM, pady = 10)

def messageWindow2():
    win = Toplevel()
    win.geometry("300x200")
    win.title("Error")
    message = "Membership already exist; \n Missing or Incomplete fields"
    Label(win, text = message).pack(side = TOP, pady = 10)
    Button(win, text = "Back to Create Function",
            command = win.destroy).pack(side = BOTTOM, pady = 10)

def clicked():
    if SUCCESS_STATE:
        retrieve_info()
        messageWindow1()
    else:
        messageWindow2()

create_btn = Button(bottom_frame,
                    text = "Create Member",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise",
                    command = clicked).grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to Main Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)
    
window.mainloop()
