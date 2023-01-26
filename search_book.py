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

#There are 5 fields in total, but can only search based on one of them
#Later supposed to be based on user inputs
Title = '' #The
Authors = 'Mar' #Mar
ISBN = '' #000001
Publisher = '' #Vintage
PublishYear = '' #1994

def decide_action():
    if Title:
        return 1
    elif Authors:
        return 2
    elif ISBN:
        return 3
    elif Publisher:
        return 4
    else:
        return 5

action = decide_action()
def perform_search():
    if action == 1:
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
            'Publisher, PublishYear FROM Book INNER JOIN Author ' +
            'ON Book.AccessionNumber = Author.BookNumber ' +
            'WHERE Title LIKE "%' +
            Title + '%"')
    elif action == 2: #Note this one
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
            'Publisher, PublishYear FROM Book INNER JOIN Author ' +
            'ON Book.AccessionNumber = Author.BookNumber ' +
            'WHERE AccessionNumber IN (SELECT BookNumber ' +
            'FROM Author WHERE AuthorName LIKE "%' +
            Authors + '%")')
    elif action == 3:
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
            'Publisher, PublishYear FROM Book INNER JOIN Author ' +
            'ON Book.AccessionNumber = Author.BookNumber ' +
            'WHERE ISBN LIKE "%' +
            ISBN + '%"')
    elif action == 4:
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
            'Publisher, PublishYear FROM Book INNER JOIN Author ' +
            'ON Book.AccessionNumber = Author.BookNumber ' +
            'WHERE Publisher LIKE "%' +
            Publisher + '%"')
    else:
        cur.execute(
            'SELECT AccessionNumber, Title, AuthorName, ISBN, ' +
            'Publisher, PublishYear FROM Book INNER JOIN Author ' +
            'ON Book.AccessionNumber = Author.BookNumber ' +
            'WHERE PublishYear LIKE "%' +
            PublishYear + '%"')
    result = cur.fetchall()
    for row in result:
        print(row)

perform_search()

conn.close()










