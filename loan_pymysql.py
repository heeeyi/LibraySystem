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

conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = PASSWORD,
    db = "library")
cur = conn.cursor()

####link to click####
Borrow = 'yes'
Return = ''

###insertion of data depends on insertion. 
###set as some random value first
########### change AN AND MEMBERID IF U WANNA TEST !!!!!!!!!!!!!!!


def retrieve_info():
    AN = 'A01'
    MemberID = 'A02B'
    return (AN, MemberID)

book_info = retrieve_info()

def decide_action():
    if Borrow:
        return 1
    if Return:
        return 2
action = decide_action()


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

def perform_action():
    # borrow book action
    if action == 1:
        if check_if_on_reservation() and check_if_on_loan() and check_if_exceed_loan_quota() and check_fine():
            # PROBLEM! date obj need convert to sth else
            BorrowDate = datetime.today().strftime('%Y-%m-%d')
            Valid_Date = timedelta(days = 14)
            DueDate = (datetime.today() + Valid_Date).strftime('%Y-%m-%d')
            cur.execute(
                'INSERT INTO Loan(BorrowDate, DueDate, MemberID, BookNumber)'+
                'VALUES("' + BorrowDate + '", "' + DueDate + '", "' + book_info[1] + '", "' + book_info[0] + '");'
            )
    # return book action
    elif action == 2:
        check_fine() # need show member has outstanding fine even book return is successful
        cur.execute(
            'DELETE FROM Loan WHERE MemberID = "' + book_info[1] + '"')

perform_action()
conn.commit()
conn.close()
        
        