import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from InterfaceHelperFunc import *
from Reservations import *
import pymysql


#NOTICE: SIZE PARAMETERS MAY WORK DIFFERENTLY FOR WINDOW & MAC
#SO NOTE THE SIZE DIFFERENCE IN THE COMMENT

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300
#SUCCESS_STATE = False
#error_type=1

class Reservation_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num_middle1=2
        button_name1=[
            'Book Reservation',
            'Reservation\nCancellation',
            'Back to main menu']
        function_name1=[
            self.call_book_res,
            self.call_res_cancel,
            self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=20
        haveEntry=False
        PreInputData=False
        Page_Initialization(self,'Reservation',
                            top_text,haveEntry,PreInputData,
                            button_num_middle1,button_name1,
                            function_name1,set_pady)
        
    def call_book_res(self):
        Book_Reservation(self)
        self.withdraw()

    def call_res_cancel(self):
        Reservation_Cancellation(self)
        self.withdraw()
        
    def call_return_main(self):
        self.master.deiconify()
        self.destroy()
        
        
class Book_Reservation(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=3
        button_name1=[
            "Accession Number","Membership ID","Reserve Date",
            "Back to\nReservation Menu","Confirm\nReservation"]
        function_name1=['','','',self.call_res_int,self.data_validation]
        set_pady=5
        haveEntry=True
        PreInputData=False
        top_text='To Reserve a Book, \nPlease Enter Information Below:'
        Page_Initialization(
            self,'Book Reservation',top_text,haveEntry,
            PreInputData,button_num_middle1,button_name1,
            function_name1,set_pady)

    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            "Assesion Number","Book Title","Member ID",
            "Member Name","Reserve Date"]
        if not check_empty_entry(self.retrieved_input_data):
        ### TODO: data from sql need to be inserted in self.retrieved_full_data
            result = Reservation().confirm_info_reservation(
                self.retrieved_input_data[2], #Date
                self.retrieved_input_data[1], #MemID
                self.retrieved_input_data[0]) #BookNum

            if result[1]:        
                self.retrieved_full_data=[
                    self.retrieved_input_data[0], result[0][1],
                    self.retrieved_input_data[1], result[0][3],
                    self.retrieved_input_data[2]]
                button_text=['Back to\nReservation Function','Confirm\nReservation']
            
                # can choose not to call the confirmation window
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = 'Error'
                button_text = 'Back to \nReservation Function'
                messageWindow(message,title,button_text)

    def confirm_func(self):

        ### TODO: some condition in checking whether the
        #action is successful ONLY after the confirmation window is shown,
        #it MUST be under confirm_func (all have same names)
        
        Retrieve_Input_Data(self)
        
        result = Reservation().make_reservation(
            date_conversion(self.retrieved_input_data[2]), #Date
            self.retrieved_input_data[1], #MemID
            self.retrieved_input_data[0]) #BookNum
            
        self.confirm_win.destroy()
        
        if result[1]:
            ### TODO: update relevant table in sql
            message="Book reservation is successful"
            title="Success"
        else:
            message = result[0]
            title = 'Error'
        button_text='Back to \nReservation Function'
        
        messageWindow(message,title,button_text)#call the message window (global func)
                    
    def call_res_int(self):
        self.parent.deiconify()
        self.destroy() 
    
class Reservation_Cancellation(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=3
        button_name1=[
            "Accession Number","Membership ID","Cancel Date",
            "Back to\nReservation Menu","Confirm\nCancellation"]
        function_name1=['','','',self.call_res_int,self.data_validation]
        set_pady=5
        haveEntry=True
        PreInputData=False
        top_text='To Cancel a Reservation, \nPlease Enter Information Below:'
        Page_Initialization(
            self,'Reservation Cancellation',top_text,haveEntry,
            PreInputData,button_num_middle1,button_name1,function_name1,set_pady)

    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            "Assesion Number","Book Title","Member ID",
            "Member Name","Cancel Date"]
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: data from sql need to be inserted in self.retrieved_full_data
            result = Reservation().confirm_info_reservation(
                self.retrieved_input_data[2], #Date
                self.retrieved_input_data[1], #MemID
                self.retrieved_input_data[0]) #BookNum
            if result[1]:        
                self.retrieved_full_data=[
                    self.retrieved_input_data[0], result[0][1],
                    self.retrieved_input_data[1], result[0][3],
                    self.retrieved_input_data[2]]
                button_text=['Back to\nCancellation Function','Confirm\nCancellation']
            
                # can choose not to call the confirmation window
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = 'Error'
                button_text = 'Back to \nCancellation Function'
                messageWindow(message,title,button_text)

    def confirm_func(self):    
        ### TODO: some condition in checking whether the
        #action is successful ONLY after the confirmation window is shown,
        #it MUST be under confirm_func (all have same names)
        #Well this is to convert python date into sql date
        result = Reservation().delete_reservation(
            date_conversion(self.retrieved_input_data[2]), #Date
            self.retrieved_input_data[1], #MemID
            self.retrieved_input_data[0]) #BookNum
            
        self.confirm_win.destroy()
        
        if result[1]:
            ### TODO: update relevant table in sql
            message= result[0]
            title="Success"
        else:
            message = result[0]
            title = 'Error'
        button_text='Back to \nReservation Function'
        
        messageWindow(message,title,button_text)
        #call the message window (global func)

                     
    def call_res_int(self):
        self.parent.deiconify()
        self.destroy() 
