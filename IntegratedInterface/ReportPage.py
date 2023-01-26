import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import pymysql
from InterfaceHelperFunc import*
from Reports import *


WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300


class Report_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num_middle1=5
        button_name1=[
            'Book Search',
            'Books on Loan',
            'Books on Reservation',
            'Outstanding Fines',
            'Books on Loan\nto Member',
            'Back to main menu']
        function_name1=[
            self.call_bk_search,
            self.call_bk_loan,
            self.call_bk_res,
            self.call_out_fine,
            self.call_bk_loan_mem,
            self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=5
        haveEntry=False
        PreInputData=False
        Page_Initialization(self,'Report',
                            top_text,haveEntry,PreInputData,
                            button_num_middle1,button_name1,
                            function_name1,set_pady)

       
    def call_bk_search(self):
        Book_Search(self)
        self.withdraw()

    def call_bk_loan(self):
        Search_Table(self,2,'Book on Loans Report')
        self.withdraw()
        
    def call_bk_res(self):
        Search_Table(self,3,'Book on Reservations Report')
        self.withdraw()

    def call_out_fine(self):
        Search_Table(self,4,'Members With Outstanding Fines')
        self.withdraw()

    def call_bk_loan_mem(self):
        Book_On_Loan_To_Member(self)
        self.withdraw()
            
    def call_return_main(self):
        self.master.deiconify()
        self.destroy()


class Book_Search(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=5
        button_name1=[
            'Title',
            'Arthor',
            'ISBN',
            'Publisher',
            'Publish Year',
            'Back to \nReports Menu',
            'Search \nBook']
        function_name1=[
            '',
            '',
            '',
            '',
            '',
            self.call_rep_int,
            self.book_search_result]
        top_text='Search based on one of the categories below: '
        set_pady=5
        haveEntry=True
        PreInputData=False
        Page_Initialization(self,'Book Search',
                            top_text,haveEntry,PreInputData,
                            button_num_middle1,button_name1,
                            function_name1,set_pady)

    def call_rep_int(self):
        self.parent.deiconify()
        self.destroy()

    def book_search_result(self):
        Retrieve_Input_Data(self)
        if Report().decide_action(*self.retrieved_input_data)== 0:
            messageWindow('No input Dected','Error','Back to \nSearch Function')
        else:
            multiple_entry=False
            for i,entry in enumerate(self.retrieved_input_data):
                if len(entry.split(" "))>1 and " " not in entry[0] and " " not in entry[-1]:
                    messageWindow('Please enter exatly one word in each field',
                                  'Error','Back to \nSearch Function')
                    multiple_entry=True
                    break
                else:
                    self.retrieved_input_data[i]=entry.strip(" ")
            if not multiple_entry:
                Search_Table(self,1,'Book Search Results')
        
class Book_On_Loan_To_Member(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=1
        button_name1=[
            'Membership ID',
            'Back to \nReports Menu',
            'Search \nMember']
        function_name1=[
            '',
            self.call_rep_int,
            self.member_search_result]
        
        top_text='Search based on the category below: '
        set_pady=5
        haveEntry=True
        PreInputData=False
        Page_Initialization(self,'Book On Loan To Member',
                            top_text,haveEntry,PreInputData,
                            button_num_middle1,button_name1,
                            function_name1,set_pady)
    def call_rep_int(self):
        self.parent.deiconify()
        self.destroy()

    def member_search_result(self):
        Retrieve_Input_Data(self)
        if not check_empty_entry(self.retrieved_input_data):
            Search_Table(self,5,'Books on Loan to Member')
        
        
class Search_Table(tk.Toplevel):
    def __init__(self,root,search_type,title):
        super().__init__()
        self.root = root
        Window_Generation(self,title,HEIGHT2*1.5,WIDTH2*2)
        back_title=['Back to\nReports Menu']
        top_frame = tk.Frame(self, width = 500, height = 50,
                        bg = "grey",
                        bd = 0)
        top_frame.pack(side = tk.TOP)
        #initialize table parametre
        total_rows=0
        total_columns=0
        lst = []

        #specify the serach type
        if search_type==1:
            result = Report().search_book(*root.retrieved_input_data) 
            lst =[('Accession Number','Title','Authors',
                   'ISBN','Publisher','Year')]
            lst.extend(result)
            total_rows = len(lst)
            total_columns = len(lst[0])
            back_title=["Back to \nSearch Function"]
    

        elif search_type==2:
            result= Report().books_on_loan()
            lst =[('Accession Number','Title','Authors',
                   'ISBN','Publisher','Year')]
            lst.extend(result)
            total_rows = len(lst)
            total_columns = len(lst[0])
            
        elif search_type==3:
            result= Report().books_on_reservation()
            lst =[('Accession Number','Title','Membership ID','Name')]
            lst.extend(result)
            total_rows = len(lst)
            total_columns = len(lst[0])

        elif search_type==4:
            result= Report().outstanding_fines()
            lst =[('Membership ID','Name','Faculty','Phone Number',
                   'Email Address')]
            lst.extend(result)
            total_rows = len(lst)
            total_columns = len(lst[0])

        elif search_type==5:
            result= Report().books_on_loan_to_member(*root.retrieved_input_data)
            lst =[('Accession Number','Title','Authors',
                   'ISBN','Publisher','Year')]
            lst.extend(result)
            total_rows = len(lst)
            total_columns = len(lst[0])
            back_title=["Back to \nSearch Function"]
            
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if j==5: ###
                    self.e = tk.Entry(top_frame, width=5, fg='black',
                               font=('default',8,'bold')) 
                elif j==0: ###
                    self.e = tk.Entry(top_frame, width=15, fg='black',
                               font=('default',8,'bold'))
                elif j==1: ###
                    self.e = tk.Entry(top_frame, width=35, fg='black',
                               font=('default',8,'bold'))
                else: ###
                    self.e = tk.Entry(top_frame, width=15, fg='black',
                               font=('default',8,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])
        Page_Bottom(self,[self.call_back],1,0,back_title)
        
    def call_back(self):
        self.destroy()
        self.root.deiconify()
