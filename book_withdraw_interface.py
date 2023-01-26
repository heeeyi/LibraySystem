from tkinter import *
from tkinter import messagebox
import tkinter
import pymysql

<<<<<<< HEAD
from book_acq_interface import SUCCESS_STATE
=======
>>>>>>> 24293ec85c956751872d762665ba17c25898dee8

#NOTICE: SIZE PARAMETERS MAY WORK DIFFERENTLY FOR WINDOW & MAC
#SO NOTE THE SIZE DIFFERENCE IN THE COMMENT

window = Tk()
window.title("Book Withdrawal")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                bg = "grey",
                bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "To Remove Outdated books From system,\nPlease Enter Required Information Below:",
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
<<<<<<< HEAD
field1 = Label(body_frame, text = "Accession Number",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue").grid(
                    row = 0, column = 0, padx = 5, pady = 10) 
entry1 = Entry(body_frame).grid(
    row = 0, column = 1, padx = 5, pady = 10)
=======
#FOR WINDOWS ALL THE pady = 5
field1 = Label(body_frame, text = "Accession Number",
                font = 10, width = 20, height = 5, bd = 2,
                bg = "lightblue")
field1.grid(
                    row = 1, column = 0, padx = 5, pady = 10)

entry1 = Entry(body_frame,font=("default", 15))
entry1.grid(
    row = 1, column = 1, padx = 5, pady = 10)
>>>>>>> 24293ec85c956751872d762665ba17c25898dee8

bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)


#SUCCESS_STATE = False
ON_LOAN = False
ON_RESERVE = False
SUCCESS_STATE = True
#Now can arbitrarily vary this for testing
#Later use mySQL response to decide

<<<<<<< HEAD
def clicked():
    #message here can be a new window? Accession Number to Year are data!
    #To be refined!
    def Main_messageWindow():
        win = Toplevel()
        win.title('Please Confirm Details To Be Corect')
        message = "Accession Number, Title, Author, ISBN, Publisher, Year"
        Label(win, text=message).pack()
        Button(win, text='Confirm Withdrawal', command=win.destroy).pack()
        Button(win, text='Back to Withdrawal Function', command=win.destroy).pack()
        second_click()

        #SOMEHOW DOESNT WORK
        def second_click():
            if ON_LOAN:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "Book is currently on Loan"
                    Label(win, text=message).pack()
                    Button(win, text='Return to Withdrawal Function', command=win.destroy).pack()
                messageWindow()
    
            elif ON_RESERVE:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "Book is currently Reserved"
                    Label(win, text=message).pack()
                    Button(win, text='Return to Withdrawal Function', command=win.destroy).pack()
                messageWindow()

            elif SUCCESS_STATE:
                def messageWindow():
                    win = Toplevel()
                    win.title('Success')
                    message = "Outdated Book is Withdrawed"
                    Label(win, text=message).pack()
                    Button(win, text='Back to Withdrawal Function', command=win.destroy).pack()
                messageWindow()

        #withdrawal function to remove book
        #withdraw_book()

    Main_messageWindow()

    """if ON_LOAN:
        def messageWindow():
            win = Toplevel()
            win.title('Error')
            message = "Book is currently on Loan"
            Label(win, text=message).pack()
            Button(win, text='Return to Withdrawal Function', command=win.destroy).pack()
        messageWindow()
    
    elif ON_RESERVE:
        def messageWindow():
            win = Toplevel()
            win.title('Error')
            message = "Book is currently Reserved"
            Label(win, text=message).pack()
            Button(win, text='Return to Withdrawal Function', command=win.destroy).pack()
        messageWindow()

    else:
        def messageWindow():
            win = Toplevel()
            win.title('Success')
            message = "Outdated Book is Withdrawed"
            Label(win, text=message).pack()
            Button(win, text='Back to Withdrawal Function', command=win.destroy).pack()
        messageWindow()

        #withdrawal function to remove book
        #withdraw_book()"""
=======
def loan_messageWindow():
    win = Toplevel()
    win.title('Error')
    message = "Book is currently on Loan"
    Label(win, text=message).pack()
    Button(win, text='Return to Withdrawal Function', command=win.destroy).pack(
        side = BOTTOM)


def reserve_messageWindow():
    win = Toplevel()
    win.title('Error')
    message = "Book is currently Reserved"
    Label(win, text=message).pack()
    Button(win, text='Return to Withdrawal Function', command=win.destroy).pack(
        side = BOTTOM)

def success_messageWindow():
    win = Toplevel()
    win.title('Success')
    message = "Outdated Book is Withdrawed"
    Label(win, text=message).pack()
    Button(win, text='Back to Withdrawal Function', command=win.destroy).pack(
        SIDE = BOTTOM)

def Withdrawal_confirmation():
    AN = entry1.get()
    confirm_win = Toplevel()
    confirm_win.geometry("400x500")
    def clicked():
        confirm_win.destroy()
        if SUCCESS_STATE:
            success_messageWindow()

        else:
            if ON_LOAN:
                loan_messageWindow()
            elif ON_RESERVE:
                reserve_messageWindow()

    confirm_win.title('Confirm Details')
    Title_confirm1= Label(confirm_win, text="Please Confirm",font=('default',20))
    Title_confirm1.pack(side=TOP)
    Title_confirm2= Label(confirm_win, text="Details To Be Correct",font=('default',20))
    Title_confirm2.pack(side=TOP)
    as_label=Label(confirm_win, text="Accession Number: "+AN,font=('default',15))
    as_label.place(x=20,y=70)
    '''book_label=Label(confirm_win, text="Book Title: "+title,font=('default',15))
    book_label.place(x=20,y=110)
    author_label=Label(confirm_win, text="Authors: "+author_name,font=('default',15))
    author_label.place(x=20,y=150)
    isbn_label=Label(confirm_win, text="ISBN: "+isbn,font=('default',15))
    isbn_label.place(x=20,y=190)
    publisher_label=Label(confirm_win, text="Publisher: "+publisher,font=('default',15))
    publisher_label.place(x=20,y=230)
    year_label=Label(confirm_win, text="Publication Year: "+year,font=('default',15))
    year_label.place(x=20,y=270)'''
    button_text1="""Back to \nWithdrawal \nFunction"""
    Button1=Button(confirm_win, text=button_text1, justify="center",font=('default',15),height = 4,width=12,command=confirm_win.destroy)
    Button1.place(x=220,y=400)
    button_text2="""Confirm Withdrawal"""
    Button2=Button(confirm_win, text=button_text2,justify="center",font=('default',15),height = 4,width=12, compound="c",command=clicked)
    Button2.place(x=20,y=400)



>>>>>>> 24293ec85c956751872d762665ba17c25898dee8



#FOR WINDOWS ALL pady = 1
create_btn = Button(bottom_frame,
<<<<<<< HEAD
                    text = "Add New Book",
=======
                    text = "Withdraw Book",
>>>>>>> 24293ec85c956751872d762665ba17c25898dee8
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise",
<<<<<<< HEAD
                    command = clicked).grid(
=======
                    command = Withdrawal_confirmation).grid(
>>>>>>> 24293ec85c956751872d762665ba17c25898dee8
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to Books Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)

<<<<<<< HEAD
    
window.mainloop()
=======

window.mainloop() 
>>>>>>> 24293ec85c956751872d762665ba17c25898dee8
