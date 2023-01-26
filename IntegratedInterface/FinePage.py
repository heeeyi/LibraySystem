import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import pymysql
from InterfaceHelperFunc import *
from Fines import *
import pymysql

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300

SUCCESS_STATE=True
error_type=1

class Fine_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num_middle1=1
        button_name1=['Fine Payment','Back to main menu']
        function_name1=[self.call_fine_paymt,self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=20
        haveEntry=False
        PreInputData=False
        Page_Initialization(self,'Fines',
                            top_text,haveEntry,
                            PreInputData,
                            button_num_middle1,
                            button_name1,
                            function_name1,
                            set_pady)

    def call_fine_paymt(self):
        Fine_Payment(self)
        self.withdraw()
        
    def call_return_main(self):
        self.master.deiconify()
        self.destroy()


class Fine_Payment(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=3
        button_name1=[
            "Membership ID","Payment Date",
            "Payment Amount","Back to\nFine Menu","Confirm \nPayment"]
        function_name1=['','','',self.call_fine_int,self.data_validation]
        set_pady=20
        haveEntry=True
        PreInputData=False
        top_text="To Make a Payment, Please Enter Information Below:"
        Page_Initialization(
            self,'Fine Payment',top_text,haveEntry,
            PreInputData,button_num_middle1,
            button_name1,function_name1,set_pady)     
            
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            'Membership ID','Payment Date','Payment Amount','Exact Fee Only']
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: Some validation process

            result = Fine().confirm_info_fine(
                self.retrieved_input_data[0])
            if result[1]:
                button_text=['Back to \nPayment Function','Confirm\nPayment']
                self.retrieved_full_data=[
                    self.retrieved_input_data[0], #MemberID
                    self.retrieved_input_data[1], #Date
                    '$'+str(self.retrieved_input_data[2]),''] #Amount
                #['A301C', ' 2/22/22', '30']
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = "Error"
                button_text = "Back to \nPayment Function"
                messageWindow(message, title, button_text)
        

    def confirm_func(self):
        #TODO: check if successful and record the payment
        back_button="Back to \nPayment Function"

        result = Fine().fine_payment(
            self.retrieved_input_data[0],
            int(self.retrieved_input_data[2]),
            date_conversion(self.retrieved_input_data[1]))
            
        if result[1]:
            messageWindow("Fine Payment Successful.","Success",back_button)
        else:
            message = result[0]
            title = "Error"
            messageWindow(message,title,back_button)
        self.confirm_win.destroy()

        
    def call_fine_int(self):
        self.parent.deiconify()
        self.destroy()


