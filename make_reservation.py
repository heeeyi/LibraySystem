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
    ResDate = "2021-12-06"
    MemID = "A301C"
    BookNum = "A06"
    return (ResDate, MemID, BookNum)
#Here supposed to be retrieving from user input
#Now just use a proxy

info = retrieve_info()

def check_success():
    cur.execute(
        'SELECT * FROM Loan WHERE BookNumber = "' + info[2] + '"')
    if cur.rowcount == 0:
        return 1 #The book is not on loan, can directly borrow
    cur.execute(
        'SELECT * FROM Reservation WHERE BookNumber = "' + info[2] + '"')
    if cur.rowcount != 0:
        return 2 #The book already reserved
    cur.execute(
        'SELECT COUNT(*) as ResNum FROM Reservation ' +
        'WHERE MemberID = "' + info[1] + '"')
    count = cur.fetchone()
    if count[0] >= 2:
        return 3 #The member already has 2 loans
    cur.execute("SELECT IFNULL(SUM(Amount), 0) as fine FROM Fine " +
                'WHERE MemberID = "' + info[1] + '"')
    count = cur.fetchone()
    if count[0] > 0:
        return 4 #The member has fine
    return 0

success = check_success()

def create_reservation():
    if success == 0:
        cur.execute(
            'INSERT INTO Reservation (ReserveDate, MemberID, BookNumber) ' +
            'VALUES (DATE("' + info[0] + '"), "' +
            info[1] + '", "' + info[2] + '")')
    else:
        pass

create_reservation()

conn.commit()
conn.close()


#The Error on SQL side:
#pymysql.err.OperationalError

