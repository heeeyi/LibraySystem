import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Book Search")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 500, height = 50,
                    bg = "grey",
                    bd = 0)
top_frame.pack(side = TOP)

#Create a Label inside this frame  
enter_label = Label(top_frame,
        text = "Search based on one of the categories below:",
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

field1 = Label(body_frame, text = "Title",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field1.grid(row = 0, column = 0, padx = 5, pady = 10)
entry1 = Entry(body_frame)
entry1.grid(row = 0, column = 1, padx = 5, pady = 10)

field2 = Label(body_frame, text = "Authors",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field2.grid(row = 1, column = 0, padx = 5, pady = 10)
entry2 = Entry(body_frame)
entry2.grid(row = 1, column = 1, padx = 5, pady = 10)

field3 = Label(body_frame, text = "ISBN",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field3.grid(row = 2, column = 0, padx = 5, pady = 10)
entry3 = Entry(body_frame)
entry3.grid(row = 2, column = 1, padx = 5, pady = 10)

field4 = Label(body_frame, text = "Publisher",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field4.grid(row = 3, column = 0, padx = 5, pady = 10)
entry4 = Entry(body_frame)
entry4.grid(row = 3, column = 1, padx = 5, pady = 10)

field5 = Label(body_frame, text = "Publication Year",
                font = 8, width = 20, height = 2, bd = 2,
                bg = "lightblue")
field5.grid(row = 4, column = 0, padx = 5, pady = 10)
entry5 = Entry(body_frame)
entry5.grid(row = 4, column = 1, padx = 5, pady = 10)

def retrieve_info():
    Title = str(entry1.get())
    Authors = str(entry2.get())
    ISBN = str(entry3.get())
    Publisher = str(entry4.get())
    Publication_Year = str(entry5.get())
    print(Title, Authors, ISBN, Publisher, Publication_Year)
    #Supposed to be adding these to MySQL
    #Now just print out in the shell

#Create the bottom frame
bottom_frame = Frame(window, width = 600, height = 80)
bottom_frame.pack(side = BOTTOM)

search_btn = Button(bottom_frame,
                    text = "Search Book",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise").grid(
                        row = 0, column = 0, padx = 10, pady = 10)
back_btn = Button(bottom_frame,
                    text = "Back to\nReports Menu",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 3,
                    bg = "turquoise").grid(
                        row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()