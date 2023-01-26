import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import pymysql
from InterfaceHelperFunc import *
from Members import *

WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300
SUCCESS_STATE = True


class Membership_interface(tk.Toplevel):
    def __init__(self,master) -> None:
        super().__init__()
        self.master = master
        button_num_middle1=3
        button_name1=[
            'Membership Creation','Membership Deletion',
            'Membership Update','Back to main menu']
        function_name1=[
            self.call_mem_create,
            self.call_mem_delete,
            self.call_mem_update,self.call_return_main]
        top_text='Select one of the options below:'
        set_pady=20
        haveEntry=False
        PreInputData=False
        Page_Initialization(self,'Membership',
                            top_text,haveEntry,
                            PreInputData,
                            button_num_middle1,
                            button_name1,
                            function_name1,
                            set_pady)


    def call_mem_create(self):
        Membership_Creation(self)
        self.withdraw()
        
    def call_mem_delete(self):
        Membership_Deletion(self)
        self.withdraw()

    def call_mem_update(self):
        Membership_Update(self)
        self.withdraw()

    def call_return_main(self):
        self.master.deiconify()
        self.destroy()


class Membership_Creation(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=5
        button_name1=[
            'Membership ID',
            'Name',
            'Faculty',
            'Phone Number',
            'Email',
            'Back to \n Membership Menu',
            'Create \nMember']
        function_name1=['','','','','',self.call_mem_int,self.data_validation]
        set_pady=5
        haveEntry=True
        PreInputData=False
        top_text="To Create Member,\nPlease Enter Requested Information Below:"
        Page_Initialization(self,'Membership Creation',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)     
            
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: Some validation process
            result = Membership().membership_creation(
                self.retrieved_input_data[0],
                self.retrieved_input_data[1],
                self.retrieved_input_data[2],
                self.retrieved_input_data[3],
                self.retrieved_input_data[4])
            if result[1]:
                messageWindow(
                    result[0],'Success',
                    'Back to Create Function')
            else:
                messageWindow(result[0],'Error',
                              'Back to Create Function')

    def call_mem_int(self):
        self.parent.deiconify()
        self.destroy()
        

class Membership_Deletion(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=1
        button_name1=[
            "Membership ID","Back to \nMembership Menu","Confirm \nDeletion"]
        function_name1=['',self.call_mem_int,self.data_validation]
        set_pady=20
        haveEntry=True
        PreInputData=False
        top_text="To Delete Member, Please enter Membership ID:"
        Page_Initialization(self,'Membership Deletion',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)     
            
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        
        to_be_confirm_list=[
            'Membership ID',
            'Name',
            'Faculty',
            'Phone Number',
            'Email Address']
        if not check_empty_entry(self.retrieved_input_data):
            ### TODO: Some validation process
            result = Membership().confirm_info_member(
                self.retrieved_input_data[0])
            if result[1]:
                button_text=['Back to \nDeletion Function','Confirm\nDeletion']
                self.retrieved_full_data=[
                    self.retrieved_input_data[0],
                    result[0][1], result[0][2],
                    result[0][3], result[0][4]]
                Confirmation_Page(self,to_be_confirm_list,button_text)
            else:
                message = result[0]
                title = "Error"
                button_text = 'Back to \nDelete Function'
                messageWindow(message,title,button_text)
        

    def confirm_func(self):

        Retrieve_Input_Data(self)

        result = Membership().membership_deletion(
            self.retrieved_input_data[0])
        
        self.confirm_win.destroy()
        #TODO: check if successful and record
        
        back_button="Back to \nDeletion Function"

        if result[1]:
            messageWindow("Membership successfully cancelled.",
                          "Success",back_button)
        else:
            message ="Member has loans, reservations or outstanding fines."
            title='Error'
            messageWindow(message,title,back_button)
  
    def call_mem_int(self):
        self.parent.deiconify()
        self.destroy()

class Membership_Update(tk.Toplevel):
    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()
        button_num_middle1=1
        button_name1=["Membership ID","Back to \nMembership Menu","Confirm \nUpdate"]
        function_name1=['',self.call_mem_int,self.data_validation]
        set_pady=20
        haveEntry=True
        PreInputData=False
        top_text="To Update Member, Please Enter Membership ID:"
        Page_Initialization(self,'Membership Update',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)   
        
    def call_mem_int(self):
        self.parent.deiconify()
        self.destroy()
        
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        if not check_empty_entry(self.retrieved_input_data):
            result = Membership().confirm_info_member(
                self.retrieved_input_data[0])
            
            ### TODO: Some validation process
            if result[1]:
                Update_Detail(self.parent,self.retrieved_input_data[0])
                self.destroy()
            else:
                message = result[0]
                title = "Error"
                button_text = 'Back to \nUpdate Function'
                messageWindow(message,title,button_text)                
                
class Update_Detail(tk.Toplevel):
    def __init__(self, root, memid) -> None:
        self.root = root
        self.memid=memid
        super().__init__()
        button_num_middle1=5
        button_name1=[
            'Membership ID',
            'Name',
            'Faculty',
            'Phone Number',
            'Email Address',
            'Back to \nMembership Menu',
            'Confirm \nUpdate']
        result = Membership().confirm_info_member(memid)
        self.preEntry_text=[
            memid, result[0][1], result[0][2],
            result[0][3], result[0][4]]
        function_name1=['','','','','',self.call_mem_int,self.data_validation]
        set_pady=5
        haveEntry=True
        PreInputData=True
        top_text="Membership Update Entry:"
        Page_Initialization(self,'Membership Update',top_text,haveEntry,
                            PreInputData,button_num_middle1,
                            button_name1,function_name1,set_pady)
        
    def data_validation(self):
        Retrieve_Input_Data(self)
        #retrieve input data, this is a global function
        to_be_confirm_list=[
            'Membership ID',
            'Name',
            'Faculty',
            'Phone Number',
            'Email Address']
        if not check_empty_entry(self.retrieved_input_data):
            button_text=['Back to \nUpdate Function','Confirm\nUpdate']
            self.retrieved_full_data=self.retrieved_input_data
            Confirmation_Page(self,to_be_confirm_list,button_text)    

    def confirm_func(self):
        
        self.confirm_win.destroy()
        #TODO: some validation and record
        back_button="Back to Update Function"

        result = Membership().membership_update(
            self.retrieved_input_data[0],
            self.retrieved_input_data[1],
            self.retrieved_input_data[2],
            self.retrieved_input_data[3],
            self.retrieved_input_data[4])
        if result[1]:
            messageWindow("Membership successfully updated.",
                          "Success",back_button)
        else:
            message = result[0]
            title='Error'
            messageWindow(message,title,back_button)

    def call_mem_int(self):
        self.root.deiconify()
        self.destroy()
            
