import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

#conn.close()

class Report(object):
    def concat_arthor(self,original_result):
        output_list = []
        book_number=[]
        for row in original_result:
            if row[0] not in book_number:
                book_number.append(row[0])
                output_list.append(list(row))
            else:
                output_list[book_number.index(row[0])][2]+=', '+row[2]
        return output_list
    
    def decide_action(self, Title, Authors, ISBN, Publisher, PublishYear):
        if Title:
            return 1
        elif Authors:
            return 2
        elif ISBN:
            return 3
        elif Publisher:
            return 4
        elif PublishYear:
            return 5
        return 0
    
    def search_book(self, Title, Authors, ISBN, Publisher, PublishYear):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        action=self.decide_action(Title, Authors, ISBN, Publisher, PublishYear)
        if action == 1:
            cur.execute(
                'SELECT AccessionNumber, Title, AuthorName, ISBN, '+
                'Publisher, PublishYear FROM Book INNER JOIN Author '+
                'ON Book.AccessionNumber = Author.BookNumber '+
                'WHERE CONCAT(" ",Title," ") '+
                'LIKE "% '+ Title+' %"')
            
        elif action == 2: #Note this one
            cur.execute(
                'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
                'Publisher, PublishYear FROM Book INNER JOIN Author ' +
                'ON Book.AccessionNumber = Author.BookNumber ' +
                'WHERE AccessionNumber IN (SELECT BookNumber ' +
                'FROM Author WHERE CONCAT(" ",AuthorName," ") LIKE "% ' +
                Authors + ' %")')
        elif action == 3:
            cur.execute(
                'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
                'Publisher, PublishYear FROM Book INNER JOIN Author ' +
                'ON Book.AccessionNumber = Author.BookNumber ' +
                'WHERE CONCAT(" ",ISBN," ") LIKE "% ' +
                ISBN + ' %"')
        elif action == 4:
            cur.execute(
                'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
                'Publisher, PublishYear FROM Book INNER JOIN Author ' +
                'ON Book.AccessionNumber = Author.BookNumber ' +
                'WHERE  CONCAT(" ",Publisher," ") LIKE "% ' +
                Publisher + ' %"')
        elif action == 5:
            cur.execute(
                'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
                'Publisher, PublishYear FROM Book INNER JOIN Author ' +
                'ON Book.AccessionNumber = Author.BookNumber ' +
                'WHERE PublishYear LIKE "%' +
                PublishYear + '%"')
        result = cur.fetchall()
        final_result=self.concat_arthor(result)
        conn.close()
        return final_result

    def books_on_loan(self):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT b.AccessionNumber, b.Title, A.AuthorName, b.ISBN, ' +
            'b.Publisher, b.PublishYear FROM Author a INNER JOIN Book b ' +
            'ON a.BookNumber = b.AccessionNumber ' +
            'INNER JOIN Loan l ' +
            'ON b.AccessionNumber = l.BookNumber')
        #Actually here needs further working, how to put all the Authors in 1 cell
        result = cur.fetchall()
        final_result=self.concat_arthor(result)
        conn.close()
        return final_result

    def books_on_reservation(self):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT b.AccessionNumber, b.Title, m.MemberID, m.Name ' +
            'FROM Book b INNER JOIN Reservation r ' +
            'ON b.AccessionNumber = r.BookNumber ' +
            'INNER JOIN Member m ON r.MemberID = m.MemberID')
        result = cur.fetchall()
        output_list = []
        for row in result:
            output_list.append(row)
            
        conn.close()
        return output_list

    def outstanding_fines(self):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT m.MemberID, m.Name, m.Faculty, m.Phone, m.Email ' +
            'FROM Member m INNER JOIN Fine f ' +
            'ON m.MemberID = f.MemberID ' +
            'WHERE f.Amount != 0')
        result = cur.fetchall()
        output_list = []
        for row in result:
            output_list.append(row)
            
        conn.close()
        return output_list

    def books_on_loan_to_member(self, Member):
        conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = PASSWORD,
            db = "library")
        cur = conn.cursor()
        cur.execute(
            'SELECT b.AccessionNumber, b.Title, A.AuthorName, b.ISBN, ' +
            'b.Publisher, b.PublishYear FROM Author a INNER JOIN Book b ' +
            'ON a.BookNumber = b.AccessionNumber ' +
            'INNER JOIN Loan l ON b.AccessionNumber = l.BookNumber ' +
            'WHERE l.MemberID = "' + Member + '"')
        result = cur.fetchall()
        final_result=self.concat_arthor(result)
        conn.close()
        return final_result
        

         
            














