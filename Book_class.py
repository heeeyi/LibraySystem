import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv


load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Book(object):

    def book_acquisition(self,AN, title, isbn, publisher, year):

        book_info = (AN, title, isbn, publisher, year)

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute('SELECT * FROM Book WHERE AccessionNumber = "' + book_info[0] + '"')
        ExistBook = cur.rowcount
        FieldCount = len(book_info)
        if ExistBook == 0 and FieldCount == 5:
            cur.execute(
                'INSERT INTO Book(AccessionNumber, Title, ISBN, Publisher, PublishYear)'+
                'Values ("' + book_info[0] + '", "' + book_info[1] + '", "' + book_info[2] + '","' + book_info[3] + '","' + book_info[-1] + '");'
            )
            conn.commit()
            conn.close()
            return ("New book added into library" , True) #output success window 
        else:
            conn.close()
            return ("Book already added, duplicate, missing or incomplete fields", False)

    
    def book_withdrawal(self,AN):

        conn = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute('SELECT * FROM Book WHERE AccessionNumber = "' + AN + '"')
        #Actually here needs further working, how to put all the Authors in 1 cell
        result = cur.fetchall()
        output_list = []
        for row in result:
            output_list.append(row)
        
        print(output_list)

        cur.execute('SELECT * FROM Loan WHERE BookNumber = "' + AN + '"')
        Loan_Result = cur.fectall()
        cur.execute('SELECT * FROM Reservation WHERE BookNumber = "' + AN + '"')
        Res_Result = cur.fectall()

        if Loan_Result != 0:
            conn.close()
            return ("Book is currently on Loan", False)
            
        if Res_Result != 0:
            conn.close()
            return ("Book is currently reserved", False)

        cur.execute('DELETE FROM Book WHERE AccessionNumber = "' + AN + '"')
        conn.commit()
        
        conn.close()

        return ("Outdated Book is Withdrawed.", True)

#testing
a = Book()
a.book_withdrawal('A50')

        
        