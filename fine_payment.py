#Page of fine payment
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Fine Payment")
window.geometry("600x500")


#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                bg = "grey",
                bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "To Pay a Fine, Please Enter Information Below:",
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

field1 = Label(body_frame, text = "Membership ID",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field1.grid(row = 0, column = 0, padx = 5, pady = 10)
entry1 = Entry(body_frame)
entry1.grid(row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Payment Date",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field2.grid(row = 1, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame)
entry2.grid(row = 1, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "Payment Amount",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field3.grid(row = 2, column = 0, padx = 5, pady = 10)
entry3 = Entry(body_frame)
entry3.grid(row = 2, column = 1, padx = 5, pady = 10)


#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

SUCCESS_STATE = True
ERROR1 = False
ERROR2 = False

def retrieve_info():
    MemID = str(entry1.get())
    payment_date = str(entry2.get())
    payment_amount = str(entry3.get())
    print(MemID, payment_date, payment_amount)
    #Supposed to be adding these to MySQL
    #Now just print out in the shell

def messageWindow1():
    win2 = Toplevel()
    win2.title("Success")
    win2.geometry("400x200")
    message = "Fine Payment Successful."
    Label(win2, text = message).pack(side = TOP)
    Button(
        win2, text = "Back to Payment Function", command = win2.destroy).pack(
            side = BOTTOM)

def messageWindow2():
    win = Toplevel()
    win.geometry("300x200")
    win.title("Error")
    message = "Member has no fine."
    Label(win, text = message).pack(side = TOP, pady = 10)
    Button(win, text = "Back to Payment Function",
            command = win.destroy).pack(side = BOTTOM, pady = 10)

def messageWindow3():
    win = Toplevel()
    win.geometry("300x200")
    win.title("Error")
    message = "Incorrect fine payment amount."
    Label(win, text = message).pack(side = TOP, pady = 10)
    Button(win, text = "Back to Payment Function",
            command = win.destroy).pack(side = BOTTOM, pady = 10)

def clicked():
    #Need to invoke a new window
    win = Toplevel()
    win.title("Please Confirm Details to be Correct")
    win.geometry("400x200")
    
    top_frame = Frame(win, width = 400, height = 150)
    top_frame.pack(side = TOP)
    message1 = "Member ID"
    message2 = "Payment Due: $X"
    message3 = "Exact Fee Only"
    message4 = "Payment Date"
    Label(top_frame, text = message1).pack()
    Label(top_frame, text = message2).pack()
    Label(top_frame, text = message3).pack()
    Label(top_frame, text = message4).pack()
    
    def clicked2():
        #Need to close the last window, while opening a new window
        win.destroy()
        if SUCCESS_STATE:
            retrieve_info()
            messageWindow1()
        elif ERROR1:
            messageWindow2()
        elif ERROR2:
            messageWindow3()
    
    bottom_frame = Frame(win, width = 400, height = 50)
    bottom_frame.pack(side = BOTTOM)
    Button(
        bottom_frame,
        text = "Confirm\nPayment",
        command = clicked2).grid(
        row = 0, column = 0, padx = 5, pady = 5)
    Button(
        bottom_frame,
        text = "Back to Payment\nFunction",
        command = win.destroy).grid(
        row = 0, column = 1, padx = 5, pady = 5)
    



# create the bottom 2 buttons
payFine_btn = Button(bottom_frame,
                        text = "Pay Fine",
                        fg = "black",
                        width = 20, height = 3,
                        font = 10, bd = 3,
                        bg = "turquoise",
                        command = clicked).grid(
                            row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                        text = "Back to Fines Menu",
                        fg = "black",
                        width = 20, height = 3,
                        font = 10, bd = 3,
                        bg = "turquoise").grid(
                            row = 0, column = 1, padx = 10, pady = 10)
    
window.mainloop()