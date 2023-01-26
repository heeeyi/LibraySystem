import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')


class Membership(object):

    def check_creation_state(self,memberID, name, faculty, phone, email):
        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        membership_info = (memberID, name, faculty, phone, email)
        
        cur.execute('SELECT * FROM Member WHERE MemberID = "' + memberID + '"')
        ExistMember = cur.rowcount
        FieldLength = len(membership_info)
        if ExistMember == 0:
            if FieldLength == 5:
                conn.close()
                return 1 #success window
            else :
                conn.close()
                return 0 #error window

    def membership_creation(self,memberID, name, faculty, phone, email):

        #membership_info = (memberID, name, faculty, phone, email)
        self.memberID = memberID
        self.name = name
        self.faculty = faculty
        self.phone = phone
        self.email = email
        
        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        
        if self.check_creation_state(memberID, name, faculty, phone, email):
            cur.execute(
                'INSERT INTO Member(MemberID, Name, Faculty, Phone, Email)' +
                'Values ("' + memberID + '", "' + name + '", "' + faculty + '","' + phone + '","' + email + '");'
            )
            conn.commit()
            conn.close()

    def check_deletion_state(self,memberID):

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute('SELECT * FROM Loan WHERE MemberID = "' + memberID + '"')
        LoanResult = cur.rowcount
        
        cur.execute('SELECT * FROM Fine WHERE MemberID = "' + memberID + '"')
        FineResult = cur.rowcount

        if (LoanResult == 0 & FineResult == 0):
            conn.close()
            return 1
        else:
            conn.close()
            return 0
    
    def membership_deletion(self,memberID):

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        
        if self.check_deletion_state(memberID):
            cur.execute(
                'DELETE'+
                ' FROM Member'+
                ' WHERE MemberID = "' + memberID + '"')

            cur.execute(
                'DELETE'+
                ' FROM Reservation'+
                ' WHERE MemberID = "' + memberID + '"')
            
            conn.commit()
            conn.close()

    
    def membership_update(self,memberID, name, faculty, phone, email):

        membership_updated_info = (memberID, name, faculty, phone, email)

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        def check_update_state(memberID):
            conn = pymysql.connect(
                host = "127.0.0.1",
                user = "root",
                password = PASSWORD,
                db = "library")
            cur = conn.cursor()
            
            cur.execute('SELECT * FROM Member WHERE MemberID = "' + memberID + '"')
            ExistMember = cur.rowcount
            FieldLength = len(membership_updated_info)
            if ExistMember == 0 or FieldLength != 5:
                conn.close()
                return 0
            else:
                conn.close()
                return 1
    
        if check_update_state(memberID):
            cur.execute(
            'UPDATE Member '+
            'SET Name = "' + name + '", Faculty = "' + faculty + '", Phone = "' + phone + '", Email = "' + email + '"' +
            ' WHERE MemberID =  "' + memberID + '"')
            
            conn.commit()
            conn.close()



#testing
a = Membership()
a.membership_update('A02C','sally','abc','123','123@als.edu')
        


        





