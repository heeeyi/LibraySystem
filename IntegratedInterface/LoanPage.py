import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from InterfaceHelperFunc import *
import pymysql
from datetime import date
from Fines import *
from Loans import *

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300
SUCCESS_STATE = True


class Loan_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num1=3
        button_num_middle1=2
        button_name1=['Book Borrowing','Book Returning','Back to main menu']
        function_name1=[
            self.call_book_borrow,self.call_book_return,self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=20
        haveEntry=False
        Page_Initialization(
            self,'Loan',top_text,haveEntry,button_num1,
            button_num_middle1,button_name1,function_name1,set_pady)
   
    def call_book_borrow(self):
        Book_Borrowing(self)
        self.withdraw()
        
    def call_book_return(self):
        Book_Return(self)
        self.withdraw()

    def call_return_main(self):
        self.master.deiconify()
        self.destroy()
        

class Book_Borrowing(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num1=4
        button_num_middle1=2
        button_name1=[
            "Accession Number","Membership ID","Back to\nLoan Menu","Borrow \nBook"]
        function_name1=['','',self.call_loan_int,self.data_validation]
        set_pady=5
        haveEntry=True
        top_text="To Borrow a Book, Please Enter Information Below:"
        Page_Initialization(
            self,'Book Borrowing',top_text,haveEntry,
            button_num1,button_num_middle1,button_name1,
            function_name1,set_pady)

    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            "Accession Number","Book Title",
            "Borrow Date","Membership ID","Member Name","Due Date"]
        
        ### TODO: data from sql need to be inserted in
        #self.retrieved_full_data, also, calculate the due date,
        #now is same as borrow date

        if not check_empty_entry(self.retrieved_input_data):

            result = Loan().confirm_info_loan(
                self.retrieved_input_data[1], #MemberID
                self.retrieved_input_data[0]) #BookNum
            if result[1]:
                self.retrieved_full_data=[
                    self.retrieved_input_data[0],
                    result[0][1], result[0][2],
                    self.retrieved_input_data[1],
                    result[0][4], result[0][5]]
                button_text=['Back to\nBorrow Function','Confirm\nLoan']
        
                # can choose not to call the confirmation window
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = "Error"
                button_text = "Back to \nPayment Function"
                messageWindow(message, title, button_text)

    def confirm_func(self):
        ### TODO: some condition in checking whether the
        #action is successful ONLY after the confirmation window is shown,
        #it MUST be under confirm_func (all have same names)
        self.confirm_win.destroy()

        #Check if he has overdue book and impose fines
        resultA = Fine().check_outstanding_fine(
            self.retrieved_input_data[1])
        if resultA:
            Fine().insert_update_fine(self.retrieved_input_data[1])
            message = "Member has outstanding fines"
            title = "Error"
        else:
            resultB = Loan().book_borrow(
                self.retrieved_input_data[0],
                self.retrieved_input_data[1])
            if resultB[1]:
                title = "Success"
            else:
                title = "Error"
            message = resultB[0]
        button_text='Back to \nBorrowing Function'
        
        messageWindow(message,title,button_text)
        #call the message window (global func)
                    
    def call_loan_int(self):
        self.parent.deiconify()
        self.destroy()


class Book_Return(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num1=4
        button_num_middle1=2
        button_name1=[
            "Accession Number","Return Date",
            "Back to\nLoan Menu","Return \nBook"]
        function_name1=['','',self.call_loan_int,self.data_validation]
        set_pady=5
        haveEntry=True
        top_text="To Return a Book, Please Enter Information Below:"
        Page_Initialization(
            self,'Book Return',top_text,haveEntry,
            button_num1,button_num_middle1,button_name1,
            function_name1,set_pady)

    def data_validation(self):
        empty_entry=False
        valid_data=True #default should be false 
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        
        to_be_confirm_list=[
            "Accession Number","Book Title",
            "Membership ID","Member Name","Return Date","Fine"]
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: data from sql need to be inserted
            #in self.retrieved_full_data, calculate the fine

            result = Loan().confirm_info_loan2(
                self.retrieved_input_data[0]) #BookNum
            
            if result[1]:
                fine = Fine().calculate_fine(
                    result[0][2])
                self.retrieved_full_data=[
                    self.retrieved_input_data[0], #AN
                    result[0][1], #Title
                    result[0][2], 
                    result[0][3], #Membername
                    datetime.today().strftime('%Y-%m-%d'), #Return date
                    '$' + str(fine)]
                button_text=['Back to\nReturn Function','Confirm\nReturn']
                # can choose not to call the confirmation window
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message="Incorrect information"
                title="Error"
                button_text='Back to \nReturn Function'
                messageWindow(message,title,button_text)
                #call the message window (global func)                

    def confirm_func(self):
        ### TODO: some condition in checking whether
        #the action is successful ONLY after the confirmation window is shown,
        #it MUST be under confirm_func (all have same names)
        self.confirm_win.destroy()

        result = Loan().book_return(
            self.retrieved_input_data[0],
            date_conversion(self.retrieved_input_data[1]))
       
        if result[1]:
            ### TODO: update relevant table in sql
            message= result[0]
            title="Success"
            
        else:
            ### TODO: update relevant table in sql
            message = result[0]
            title='Error'
            
        button_text='Back to \nReturn Function'
        
        messageWindow(message,title,button_text)
        #call the message window (global func)
                    
    def call_loan_int(self):
        self.parent.deiconify()
        self.destroy()
