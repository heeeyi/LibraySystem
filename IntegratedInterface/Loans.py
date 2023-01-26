import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv
import datetime
from datetime import datetime
from datetime import timedelta
from Fines import *

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Loan(object):
    
    def book_borrow(self, AccessionNumber, memberID):
        book_info = (AccessionNumber, memberID)

        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        def check_if_on_reservation():
            cur.execute(
                'SELECT * FROM Reservation WHERE BookNumber = "'
                + book_info[0] + '"')
            ExistBook = cur.rowcount
            if ExistBook == 0:
                return 1 
            else:
                return 0 

        def check_if_on_loan():
            cur.execute(
                'SELECT * FROM Loan WHERE BookNumber = "' + book_info[0] + '"')
            ExistBook = cur.rowcount
            if ExistBook == 0:
                return 1 
            else:
                return 0 

        def check_if_exceed_loan_quota():
            cur.execute(
                'SELECT * FROM Loan WHERE MemberID = "' + book_info[1] + '"')
            ExistBook = cur.rowcount
            if ExistBook < 2:
                return 1 
            else:
                return 0

        resultA = check_if_on_reservation() and check_if_on_loan() and check_if_exceed_loan_quota()

        if resultA:            
            BorrowDate = datetime.today().strftime('%Y-%m-%d')
            Valid_Date = timedelta(days = 14)
            DueDate = (datetime.today() + Valid_Date).strftime('%Y-%m-%d')
            cur.execute(
                'INSERT INTO Loan(BorrowDate, DueDate, MemberID, BookNumber)'+
                'VALUES("' + BorrowDate + '", "' + DueDate
                + '", "' + book_info[1] + '", "' + book_info[0] + '");'
            )
            conn.commit()
            conn.close()
            return ("Book borrow successful", True)

        elif not check_if_on_loan():
            cur.execute(
                'SELECT DueDate FROM Loan WHERE BookNumber = "' +
                book_info[0] + '"')
            DueDate = cur.fetchone()[0]
            conn.close()
            return ("Book currently on Loan until: " +
                    DueDate.strftime('%Y-%m-%d'), False)

        elif not check_if_on_reservation():
            conn.close()
            return ("Book currently on reservation", False)
        
        elif not check_if_exceed_loan_quota():
            conn.close()
            return ("Member loan quota exceeded", False)

    def confirm_info_loan(self, MemID, BookNum):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        #Extract information, confirm cancellation details to be correct
        cur.execute(
            'SELECT AccessionNumber, Title FROM Book ' +
            'WHERE AccessionNumber = "' + BookNum + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        output = cur.fetchone()
        cur.execute(
            'SELECT MemberID, Name FROM Member ' +
            'WHERE MemberID = "' + MemID + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        BorrowDate = datetime.today().strftime('%Y-%m-%d')
        Valid_Date = timedelta(days = 14)
        DueDate = (datetime.today() + Valid_Date).strftime('%Y-%m-%d')

        output = output + (BorrowDate,)
        output = output + cur.fetchone()
        output = output + (DueDate,)
        conn.close()

        return (output, True)
    #(('A01', 'A 1984 Story', '2022-02-24', 'AAA', 'Heyi', '2022-03-10'), True)

    def confirm_info_loan2(self, BookNum):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        #Extract information
        cur.execute(
            'SELECT AccessionNumber, Title FROM Book ' +
            'WHERE AccessionNumber = "' + BookNum + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        output = cur.fetchone()

        cur.execute(
            'SELECT m.MemberID, m.Name FROM Member m ' +
            'INNER JOIN Loan l ON m.MemberID = l.MemberID ' +
            'INNER JOIN Book b ON b.AccessionNumber = l.BookNumber '
            'WHERE b.AccessionNumber = "' + BookNum + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        ReturnDate = datetime.today().strftime('%Y-%m-%d')

        output = output + cur.fetchone()
        output = output + (ReturnDate,)
        conn.close()

        return (output, True)

    def book_return(self, AccessionNumber, return_date):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        cur.execute(
            'SELECT MemberID from Loan where BookNumber = "' +
            AccessionNumber + '"')        
        MemberID = cur.fetchone()[0]       
        book_info = (AccessionNumber, MemberID)
        
        def check_fine():
            cur.execute(
                'SELECT * FROM Fine WHERE MemberID = "' + book_info[1] + '"')
            ExistFine = cur.rowcount
            if ExistFine == 0:
                return 1 #output success window
            else:
                return 0 #output error message
            
        fine_result = Fine().check_outstanding_fine(MemberID)
        if fine_result:
            Fine().insert_update_fine(MemberID)
        
        cur.execute(
            'DELETE FROM Loan WHERE MemberID = "' + book_info[1] + '"')
        conn.commit()

        if check_fine():
            conn.close()
            return ("Book return successful", True)
        else:
            conn.close()
            return ("Book returned successfully but has fines", False)

        
        
