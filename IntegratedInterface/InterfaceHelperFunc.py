import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import tkinter
import pymysql

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300

#generate a widow
def Window_Generation(page,page_name,height,width):
    wid_screen = page.winfo_screenwidth()
    height_screen = page.winfo_screenheight()
    x = (wid_screen/2) - (width/2)
    y = (height_screen/2) - (height/2)
    page.geometry('%dx%d+%d+%d' % (width, height, x, y))
    page.title(page_name)
    

#use to initialize the page
#page=class who call the function, e.g MainPage
#page_name: name of the page
#top_text:text shown on the top of the page. e.g, "select one of the options:"
#haveEntry: whether need an entry field
#button_num: how many button on screen
#button_num_middle: how many button on the middle screen
#button_name: what's the name of the button
#function_name: what is the function called after the button is clicked
#set_pady: pady of each button

def Page_Initialization(page,page_name,top_text,haveEntry,PreInputData,button_num_middle,button_name,function_name,set_pady):
    button_num=len(button_name)
    Window_Generation(page,page_name,HEIGHT,WIDTH)
    #page size and location
    Page_Top(page,top_text)
    if haveEntry==False:
        #only the button will be created
        Page_Body_button(page,button_num_middle,button_name,function_name,set_pady)
    else:
        Page_Body_entry(page,button_num_middle,button_name,function_name,set_pady,PreInputData)
        
    if (button_num-button_num_middle)!=0:
        Page_Bottom(page,function_name,button_num,button_num_middle,button_name) 
    
#Top Page initialization
def Page_Top(page,top_text):
    #Create a top frame
    top_frame = tk.Frame(page, width = 360, height = 50,
                        bg = "grey",
                        bd = 0)
    top_frame.pack(side = tk.TOP)
    
    #Create a button inside this frame
    select_btn = tk.Label(top_frame,
                        text = top_text,
                        fg = "black", #text color
                        width = 50,
                        font = 10, ###
                        #Change font of the text, seem change button width?
                        #Width of the button in letters
                        height = 3, ###
                        #Height of button in text lines for textual buttons
                        bd = 2, #Border width in pixels, default is 2
                        bg = "lightblue").grid(
                            row = 0, column = 0,
                            padx = 1, pady = 1)
    #grid seem automatically center the widget inside the frame
    
def time_display(page,i):
    page.top = tk.Toplevel(page)
    wid_screen = page.winfo_screenwidth()
    height_screen = page.winfo_screenheight()
    x = (wid_screen/2) - (WIDTH2/2)
    y = (height_screen/2) - (HEIGHT2/2)
    page.top.geometry('%dx%d+%d+%d' % (WIDTH2, HEIGHT2, x, y))
    page.cal = Calendar(page.top, selectmode = 'day')
    ### Removed year = 2020, month = 5, day = 22
     
    page.cal.pack() ### Removed pady = 1
    ttk.Button(page.top, text="OK", command=lambda:close_time_display(page,i)).pack()

def close_time_display(page,i):
    page.entry_generation[i].config(text = "Selected date: " + page.cal.get_date()+"\n Click to reselect")
    page.top.destroy()
    
def Page_Body_entry(page,button_num_middle,button_name,function_name,set_pady,preEntry):
    #Create the middle button
    page.entry_generation=[]
    body_frame = tk.Frame(page, width = 600, height = 350)
    body_frame.pack()

    for i in range(button_num_middle): #how many entry(count the entry+field as 1) in the body frame
        tk.Label(body_frame, text = button_name[i],
                        font = 8, width = 20, height = 2, bd = 2, ###
                        bg = "lightblue").grid(
                            row = i, column = 0, padx = 5, pady = set_pady) 
        if 'Date' in button_name[i]:
            index=i
            dateentry=tk.Button(body_frame, text='Click to select the date',
                            width = 25, height = 2,
                            bd = 3, ### Removed font = 8, 
                            bg = "white",
                            command = lambda:time_display(page,index))
            dateentry.grid(row = i, column = 1, padx = 5, pady = set_pady)
            page.entry_generation.append(dateentry)
            
        else:
            if preEntry==True and 'ID'in button_name[i]:
                 entry = tk.Label(body_frame, text= page.preEntry_text[i],
                          font = 8, width = 20, height = 2, bd = 2)
                 entry.grid(row = i, column = 1, padx = 5, pady = 10)
            else:
                entry=tk.Entry(body_frame)
                if preEntry==True:
                    entry.insert(tk.END, page.preEntry_text[i])
                entry.grid(row = i, column = 1, padx = 5, pady = set_pady)
            page.entry_generation.append(entry)



