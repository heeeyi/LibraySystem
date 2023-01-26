import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv
from datetime import date

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Fine(object):

    def check_outstanding_fine(self, MemberID):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM Loan WHERE DueDate < CURDATE() ' +
            'and MemberID = "' + MemberID + '"')
        if cur.rowcount != 0:
            conn.close()
            return True
        else:
            conn.close()
            return False

    def calculate_fine(self, MemberID):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        fine = 0
        cur.execute(
            'SELECT * FROM Loan WHERE DueDate < CURDATE() ' +
            'and MemberID = "' + MemberID + '"')
        result = cur.fetchall()
        for row in result:
            fine += (date.today() - row[2]).days
        conn.close()
        return fine

    def insert_update_fine(self, MemberID):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        fine = 0
        cur.execute(
            'SELECT * FROM Loan WHERE DueDate < CURDATE() ' +
            'and MemberID = "' + MemberID + '"')
        result = cur.fetchall()
        for row in result:
            fine += (date.today() - row[2]).days
        cur.execute(
            'SELECT * FROM Fine WHERE MemberID = "' + MemberID + '"')
        if cur.rowcount == 0:
            cur.execute(
                'INSERT INTO Fine (Amount, MemberID) ' +
                'VALUES (' + str(fine) + ', "' + MemberID + '")')
        else:
            cur.execute(
                'UPDATE Fine SET Amount = ' + str(fine) +
                ' WHERE MemberID =  "' + MemberID + '"')
        conn.commit()
        conn.close()
        return ("Fine imposed on member", True)

    def confirm_info_fine(self, MemID):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        #Extract information, confirm cancellation details to be correct
        cur.execute(
            'SELECT MemberID FROM Member ' +
            'WHERE MemberID = "' + MemID + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        output = cur.fetchone()
        conn.close()

        return (output, True)

    def fine_payment(self, MemberID, Amount, Date):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute(
            'SELECT * FROM Fine WHERE MemberID = "' +
            MemberID + '" and Amount != 0')
        if cur.rowcount == 0:
            conn.close()
            return ("Member has no fine", False)
        else:
            result = cur.fetchone()
            if Amount != int(result[2]):
                conn.close()
                return ("Incorrect fine payment amount", False)      
            cur.execute(
                'UPDATE Fine SET Amount = 0, PayDate = DATE("' + Date + '") ' +
                'WHERE MemberID = "' + MemberID + '"')
            conn.commit()
            conn.close()
            return ("Fine successfully paid", True)


        

        
        







    
