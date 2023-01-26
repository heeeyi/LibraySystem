import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv


load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

class Book(object):

    def book_acquisition(self, AN, title, author, isbn, publisher, year):

        book_info = (AN, title, author, isbn, publisher, year)

        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute(
            'SELECT * FROM Book WHERE AccessionNumber = "' +
            book_info[0] + '"')
        ExistBook = cur.rowcount
        #FieldCount = len(book_info)
        if ExistBook == 0:
            cur.execute(
                'INSERT INTO Book(AccessionNumber, Title, ISBN, Publisher, PublishYear)'+
                'Values ("' + book_info[0] + '", "' + book_info[1] +
                '", "' + book_info[3] + '","' + book_info[4] + '","'
                + book_info[-1] + '");'
            )
            conn.commit()            
            author_list = author.split(",")
            for author in author_list:
                cur.execute(
                    'INSERT INTO Author(AuthorName, BookNumber)' +
                    'Values ("' + author.strip() + '","' +
                    book_info[0] +'");'
                )
            conn.commit()
            conn.close()
            return ("New book added into library" , True) #output success window 
        else:
            conn.close()
            return (
                "Book already added, duplicate, missing or incomplete fields",
                False)


    def concat_author(self,original_result):
        output_list = []
        book_number=[]
        for row in original_result:
            if row[0] not in book_number:
                book_number.append(row[0])
                output_list.append(list(row))
            else:
                output_list[book_number.index(row[0])][2]+=', '+row[2]
        return output_list

    def confirm_info_book(self, BookNum):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        #Extract information, confirm cancellation details to be correct
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, '+
            'Publisher, PublishYear FROM Book INNER JOIN Author '+
            'ON Book.AccessionNumber = Author.BookNumber '+
            'WHERE AccessionNumber = "' + BookNum + '"')
        if cur.rowcount == 0:
            conn.close()
            return ("Incorrect information", False)
        result = cur.fetchall()
        output = self.concat_author(result)[0]
        conn.close()

        return (output, True)

    
    def book_withdrawal(self,AN):

        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()

        cur.execute('SELECT * FROM Loan WHERE BookNumber = "' + AN + '"')
        Loan_Result = cur.rowcount
        cur.execute('SELECT * FROM Reservation WHERE BookNumber = "' + AN + '"')
        Res_Result = cur.rowcount

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


        
        
