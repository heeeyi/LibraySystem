#Page of book borrowing
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Book Borrowing")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                bg = "grey",
                bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "To Borrow a Book, Please Enter Information Below:",
        fg = "black",
        width = 65,
        font = 10,
        height = 4,
        bd = 3, 
        bg = "turquoise").grid(
            row = 0, column = 0,
            padx = 1, pady = 1)

#Create the middle frame
body_frame = Frame(window, width = 600, height = 300)
body_frame.pack()

field1 = Label(body_frame, text = "Accession Number",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field1.grid(row = 0, column = 0, padx = 5, pady = 10)
entry1 = Entry(body_frame)
entry1.grid(row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Membership ID",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field2.grid(row = 1, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame)
entry2.grid(row = 1, column = 1, padx = 5, pady = 10)

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

SUCCESS_STATE = True
ERROR1 = False
ERROR2 = False
ERROR3 = False
#Now can arbitrarily vary this for testing
#Later use mySQL response to decide

def retrieve_info():
    Accession_Number = str(entry1.get())
    Membership_ID = str(entry2.get())
    print(Accession_Number, Membership_ID)
    #Supposed to be adding these to MySQL
    #Now just print out in the shell


def successMessageWindow():
    win2 = Toplevel()
    win2.title("Success")
    win2.geometry("400x200")
    message = "Book Borrowing Successful."
    Label(win2, text = message).pack(side = TOP)
    Button(
        win2, text = "Back to Book Return Function", command = win2.destroy).pack(
            side = BOTTOM)

def error1_msg_window():
    win = Toplevel()
    win.title('Error')
    message = "Book currently on Loan until:\nDD/MM/YYYY"
    Label(win, text=message).pack()
    Button(win, text='Back to Borrow Function', command=win.destroy).pack()

def error2_msg_window():
    win = Toplevel()
    win.title('Error')
    message = "Member loan quota exceeded."
    Label(win, text=message).pack()
    Button(win, text='Back to Borrow Function', command=win.destroy).pack()

def error3_msg_window():
    win = Toplevel()
    win.title('Error')
    message = "Member has outstanding fines."
    Label(win, text=message).pack()
    Button(win, text='Back to Borrow Function', command=win.destroy).pack()

def clicked():
    #Need to invoke a new window
    win = Toplevel()
    win.title("Confirm Loan Details To Be Correct")
    win.geometry("400x200")
    
    top_frame = Frame(win, width = 400, height = 150)
    top_frame.pack(side = TOP)
    message1 = "Accession Number"
    message2 = "Book Title"
    message3 = "Borrow Date"
    message4 = "Membership ID"
    message5 = "Member Name"
    message6 = "Due Date"
    Label(top_frame, text = message1).pack()
    Label(top_frame, text = message2).pack()
    Label(top_frame, text = message3).pack()
    Label(top_frame, text = message4).pack()
    Label(top_frame, text = message5).pack()
    Label(top_frame, text = message6).pack()

    def clicked1():
        if SUCCESS_STATE:
            retrieve_info()
            successMessageWindow()
        elif ERROR1:
            error1_msg_window()
        elif ERROR2:
            error2_msg_window()
        elif ERROR3:
            error3_msg_window()

    bottom_frame = Frame(win, width = 400, height = 50)
    bottom_frame.pack(side = BOTTOM)
    Button(
        bottom_frame,
        text = "Confirm\nLoan",
        command = clicked1).grid(
        row = 0, column = 0, padx = 5, pady = 5)
    Button(
        bottom_frame,
        text = "Back to\nBorrow Function",
        command = win.destroy).grid(
        row = 0, column = 1, padx = 5, pady = 5)    

create_btn = Button(bottom_frame,
                    text = "Borrow Book",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise",
                    command = clicked).grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to Loans Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)
    
window.mainloop()

