from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import tkinter
import pymysql

#NOTICE: SIZE PARAMETERS MAY WORK DIFFERENTLY FOR WINDOW & MAC
#SO NOTE THE SIZE DIFFERENCE IN THE COMMENT
window = Tk()
window.title("Book Reservation")
window.geometry("600x500")


def time_display():
    def close_time_display():
        date.config(text = "Selected Date is: " + cal.get_date())
        top.destroy()
    top = Toplevel(window)

    cal = Calendar(top, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
    cal.pack(pady = 20)
    ttk.Button(top, text="OK", command=close_time_display).pack()
    
#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                bg = "grey",
                bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "To Reserve a Book, Please Enter Information Below:",
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
                font = 10, width = 20, height = 5, bd = 2,
                bg = "lightblue")
field1.grid(
                    row = 1, column = 0, padx = 5, pady = 10)

entry1 = Entry(body_frame,font=("default", 15))
entry1.grid(
    row = 1, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Membership ID",
                font = 10, width = 20, height = 5, bd = 2,
                bg = "lightblue")
field2.grid(
                    row = 2, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame,font=("default", 15))
entry2.grid(
    row = 2, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "Reserva Date",
                font = 10, width = 20, height = 5, bd = 2,
                bg = "lightblue")
field3.grid(
                    row = 3, column = 0, padx = 5, pady = 10)
entry3 = Button(body_frame, text='Click to select the date',
                    width = 23, height = 1,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "white",
                    command = time_display)
entry3.grid(
    row = 3, column = 1, padx = 5, pady = 10)
date = Label(window, text = "")
date.place(x=310, y=360)
#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)


SUCCESS_STATE = False
error_type=0
#Now can arbitrarily vary this for testing
#Later use mySQL response to decide


def reservation_confirmation():
    AN=entry2.get()
    MemID=entry1.get()
    date_text=date.cget("text").split(":")[-1]
    confirm_win = Toplevel()
    confirm_win.geometry("300x400")
    def clicked():
        confirm_win.destroy()
        if SUCCESS_STATE:
            def messageWindow():
                win = Toplevel()
                win.title('Success')
                message = "Reservation is successful"
                Label(win, text=message).pack()
                Button(win, text='Back to Acquisition Function', command=win.destroy).pack()
            messageWindow()

        else:
            if error_type==0:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "Books already reserved; Duplicate, Missing or Incomplete fields."
                    Label(win, text=message).pack()
                    Button(win, text='Back to Reserve Function', command=win.destroy).pack()
                messageWindow()
            elif error_type==1:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "Member currently has 2 Books on Reservation"
                    Label(win, text=message).pack()
                    Button(win, text='Back to Reserve Function', command=win.destroy).pack()
                messageWindow()
            elif error_type==2:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "Member has Outstanding Fine of:"
                    Label(win, text=message).pack()
                    Button(win, text='Back to Reserve Function', command=win.destroy).pack()
                messageWindow()
            else:
                def messageWindow():
                    win = Toplevel()
                    win.title('Error')
                    message = "The book is available for loan, please go to loan menu"
                    Label(win, text=message).pack()
                    Button(win, text='Back to Reserve Function', command=win.destroy).pack()
                messageWindow()
    confirm_win.title('Reservation Confirmation')
    Title_confirm1= Label(confirm_win, text="Confirm Reservation",font=('default',20))
    Title_confirm1.pack(side=TOP)
    Title_confirm2= Label(confirm_win, text="Details To Be Correct",font=('default',20))
    Title_confirm2.pack(side=TOP)
    as_label=Label(confirm_win, text="Assesion Number: "+AN,font=('default',15))
    as_label.place(x=20,y=70)
    book_label=Label(confirm_win, text="Book Title: ",font=('default',15))
    book_label.place(x=20,y=110)
    memid_label=Label(confirm_win, text="Member ID: "+MemID,font=('default',15))
    memid_label.place(x=20,y=150)
    memname_label=Label(confirm_win, text="Member Name: ",font=('default',15))
    memname_label.place(x=20,y=190)
    date_label=Label(confirm_win, text="Reserve Date: "+date_text,font=('default',15))
    date_label.place(x=20,y=230)
    button_text1="""Back to
Reserve
Function"""
    Button1=Button(confirm_win, text=button_text1, justify="center",font=('default',15),height = 4,width=12,command=confirm_win.destroy)
    Button1.place(x=160,y=300)
    button_text2="""Confirm
Reservation"""
    Button2=Button(confirm_win, text=button_text2,justify="center",font=('default',15),height = 4,width=12, compound="c",command=clicked)
    Button2.place(x=20,y=300)
    

    
    
#FOR WINDOWS ALL pady = 1
create_btn = Button(bottom_frame,
                    text = "Reserve Book",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise",
                    command = reservation_confirmation).grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to Reservations Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3, #WINDOWS: font = 8
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)

    
window.mainloop()
