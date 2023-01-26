import pymysql
import csv

#Connect to database

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "XXX",
    db = "library")
cur = conn.cursor()


#Insert into Member Table

f = open("LibMems.txt","r", encoding = "utf-8")
lines = f.readlines()
count = 0
for line in lines:
    if count > 0:
        row = line.strip().split(',')
        cur.execute(
            "INSERT INTO Member(MemberID, Name, Faculty, Phone, Email) " +
            "Values (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4]))
    count += 1
f.close()

#Insert into Book Table

h = open("LibBooks.txt","r", encoding = "utf-8")
reader = csv.reader(h, delimiter = ',', skipinitialspace = True, quotechar = '"')
count = 0
for row in reader:
    if count > 0:
        #print(row[1])
        cur.execute(
            "INSERT INTO Book(AccessionNumber, Title, ISBN, Publisher, PublishYear) " +
            "Values (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[-3], row[-2], row[-1]))
    count += 1
h.close()

#Insert into Author Table

f2 = open("LibBooks.txt", "r", encoding = "utf-8")
reader = csv.reader(f2, delimiter = ',',
                    skipinitialspace = True, quotechar = '"')
#Actually here author information is in order
#At most 3 authors, row length 8
count = 0
for row in reader:
    if count > 0:
        Book = row[0]
        for i in range(2, 5):
            if row[i] != "":
               cur.execute(
                   "INSERT INTO Author (AuthorName, BookNumber) " +
                   "VALUES (%s, %s)",
                   (row[i], Book))
    count += 1
f2.close()

conn.commit()
conn.close()

#The book title is really too long...
#ALTER TABLE Book MODIFY COLUMN Title VARCHAR(100);

