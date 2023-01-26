import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = PASSWORD,
    db = "library")
cur = conn.cursor()

def retrieve_info():
    MemID = "A301C"
    BookNum = "A06"
    CancelDate = "2021-12-08"
    return (MemID, BookNum, CancelDate)
#Here supposed to be retrieving from user input
#Now just use a proxy

info = retrieve_info()

#Then delete interface will pop a window check information
#Also need to retrieve data from Book and Member
def confirm_window():
    cur.execute(
        'SELECT AccessionNumber, Title FROM Book ' +
        'WHERE AccessionNumber = "' + info[1] + '"')
    output = cur.fetchone()
    cur.execute(
        'SELECT MemberID, Name FROM Member ' +
        'WHERE MemberID = "' + info[0] + '"')
    output = output + cur.fetchone()
    output = output + (info[2],)
    return output

confirm_delete = confirm_window() 

def check_success():
    cur.execute(
        'SELECT * FROM Reservation WHERE MemberID = "' +
        info[0] + '" and BookNumber = "' +
        info[1] + '"')
    if cur.rowcount == 0:
        return False
    return True

success = check_success()

def cancel_reservation():
    if success:
        cur.execute(
            'DELETE FROM Reservation WHERE MemberID = "' +
            info[0] + '" and BookNumber = "' +
            info[1] + '"')
    else:
        pass

cancel_reservation()

conn.commit()
conn.close()


