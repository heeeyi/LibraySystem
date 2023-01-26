import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv
import datetime
from datetime import datetime
from datetime import timedelta

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Loan(object):
    
    def book_borrow(self, AccessionNumber, memberID):
        book_info = (AccessionNumber, memberID)

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        def check_if_on_reservation():
            cur.execute(
                'SELECT * FROM Reservation WHERE BookNumber = "' + book_info[0] + '"')
            ExistBook = cur.rowcount
            if ExistBook == 0:
                return 1 #output success window
            else:
                return 0 #output error message

        def check_if_on_loan():
            cur.execute(
                'SELECT * FROM Loan WHERE BookNumber = "' + book_info[0] + '"')
            ExistBook = cur.rowcount
            if ExistBook == 0:
                return 1 #output success window
            else:
                return 0 #output error message

        def check_if_exceed_loan_quota():
            cur.execute(
                'SELECT * FROM Loan WHERE MemberID = "' + book_info[1] + '"')
            ExistBook = cur.rowcount
            if ExistBook < 2:
                return 1 #output success window
            else:
                return 0 #output error message

        def check_fine():
            cur.execute(
                'SELECT * FROM Fine WHERE MemberID = "' + book_info[1] + '"')
            ExistFine = cur.rowcount
            if ExistFine == 0:
                return 1 #output success window
            else:
                return 0 #output error message        

        if check_if_on_reservation() and check_if_on_loan() and check_if_exceed_loan_quota() and check_fine():
            BorrowDate = datetime.today().strftime('%Y-%m-%d')
            Valid_Date = timedelta(days = 14)
            DueDate = (datetime.today() + Valid_Date).strftime('%Y-%m-%d')
            cur.execute(
                'INSERT INTO Loan(BorrowDate, DueDate, MemberID, BookNumber)'+
                'VALUES("' + BorrowDate + '", "' + DueDate + '", "' + book_info[1] + '", "' + book_info[0] + '");'
            )
            conn.commit()
            conn.close()
            return ("Book borrow successful", True)
        
        elif not check_if_on_reservation():
            conn.close()
            return ("Book currently on reservation", False)

        elif not check_if_on_loan():
            cur.execute(
                'SELECT DueDate FROM Loan WHERE BookNumber = "' + book_info[0] + '"')
            DueDate = cur.fetchone()[0]

            conn.close()
            return ("Book currently on Loan until: " + DueDate.strftime('%Y-%m-%d'), False)
        
        elif not check_if_exceed_loan_quota():
            conn.close()
            return ("Member loan quota exceeded", False)

        elif not check_fine():
            conn.close()
            return ("Member has outstanding fines", False)
        
        conn.commit()
        conn.close()
        

    def book_return(self, AccessionNumber, return_date):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        cur.execute(
            'SELECT MemberID from Loan where BookNumber = "' + AccessionNumber + '"')
        
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
        
        cur.execute(
            'DELETE FROM Loan WHERE MemberID = "' + book_info[1] + '"')
        conn.commit()

        if check_fine(): # need show member has outstanding fine even book return is successful
            conn.close()
            return ("Book return successful", True)
        else:
            conn.close()
            return ("Book returned successfully but has fines", False)

 
        
        conn.commit()
        conn.close()
        
        