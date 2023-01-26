import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import pymysql
from InterfaceHelperFunc import *
from Books import *

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300
SUCCESS_STATE = True

class Book_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num_middle1=2
        button_name1=['Book Acquisition','Book Withdrawal','Back to main menu']
        function_name1=[self.call_book_acq,self.call_book_withdrawl,self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=20
        haveEntry=False
        PreInputData=False
        Page_Initialization(self,'Books',
                            top_text,haveEntry,
                            PreInputData,
                            button_num_middle1,
                            button_name1,
                            function_name1,
                            set_pady)

    def call_book_acq(self):
        Book_Acquisition(self)
        self.withdraw()
        
    def call_book_withdrawl(self):
        Book_Withdrawal(self)
        self.withdraw()

    def call_return_main(self):
        self.master.deiconify()
        self.destroy()

class Book_Acquisition(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=6
        button_name1=[
            'Accession Number',
            'Title',
            'Author',
            'ISBN',
            'Publisher',
            'Publish Year',
            'Back to \nBooks Menu',
            'Add \nNew Book']
        function_name1=[
            '','','','','','',self.call_book_int,self.data_validation]
        set_pady=5
        haveEntry=True
        PreInputData=False
        top_text="For New Book Acquisition,\nPlease Enter Required Information Below:"
        Page_Initialization(self,'Book Acquisition',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)     
            
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
                    
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: Some validation process
            result = Book().book_acquisition(
                self.retrieved_input_data[0],
                self.retrieved_input_data[1],
                self.retrieved_input_data[2],
                self.retrieved_input_data[3],
                self.retrieved_input_data[4],
                self.retrieved_input_data[5])
            
            if result[1]:
                messageWindow(
                    result[0],'Success','Back to \nAcquisition Function')
            else:
                messageWindow(
                    result[0],'Error','Back to \nAcquisition Function')
                
    def call_book_int(self):
        self.parent.deiconify()
        self.destroy()
        

class Book_Withdrawal(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=1
        button_name1=["Accession Number","Back to \nBooks Menu","Confirm \nWithdrawal"]
        function_name1=['',self.call_book_int,self.data_validation]
        set_pady=20
        haveEntry=True
        PreInputData=False
        top_text="To Remove Outdated books From system,\nPlease Enter Required Information Below:"
        Page_Initialization(self,'Book Withdrawal',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)     
            
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            'Accession Number',
            'Title',
            'Arthor',
            'ISBN',
            'Publisher',
            'Publish Year']
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: Some validation process
            result = Book().confirm_info_book(
                self.retrieved_input_data[0])            
            if result[1]:
                button_text=[
                    'Back to \nWithdrawal Function','Confirm\nWithdrawal']
                self.retrieved_full_data=[
                    self.retrieved_input_data[0],
                    result[0][1], result[0][2],
                    result[0][3], result[0][4], result[0][5]]
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = 'Error'
                button_text = 'Back to \nWithdrawal function'
                messageWindow(message, title, button_text)
        

    def confirm_func(self):
        #TODO: check if successful and record the payment
        result = Book().book_withdrawal(
            self.retrieved_input_data[0])
        
        back_button="Back to \nWithdrawal Function"
        if result[1]:
            #reocrd
            messageWindow(result[0],"Success",back_button)
        else:
            message = result[0]
            title='Error'
            messageWindow(message,title,back_button)
        self.confirm_win.destroy()
            
            
    def call_book_int(self):
        self.parent.deiconify()
        self.destroy()