#Middle page initialization if all of them are button
def Page_Body_button(page,button_num_middle,button_name,function_name,set_pady):
    #Create the middle button
    body_frame = tk.Frame(page, width = 600, height = 350)
    body_frame.pack()

    for i in range(0,button_num_middle):
        tk.Button(body_frame, text = button_name[i],
                            fg = "black",
                            width = 20, height = 2, ###
                            font = 10, bd = 2,
                            bg = "steelblue",
                command=function_name[i]).grid(
                                row = i, column = 0, padx = 1, pady = set_pady)

#Bottom page initialization
def Page_Bottom(page,function_name,button_num,button_num_middle,button_name):
    #Create the bottom button
    bottom_frame = tk.Frame(page, width = 600, height = 50)
    bottom_frame.pack(side = tk.BOTTOM)
    for i in range(button_num-button_num_middle):#how many button in the bottom frame
        tk.Button(bottom_frame, text = button_name[i+button_num_middle],
                            fg = "black",
                            width = 20, height = 3,
                            font = 8,
                            bd = 2, bg = "turquoise",command=function_name[i+button_num_middle]).grid(
                                row = 0, column = i, padx = 5, pady = 5)
#no sql here
def Retrieve_Input_Data(page):
    page.retrieved_input_data=[]
    for i in range(len(page.entry_generation)):
        if 'button' in str(page.entry_generation[i]):
            page.retrieved_input_data.append(page.entry_generation[i].cget("text").split("\n")[0].split(":")[-1])
        elif 'label' in str(page.entry_generation[i]):
            page.retrieved_input_data.append(page.entry_generation[i].cget("text"))
        else:
            page.retrieved_input_data.append(page.entry_generation[i].get())
    #print(page.retrieved_input_data)
    
#no sql here
def Confirmation_Page(page,to_be_confirm_list,button_text):
    page.confirm_win=tk.Toplevel()
    page_name='Please confirm details to be correct: '
    Window_Generation(page.confirm_win,page_name,HEIGHT2,WIDTH2)
    top_frame = tk.Frame(page.confirm_win, width = 400, height = 150)
    top_frame.pack(side = tk.TOP)

    for i,data in enumerate(page.retrieved_full_data):
        text=to_be_confirm_list[i]+": "+data
        tk.Label(top_frame, text = text).pack()
    
    bottom_frame = tk.Frame(page.confirm_win, width = 400, height = 50)
    bottom_frame.pack(side = tk.BOTTOM)

    tk.Button(bottom_frame, text=button_text[1],command=page.confirm_func).grid(row = 0, column = 1, padx = 5, pady = 5)
    tk.Button(bottom_frame, text=button_text[0],command=page.confirm_win.destroy).grid(row = 0, column = 0, padx = 5, pady = 5)

#no sql here
    
def messageWindow(message,title,button_text):
    win = tk.Toplevel()
    Window_Generation(win,title,HEIGHT2,WIDTH2)
    tk.Label(win, text=message).pack(side=tk.TOP)
    tk.Button(win, text=button_text, command=win.destroy).pack(side = tk.BOTTOM)
        
def date_conversion(date):
    output = ""
    date_list = date.split('/')
    output += "20" + date_list[2] + "-"
    if len(date_list[0]) < 2:
        output += "0"
    output += date_list[0].strip() + "-"
    output += date_list[1]
    return output
    
### verify if there is empty entry, if so, print error message
def check_empty_entry(retrieved_input_data):
    for entry in retrieved_input_data:
        if entry =='' or 'Click' in entry:
            message="Missing or Incomplete Field"
            title="Error"
            button_text='Back to \nReturn Function'
            messageWindow(message,title,button_text)
            #call the message window (global func)
            return True
    return False
