-- Loan -- 
-- check_reservation_--
SELECT * FROM Reservation WHERE BookNumber = x;

-- check loan --
SELECT * FROM Loan WHERE BookNumber = x;

-- check loan quota （if cur.rowcount == 2 return false) --
SELECT * FROM Loan WHERE MemberID = x;

-- check fine --
SELECT * FROM Fine WHERE MemberID = x;

-- execute book borrowing --
-- borrow_date_add_14_days use datetime -- 
INSERT INTO Loan(BorrowDate, DueDate, MemberID, BookNumber)
VALUES(borrowdate, borrowdate_add_14_days, id, accessionNumber);

-- execute book return -- 
DELETE FROM Loan WHERE MemberID = x;

