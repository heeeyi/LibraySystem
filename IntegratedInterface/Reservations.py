import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Reservation(object):
    def make_reservation(self, ResDate, MemID, BookNum):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM Loan WHERE BookNumber = "' + BookNum + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("The book can be directly loaned", False)
        cur.execute(
            'SELECT * FROM Reservation WHERE BookNumber = "' + BookNum + '"')
        if cur.rowcount != 0:
            conn.close()
            return ("The book is already reserved", False)
        cur.execute(
            'SELECT COUNT(*) as ResNum FROM Reservation ' +
            'WHERE MemberID = "' + MemID + '"')
        count = cur.fetchone()
        if count[0] >= 2:
            conn.close()
            return ("The member already has 2 loans", False)
        cur.execute(
            "SELECT IFNULL(SUM(Amount), 0) as fine FROM Fine " +
            'WHERE MemberID = "' + MemID + '"')
        count = cur.fetchone()
        if count[0] > 0:
            conn.close()
            return ("The member has outstanding fine", False)
        cur.execute(
            'INSERT INTO Reservation (ReserveDate, MemberID, BookNumber) ' +
            'VALUES (DATE("' + ResDate + '"), "' +
            MemID + '", "' + BookNum + '")')
        conn.commit()
        conn.close()
        return ("Reservation successful", True)


    def confirm_info_reservation(self, Date, MemID, BookNum):
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
        output = output + cur.fetchone()
        output = output + (Date,)
        conn.close()

        return (output, True)


    def delete_reservation(self, CancelDate, MemID, BookNum):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute(
            'SELECT * FROM Reservation ' +
            'WHERE BookNumber = "' + BookNum + '" and ' +
            'MemberID = "' + MemID + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Member has no such reservation", False)
        cur.execute(
            'DELETE FROM Reservation WHERE MemberID = "' +
            MemID + '" and BookNumber = "' +
            BookNum + '"')
        conn.commit()
        conn.close()
        return ("Reservation deletion successful", True)
        













