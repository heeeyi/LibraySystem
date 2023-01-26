import tkinter
from tkinter import *
window = Tk()
window.title("Report Homepage")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 360, height = 50,
                    bg = "grey",
                    bd = 0)
top_frame.pack(side = TOP)

#Create a button inside this frame   
select_btn = Label(top_frame,
                    text = "Select one of the options below:",
                    fg = "black", #text color
                    width = 50,
                    font = 11,
                    #Change font of the text, seem change button width?
                    #Width of the button in letters
                    height = 4,
                    #Height of button in text lines for textual buttons
                    bd = 2, #Border width in pixels, default is 2
                    bg = "lightblue").grid(
                        row = 0, column = 0,
                        padx = 1, pady = 1)
#grid seem automatically center the widget inside the frame

#Create the middle button
body_frame = Frame(window, width = 600, height = 350)
body_frame.pack()

BookSearch_btn = Button(body_frame, text = "Book Search",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 0, column = 0, padx = 1, pady = 20)
    
BooksOnLoan_btn = Button(body_frame, text = "Books on Loan",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 1, column = 0, padx = 1, pady = 20)

BookOnReservation_btn = Button(body_frame, text = "Books on Reservation",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 2, column = 0, padx = 1, pady = 20)

OutstandingFines_btn = Button(body_frame, text = "Outstanding Fines",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 3, column = 0, padx = 1, pady = 20)

BooksOnLoanToMember_btn = Button(body_frame, text = " Books on Loan to\nMember",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 4, column = 0, padx = 1, pady = 20)


#Create the bottom button
bottom_frame = Frame(window, width = 600, height = 50,
                        bg = "grey")
bottom_frame.pack(side = BOTTOM)
back_btn = Button(bottom_frame, text = "Back to main menu",
                    fg = "black",
                    width = 50, height = 2,
                    font = 10,
                    bd = 2, bg = "lightblue").grid(
                        row = 0, column = 0, padx = 1, pady = 1)
window.mainloop()
      