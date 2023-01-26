#WHATEVER PART YOU WANT TO TEST,
#PUT THAT TRIAL AS TRUE
#SO THAT ALL CODE IS WITHIN 1 FILE.

trial2 = False
if trial2: #The main page of Membership creation
    import tkinter
    from tkinter import *
    window = Tk()
    window.title("Membership")
    window.geometry("600x500")

    #Create a top frame
    top_frame = Frame(window, width = 360, height = 50,
                      bg = "grey",
                      bd = 0)
    top_frame.pack(side = TOP)

    #Create a Label inside this frame
    #Note here should be just a label, not a button
    
    select_btn = Label(top_frame,
                        text = "Select one of the options below:",
                        fg = "black", #text color
                        width = 50,
                        font = 11,
                        #Change font of the text, seem change button width?
                        #Width of the button in letters
                        height = 4,
                        #Height of button in text lines for textual buttons
                        bd = 3, #Border width in pixels, default is 2
                        bg = "lightblue").grid(
                            row = 0, column = 0,
                            padx = 1, pady = 1)
    #grid seem automatically center the widget inside the frame

    #Create the middle button
    body_frame = Frame(window, width = 600, height = 350)
    body_frame.pack()

    create_btn = Button(body_frame, text = "Membership Creation",
                        fg = "black",
                        width = 20, height = 3,
                        font = 10, bd = 2,
                        bg = "steelblue").grid(
                            row = 0, column = 0, padx = 1, pady = 20)
    
    delete_btn = Button(body_frame, text = "Membership deletion",
                        fg = "black",
                        width = 20, height = 3,
                        font = 10, bd = 2,
                        bg = "steelblue").grid(
                            row = 1, column = 0, padx = 1, pady = 20)
    update_btn = Button(body_frame, text = "Membership update",
                        fg = "black",
                        width = 20, height = 3,
                        font = 10, bd = 2,
                        bg = "steelblue").grid(
                            row = 2, column = 0, padx = 1, pady = 20)

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

trial3 = False
if trial3: #Page of membership creation
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
                   bg = "lightblue").grid(
                       row = 0, column = 0, padx = 5, pady = 10)
    entry1 = Entry(body_frame).grid(
        row = 0, column = 1, padx = 5, pady = 10)

    field2 = Label(body_frame, text = "Name",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 1, column = 0, padx = 5, pady = 10)
    entry2 = Entry(body_frame).grid(
        row = 1, column = 1, padx = 5, pady = 10)

    field3 = Label(body_frame, text = "Faculty",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 2, column = 0, padx = 5, pady = 10)
    entry3 = Entry(body_frame).grid(
        row = 2, column = 1, padx = 5, pady = 10)

    field4 = Label(body_frame, text = "Phone Number",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 3, column = 0, padx = 5, pady = 10)
    entry4 = Entry(body_frame).grid(
        row = 3, column = 1, padx = 5, pady = 10)

    field5 = Label(body_frame, text = "Email Address",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 4, column = 0, padx = 5, pady = 10)
    entry5 = Entry(body_frame).grid(
        row = 4, column = 1, padx = 5, pady = 10)

    #Create the bottom frame
    bottom_frame = Frame(window, width = 600, height = 80)
    bottom_frame.pack(side = BOTTOM)

    SUCCESS_STATE = False

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
    
trial4 = False
if trial4: #Page of membership deletion:
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
        height = 2, bd = 2, bg = "lightblue").grid(
        row = 0, column = 0, padx = 5, pady = 40)
    entry = Entry(body_frame).grid(
        row = 0, column = 1, padx = 5, pady = 40)

    #Create the bottom frame
    bottom_frame = Frame(window, width = 600, height = 80)
    bottom_frame.pack(side = BOTTOM)

    SUCCESS_STATE = False

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
        message1 = "Member ID"
        message2 = "Name"
        message3 = "Faculty"
        message4 = "Phone Number"
        message5 = "Email Address"
        Label(top_frame, text = message1).pack()
        Label(top_frame, text = message2).pack()
        Label(top_frame, text = message3).pack()
        Label(top_frame, text = message4).pack()
        Label(top_frame, text = message5).pack()

        def clicked2():
            #Need to close the last window, while opening a new window
            win.destroy()
            if SUCCESS_STATE:
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

