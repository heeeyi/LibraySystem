-- membership --
-- membership creation -- 
INSERT INTO Member(MemberID,Name, Faculty, Phone, Email)
Values (id,name, faculty, phone, email);

-- membership deletion --
DELETE
FROM Member
WHERE MemberID = x;
-- all reserve request will be cancelled
DELETE
FROM Reservation
WHERE MemberID = x;
-- deletion condition -- 
SELECT LoanID
FROM Loan
WHERE MemberID = x;

SELECT Amount 
FROM Fine 
WHERE MemberID = x;


-- membership update -- 
UPDATE Member
SET Name = 'a', Faculty = 'b', Phone = 'c', Email = 'e'
WHERE MemberID = x;