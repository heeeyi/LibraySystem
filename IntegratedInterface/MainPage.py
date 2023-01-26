import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import tkinter
import pymysql
from ReservationPage import *
from ReportPage import *
from MemberPage import *
from FinePage import *
from BookPage import *
from LoanPage import *
from InterfaceHelperFunc import *


WIDTH = 600
HEIGHT = 500
WIDTH2 = 400
HEIGHT2 = 300

class Main_interface(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        button_num1=6
        button_num_middle1=6
        button_name1=['Membership','Books','Loans','Reservations','Fines','Reports']
        function_name1=[self.call_mem_int,self.call_book_int,self.call_loan_int,self.call_res_int,self.call_fine_int,self.call_rep_int]
        set_pady=5
        top_text='Select one of the options below:'
        haveEntry=False
        Page_Initialization(self,'ALS',top_text,haveEntry,button_num1,button_num_middle1,button_name1,function_name1,set_pady)
        
    def call_res_int(self):
        Reservation_interface(self)
        self.withdraw()

    def call_rep_int(self):
        Report_interface(self)
        self.withdraw()

    def call_mem_int(self):
        Membership_interface(self)
        self.withdraw()

    def call_fine_int(self):
        Fine_interface(self)
        self.withdraw()

    def call_book_int(self):
        Book_interface(self)
        self.withdraw()

    def call_loan_int(self):
        Loan_interface(self)
        self.withdraw()
