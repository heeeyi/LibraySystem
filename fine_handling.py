#THE FINE HANDLING ALGORITHM:

#The Check happens when actions including
#Delete member/ Borrow book/ Return book/ Reservat book are carried out
#SELECT xx FROM Loan -- that exceeds the due date

#If rowcount =/= 0, SELECT FROM Fine, see if the member already in Fine table
#Yes -- UPDATE; No -- INSERT
#Whatever the outcome, SELECT FROM Loan to re-calculate the fine
#Then insert/update the number inside

#THE FUNCTIONS:
#First check if has fine or not
#If yes, calculate fine
#Then insert into Fine
#Payment of the fine is independent, should be run separately

import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import pymysql
import csv
from datetime import date

load_dotenv()

PASSWORD = os.getenv('MY_SQL_PASSWORD')

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = PASSWORD,
    db = "library")
cur = conn.cursor()

#This function should be executed whenever the member wants to
#delete member/borrow book/return book/reserve book
def check_outstanding_fine(MemberID):
    cur.execute(
        'SELECT * FROM Loan WHERE DueDate < CURDATE() ' +
        'and MemberID = "' + MemberID + '"')
    if cur.rowcount != 0:
        return True
    else:
        return False

#This function calculate the total fine
def calculate_fine(MemberID):
    fine = 0
    cur.execute(
        'SELECT * FROM Loan WHERE DueDate < CURDATE() ' +
        'and MemberID = "' + MemberID + '"')
    result = cur.fetchall()
    for row in result:
        fine += (date.today() - row[2]).days
    return fine

#This function insert/update fine table
def insert_update_fine(MemberID):
    fine = calculate_fine(MemberID)
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

#insert_update_fine("A201B")

#This function check if has fine, if yes also handle payment
#Return a state of True/False, can be used to pop interfaces
def fine_payment(MemberID):
    cur.execute(
        'SELECT * FROM Fine WHERE MemberID = "' + MemberID + '"')
    if cur.rowcount == 0:
        return False
    else:
        cur.execute(
            'UPDATE Fine SET Amount = 0, PayDate = CURDATE() ' +
            'WHERE MemberID = "' + MemberID + '"')
        return True

success_state = fine_payment("A201B")
#print(success_state)
conn.commit()

conn.close()







