#Membership update entry page:
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Membership Update Entry")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(
    top_frame,
    text = "Please Enter Requested Information Below: ",
    fg = "black", width = 60,
    font = 8, height = 3,
    bd = 3, bg = "turquoise").grid(
        row = 0, column = 0, padx = 1, pady = 1)

def fill_default():
    MemID = "AAA"
    Name = "XiaoMing"
    Faculty = "SoC"
    Phone = "12345678"
    Email = "happy@gmail.com"
    return (MemID, Name, Faculty, Phone, Email)
#This supposed to be extracting from MySQL
#Now just use a proxy

#Create the middle frame
body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()
default = fill_default()

field1 = Label(body_frame, text = "Membership ID",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field1.grid(row = 0, column = 0, padx = 5, pady = 5)
entry1 = Entry(body_frame)
entry1.insert(END, default[0])
#This is how you insert default values (original values) into Entry
entry1.grid(row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Name",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field2.grid(row = 1, column = 0, padx = 5, pady = 5)
entry2 = Entry(body_frame)
entry2.insert(END, default[1])
entry2.grid(row = 1, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "Faculty",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field3.grid(row = 2, column = 0, padx = 5, pady = 5)
entry3 = Entry(body_frame)
entry3.insert(END, default[2])
entry3.grid(row = 2, column = 1, padx = 5, pady = 10)

field4 = Label(body_frame, text = "Phone Number",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field4.grid(row = 3, column = 0, padx = 5, pady = 5)
entry4 = Entry(body_frame)
entry4.insert(END, default[3])
entry4.grid(row = 3, column = 1, padx = 5, pady = 10)

field5 = Label(body_frame, text = "Email Address",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field5.grid(row = 4, column = 0, padx = 5, pady = 5)
entry5 = Entry(body_frame)
entry5.insert(END, default[4])
entry5.grid(row = 4, column = 1, padx = 5, pady = 10)

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

SUCCESS_STATE = True

def return_info():
    MemID = str(entry1.get())
    Name = str(entry2.get())
    Faculty = str(entry3.get())
    Phone = str(entry4.get())
    Email = str(entry5.get())
    return (MemID, Name, Faculty, Phone, Email)
    #Supposed to be adding these to MySQL
    #Now just print out in the shell

def messageWindow1():
    win2 = Toplevel()
    win2.title("Success")
    win2.geometry("400x200")
    message = "Membership successfully updated."
        
    top_frame = Frame(win2, width = 400, height = 100)
    top_frame.pack(side = TOP)
    Label(win2, text = message).pack()

    bottom_frame = Frame(win2, width = 400, height = 100)
    bottom_frame.pack(side = BOTTOM)
    Button(
        bottom_frame, text = "Create another member").grid(
            row = 0, column = 0, padx = 5, pady = 5)
    Button(
        bottom_frame, text = "Back to Update Function",
        command = win2.destroy).grid(
            row = 0, column = 1, padx = 5, pady = 5)
        
def messageWindow2():
    win2 = Toplevel()
    win2.title("Error")
    win2.geometry("400x200")
    message = "Missing or Incomplete fields"
    Label(win2, text = message).pack(side = TOP)
    Button(
        win2, text = "Back to Update Function",
        command = win2.destroy).pack(
            side = BOTTOM)

def clicked():
    #Need to invoke a new window
    win = Toplevel()
    win.title("Please confirm details to be correct")
    win.geometry("400x200")

    top_frame = Frame(win, width = 400, height = 150)
    top_frame.pack(side = TOP)

    entry_text = return_info()
        
    message1 = "Member ID: " + entry_text[0]
    message2 = "Name: " + entry_text[1]
    message3 = "Faculty: " + entry_text[2]
    message4 = "Phone Number: " + entry_text[3]
    message5 = "Email Address: " + entry_text[4]
    Label(top_frame, text = message1).pack()
    Label(top_frame, text = message2).pack()
    Label(top_frame, text = message3).pack()
    Label(top_frame, text = message4).pack()
    Label(top_frame, text = message5).pack()

    def clicked2():
        #Need to close the last window, while opening a new window
        win.destroy()
        if SUCCESS_STATE:
            print(entry_text)
            #Later this supposed to be adding to MySQL
            messageWindow1()
        else:
            messageWindow2()

    bottom_frame = Frame(win, width = 400, height = 50)
    bottom_frame.pack(side = BOTTOM)
    Button(
        bottom_frame,
        text = "Confirm\nUpdate",
        command = clicked2).grid(
        row = 0, column = 0, padx = 5, pady = 5)
    Button(
        bottom_frame,
        text = "Back to Update\nFunction",
        command = win.destroy).grid(
        row = 0, column = 1, padx = 5, pady = 5)

update_btn = Button(
    bottom_frame, text = "Update Member",
    fg = "black", width = 25, height = 3,
    font = 10, bd = 3, bg = "turquoise",
    command = clicked).grid(
        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(
    bottom_frame, text = "Back to Membership Menu",
    fg = "black", width = 25, height = 3,
    font = 10, bd = 3, bg = "turquoise").grid(
        row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()
