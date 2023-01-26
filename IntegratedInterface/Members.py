import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')


class Membership(object):

    def membership_creation(self,memberID, name, faculty, phone, email):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM Member WHERE MemberID = "' + memberID + '"')
        ExistMember = cur.rowcount
        #FieldLength = len(membership_info)
        if ExistMember == 0:
            #if FieldLength == 5:
            cur.execute(
                'INSERT INTO Member(MemberID, Name, Faculty, Phone, Email)' +
                'Values ("' + memberID + '", "'
                + name + '", "' + faculty + '","' +
                phone + '","' + email + '");')
            conn.commit()
            conn.close()
            return ("ALS Membership created", True)
        conn.close()
        return ("Member already exist;\nMissing or incomplete fields", False)

    def confirm_info_member(self, MemID):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        #Extract information, confirm cancellation details to be correct
        cur.execute(
            'SELECT MemberID, Name, Faculty, Phone, Email FROM Member ' +
            'WHERE MemberID = "' + MemID + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        output = cur.fetchone()
        conn.close()

        return (output, True)

    def membership_deletion(self,memberID):

        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute('SELECT * FROM Loan WHERE MemberID = "' + memberID + '"')
        LoanResult = cur.rowcount

        cur.execute('SELECT * FROM Reservation WHERE MemberID = "'
                    + memberID + '"')
        ReserveResult = cur.rowcount
        
        cur.execute('SELECT * FROM Fine WHERE MemberID = "' + memberID + '"')
        FineResult = cur.rowcount

        if (LoanResult == 0 and FineResult == 0 and ReserveResult == 0):
            cur.execute(
                'DELETE'+
                ' FROM Member'+
                ' WHERE MemberID = "' + memberID + '"')
            conn.commit()
            conn.close()
            return ("Membership successfully deleted", True)
        else:
            conn.close()
            return (
                "Member has loans,\nreservations or outstanding fines", False)
    
    def membership_update(self,memberID, name, faculty, phone, email):

        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
            
        cur.execute('SELECT * FROM Member WHERE MemberID = "' + memberID + '"')
        ExistMember = cur.rowcount
        if ExistMember == 0:
            conn.close()
            return ("No such member;\nMissing or incomplete fields", False)
        else:
            cur.execute(
            'UPDATE Member '+
            'SET Name = "' + name + '", Faculty = "' +
            faculty + '", Phone = "' + phone + '", Email = "' + email + '"' +
            ' WHERE MemberID =  "' + memberID + '"')
            conn.commit()
            conn.close()
            return ("ALS Membership updated", True)
    
        

        


        