trial5 = False
if trial5: #Page of membership update main page:
    import tkinter
    from tkinter import *
    from tkinter import messagebox
    window = Tk()
    window.title("Membership Update")
    window.geometry("600x500")

    top_frame = Frame(window, width = 500, height = 50)
    top_frame.pack(side = TOP)

    enter_label = Label(
        top_frame,
        text = "To Update Member, Please Enter Membership ID:",
        fg = "black", width = 65,
        font = 10, height = 4,
        bd = 3, bg = "turquoise").grid(
            row = 0, column = 0, padx = 1, pady = 1)

    body_frame = Frame(window, width = 600, height = 300)
    body_frame.pack()

    field = Label(
        body_frame, text = "Membership ID", font = 10,
        width = 20, height = 2, bd = 2, bg = "lightblue").grid(
            row = 0, column = 0, padx = 5, pady = 40)
    entry = Entry(body_frame).grid(
        row = 0, column = 1, padx = 5, pady = 40)

    bottom_frame = Frame(window, width = 600, height = 80)
    bottom_frame.pack(side = BOTTOM)

    update_btn = Button(
        bottom_frame, text = "Update Member",
        fg = "black", width = 25, height = 3,
        font = 10, bd = 3, bg = "turquoise").grid(
            row = 0, column = 0, padx = 10, pady = 10)
    back_btn = Button(
        bottom_frame, text = "Back to Membership Menu",
        fg = "black", width = 25, height = 3,
        font = 10, bd = 3, bg = "turquoise").grid(
            row = 0, column = 1, padx = 10, pady = 10)
    window.mainloop()

trial6 = False
if trial6: #Membership update entry page:
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

    #Create the middle frame
    body_frame = Frame(window, width = 600, height = 300)
    body_frame.pack()

    field1 = Label(body_frame, text = "Membership ID",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 0, column = 0, padx = 5, pady = 5)
    entry1 = Entry(body_frame).grid(
        row = 0, column = 1, padx = 5, pady = 10)

    field2 = Label(body_frame, text = "Name",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 1, column = 0, padx = 5, pady = 5)
    entry2 = Entry(body_frame).grid(
        row = 1, column = 1, padx = 5, pady = 10)

    field3 = Label(body_frame, text = "Faculty",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 2, column = 0, padx = 5, pady = 5)
    entry3 = Entry(body_frame).grid(
        row = 2, column = 1, padx = 5, pady = 10)

    field4 = Label(body_frame, text = "Phone Number",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 3, column = 0, padx = 5, pady = 5)
    entry4 = Entry(body_frame).grid(
        row = 3, column = 1, padx = 5, pady = 10)

    field5 = Label(body_frame, text = "Email Address",
                   font = 8, width = 20, height = 2, bd = 2,
                   bg = "lightblue").grid(
                       row = 4, column = 0, padx = 5, pady = 5)
    entry5 = Entry(body_frame).grid(
        row = 4, column = 1, padx = 5, pady = 10)

    #Create the bottom frame
    bottom_frame = Frame(window, width = 600, height = 80)
    bottom_frame.pack(side = BOTTOM)

    SUCCESS_STATE = True

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
        message1 = "Member ID"
        message2 = "Name"
        message3 = "Faculty"
        message4 = "Phone Number"
        message5 = "Email Address"
        Label(top_frame, text = message1).pack()
        Label(top_frame, text = message2).pack()
        Label(top_frame, text = message3).pack()
        Label(top_frame, text = message4).pack()
        Label(top_frame, text = message5).pack()

        def clicked2():
            #Need to close the last window, while opening a new window
            win.destroy()
            if SUCCESS_STATE:
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












