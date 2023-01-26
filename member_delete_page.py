#Page of membership deletion:
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Membership Deletion")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
    bg = "grey", bd = 0)
top_frame.pack(side = TOP)
    
#Create a label inside this frame
enter_label = Label(top_frame,
                    text = "To Delete Member, Please enter Membership ID:",
                    fg = "black", width = 65,
                    font = 10, height = 4,
                    bd = 3, bg = "turquoise").grid(
                        row = 0, column = 0, padx = 1, pady = 1)

#Create the middle frame
body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()

field = Label(body_frame, text = "Membership ID", font = 10, width = 20,
    height = 2, bd = 2, bg = "lightblue")
field.grid(row = 0, column = 0, padx = 5, pady = 40)
entry = Entry(body_frame)
entry.grid(row = 0, column = 1, padx = 5, pady = 40)

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

SUCCESS_STATE = True

def retrieve_info():
    MemID = str(entry.get())
    #Supposed to be using this to retrieve in MySQL
    #Now just use a proxy
    Name = "XiaoMing"
    Faculty = "SoC"
    Phone = "12345678"
    Email = "happy@gmail.com"
    return (MemID, Name, Faculty, Phone, Email)

def messageWindow1():
    win2 = Toplevel()
    win2.title("Success")
    win2.geometry("400x200")
    message = "Membership successfully deleted."
    Label(win2, text = message).pack(side = TOP)
    Button(
        win2, text = "Back to Delete Function", command = win2.destroy).pack(
            side = BOTTOM)
def messageWindow2():
    win2 = Toplevel()
    win2.title("Error")
    win2.geometry("400x200")
    message = "Member already exist;\nMissing or Incomplete fields"
    Label(win2, text = message).pack(side = TOP)
    Button(
        win2, text = "Back to Delete Function", command = win2.destroy).pack(
            side = BOTTOM)

def clicked():
    #Need to invoke a new window
    win = Toplevel()
    win.title("Please Confirm Details to be Correct")
    win.geometry("400x200")
        
    top_frame = Frame(win, width = 400, height = 150)
    top_frame.pack(side = TOP)

    entry_text = retrieve_info()
    
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
            retrieve_info()
            messageWindow1()
        else:
            messageWindow2()
                
    bottom_frame = Frame(win, width = 400, height = 50)
    bottom_frame.pack(side = BOTTOM)
    Button(
        bottom_frame,
        text = "Confirm\nWithdrawal",
        command = clicked2).grid(
        row = 0, column = 0, padx = 5, pady = 5)
    Button(
        bottom_frame,
        text = "Back to Withdrawal\nFunction",
        command = win.destroy).grid(
        row = 0, column = 1, padx = 5, pady = 5)
            
delete_btn = Button(bottom_frame, text = "Delete Member",
                    fg = "black", width = 25, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise", command = clicked).grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame, text = "Back to Membership Menu",
    fg = "black", width = 25, height = 3,
    font = 10, bd = 3,
    bg = "turquoise").grid(
    row = 0, column = 1, padx = 10, pady = 10)
                      
window.mainloop()

