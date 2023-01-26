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

def perform_report():
    cur.execute(
        'SELECT b.AccessionNumber, b.Title, A.AuthorName, b.ISBN, ' +
        'b.Publisher, b.PublishYear FROM Author a INNER JOIN Book b ' +
        'ON a.BookNumber = b.AccessionNumber ' +
        'INNER JOIN Loan l ' +
        'ON b.AccessionNumber = l.BookNumber')
    #Actually here needs further working, how to put all the Authors in 1 cell
    result = cur.fetchall()
    for row in result:
        print(row)

perform_report()

conn.close()
