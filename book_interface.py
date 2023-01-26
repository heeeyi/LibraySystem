from tkinter import *
from tkinter import messagebox
import pymysql

window = Tk()
window.title("Book")
window.geometry("600x500")

#Create a top frame
top_frame = Frame(window, width = 360, height = 50,
                    bg = "grey",
                    bd = 0)
top_frame.pack(side = TOP)

#Create a button inside this frame
#change to lable 
select_btn = Label(top_frame,
                    text = "Select one of the options below:",
                    fg = "black", #text color
                    width = 50,
                    font = 11,
                    height = 4,
                    bd = 2, 
                    bg = "lightblue").grid(
                        row = 0, column = 0,
                        padx = 1, pady = 1)

#Create the middle button
body_frame = Frame(window, width = 600, height = 350)
body_frame.pack()

acq_btn = Button(body_frame, text = "Book Acquisition",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 0, column = 0, padx = 1, pady = 20)
    
withdrawl_btn = Button(body_frame, text = "Book Withdrawal",
                    fg = "black",
                    width = 20, height = 3,
                    font = 10, bd = 2,
                    bg = "steelblue").grid(
                        row = 1, column = 0, padx = 1, pady = 20)

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


"""def bookRegister():
    
    accession_number = en1.get()
    title = en2.get()
    authors = en3.get()
    isbn = en4.get()
    publisher = en5.get()
    publish_year = en6.get()
    insertBooks = "insert into "+BookCollection+" values('"+accession_number+"','"+title+"','"+authors+"','"+isbn+"','"+publisher+"','"+publish_year+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
    except:
        messagebox.showinfo("Error!", "Book already added; Duplicate, Missing or Incomplete fields.")
    
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

def addBooks(): 
    
    global en1,en2,en3,en4,en5,en6,Canvas1,con,cur,BookCollection,root
    
    root = Tk()
    root.title("library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Vitasoy_5757"
    mydatabase="library"

    con = pymysql.connect(host="127.0.0.1",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    BookCollection = "Book" # Book Table

    same=True
    n=0.3
        
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)
        
    # Accession Number
    lb1 = Label(labelFrame,text="Accession Number : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1)
        
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)
        
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.25, relwidth=0.62)
        
    # Authors
    lb3 = Label(labelFrame,text="Authors : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4)
        
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.4, relwidth=0.62)
        
    # ISBN
    lb4 = Label(labelFrame,text="ISBN : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55)
        
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.55, relwidth=0.62)
        
    # Publisher
    lb5 = Label(labelFrame,text="Publisher : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.55)
        
    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.55, relwidth=0.62)

    #Publish year
    lb6 = Label(labelFrame,text="Publish Year : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.55)
        
    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.55, relwidth=0.62)

    #AddNew Button
    AddNewBtn = Button(root,text="Add New Book",bg='#d1ccc0', fg='black',command=bookRegister)
    AddNewBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    backBtn = Button(root,text="Back To Books Menu",bg='#f7f1e3', fg='black', command=root.quit)
    backBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()"""