-- 11. Search

-- Book search: a member can perform a search on the collection of books
-- specifying any word in AN, title, isbn, publisher, public year; and any word in the authors
-- Same for search in title, isbn, publisher, public year etc
SELECT Title, AuthorName, ISBN, Publisher, PublishYear
FROM Book
INNER JOIN Author ON Book.AccessionNumber = Author.BookNumber
WHERE AccessionNumber LIKE "A0%" 

-- If search authors
-- Here should use IN not =, because the subquery returns more than 1 row
-- And must use a join method, otherwise will return a LOT more rows
SELECT AccessionNumber, Title, AuthorName, ISBN, Publisher, PublishYear
FROM Book
INNER JOIN Author ON Book.AccessionNumber = Author.BookNumber
WHERE AccessionNumber IN (SELECT BookNumber 
    FROM Author 
    WHERE AuthorName LIKE "%Mar%");

    
-- 12. Books on Loan

-- Some self test cases:
INSERT INTO Loan (BorrowDate, DueDate, MemberID, BookNumber)
VALUES (DATE("2021-12-01"), DATE("2021-12-15"), "A201B", "A06");

INSERT INTO Loan (BorrowDate, DueDate, MemberID, BookNumber)
VALUES (DATE("2022-01-12"), DATE("2021-01-26"), "A801H", "A03"); -- well here mistake
UPDATE Loan SET BorrowDate = DATE("2021-01-12") WHERE BookNumber = "A03";

INSERT INTO Loan (BorrowDate, DueDate, MemberID, BookNumber)
VALUES (CURDATE(), DATE("2022-03-04"), "A401D", "A22");
-- Well CURDATE() seems to have the correct format, but not CURDATE() + 1
-- I have to type manually

DELETE FROM Loan LIMIT 10;
-- Better not randomly delete, otherwise the auto_increment number actually do mess up

SELECT b.AccessionNumber, b.Title, a.AuthorName, b.ISBN, b.Publisher, b.PublishYear
FROM Author a INNER JOIN Book b
ON a.BookNumber = b.AccessionNumber
INNER JOIN Loan l
ON b.AccessionNumber = l.BookNumber
-- It displays the author as separate rows


-- 13. Books on Reservation

SELECT b.AccessionNumber, b.Title, m.MemberID, m.Name
FROM Book b INNER JOIN Reservation r
ON b.AccessionNumber = r.BookNumber
INNER JOIN Member m
ON r.MemberID = m.MemberID


-- 8. Reservation
INSERT INTO Reservation (ReserveDate, MemberID, BookNumber)
VALUES (DATE("2021-12-06"), "A301C", "A06")

INSERT INTO Reservation (ReserveDate, MemberID, BookNumber)
VALUES (CURDATE(), "A201B", "A22"); 
-- This will only be successful if the book is currently on loan, not reserved
-- and this member has less than 2 reservations, no outstanding fine

-- checks:
SELECT * FROM Loan WHERE BookNumber = "x";
SELECT * FROM Reservation WHERE BookNumber = "x";
SELECT COUNT(*) as ResNum FROM Reservation WHERE MemberID = 'x';
SELECT IFNULL(SUM(Amount), 0) as fine FROM Fine WHERE MemberID = "A301C";


-- 9. Cancel Reservation
DELETE FROM Reservation WHERE MemberID = 'x' and BookNumber = 'x';

-- Retrieve information from database
SELECT AccessionNumber, Title FROM Book WHERE AccessionNumber = 'x';
SELECT MemberID, Name FROM Member WHERE MemberID = 'x';
SELECT * FROM Reservation WHERE MemberID = 'x' and BookNumber = 'x';


-- 10. Fine Payment
-- Rationale: The moment the member come to 
SELECT * FROM Loan 
WHERE DueDate < CURDATE() and MemberID = 'x';

SELECT * FROM Fine WHERE MemberID = 'x';
INSERT INTO Fine (Amount, MemberID) VALUES (60, 'x');
UPDATE Fine SET Amount = 66 WHERE MemberID = 'x';

SELECT * FROM Fine WHERE MemberID = 'x' and Amount != 0;
UPDATE Fine SET Amount = 0, PayDate = CURDATE() WHERE MemberID = 'x';


UPDATE Fine SET Amount = 66, PayDate = NULL WHERE MemberID = "A201B";

-- 14. Members with Fine
SELECT m.MemberID, m.Name, m.Faculty, m.Phone, m.Email FROM Member m 
INNER JOIN Fine f 
ON m.MemberID = f.MemberID 
WHERE f.Amount != 0;

-- 15. Books on loan to MEMBER

SELECT b.AccessionNumber, b.Title, a.AuthorName, b.ISBN, b.Publisher, b.PublishYear
FROM Author a INNER JOIN Book b
ON a.BookNumber = b.AccessionNumber
INNER JOIN Loan l ON b.AccessionNumber = l.BookNumber
WHERE l.MemberID = 'x';
