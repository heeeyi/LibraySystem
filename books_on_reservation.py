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
        'SELECT b.AccessionNumber, b.Title, m.MemberID, m.Name ' +
        'FROM Book b INNER JOIN Reservation r ' +
        'ON b.AccessionNumber = r.BookNumber ' +
        'INNER JOIN Member m ON r.MemberID = m.MemberID')
    result = cur.fetchall()
    for row in result:
        print(row)
perform_report()

conn.close()
