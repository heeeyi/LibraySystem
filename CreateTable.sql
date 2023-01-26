-- This is how comments are done in SQL;
CREATE TABLE Member (
	MemberID VARCHAR(10) NOT NULL,
	Name VARCHAR(35) NOT NULL,
	Faculty VARCHAR(15) NOT NULL,
	Phone VARCHAR(15) NOT NULL,
	Email VARCHAR(25) NOT NULL,
	PRIMARY KEY (MemberID));

CREATE TABLE Book (
	AccessionNumber VARCHAR(5) NOT NULL,
	Title VARCHAR(100) NOT NULL,
	ISBN VARCHAR(20) NOT NULL,
	Publisher VARCHAR(50) NOT NULL,
	PublishYear VARCHAR(5) NOT NULL,
	PRIMARY KEY (AccessionNumber));
	
CREATE TABLE Author (
	AuthorID INTEGER NOT NULL AUTO_INCREMENT,
	AuthorName VARCHAR(35) NOT NULL,
	BookNumber VARCHAR(5) NOT NULL,
	PRIMARY KEY (AuthorID),
	FOREIGN KEY (BookNumber) REFERENCES Book(AccessionNumber) 
		ON DELETE CASCADE ON UPDATE CASCADE);
-- If book deleted, its author information also deleted;
		
CREATE TABLE Loan (
	LoanID INTEGER NOT NULL AUTO_INCREMENT,
	BorrowDate DATE NOT NULL,
	DueDate DATE NOT NULL, -- This is derived;
	MemberID VARCHAR(10) NOT NULL,
	BookNumber VARCHAR(5) NOT NULL,
	PRIMARY KEY (LoanID),
	FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
		ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (BookNumber) REFERENCES Book(AccessionNumber)
		ON DELETE NO ACTION ON UPDATE CASCADE);
-- I feel Loan should be holding CURRENT book on loan;
-- So if the member has existing loan, should reject delete membership;
-- Same for book;

CREATE TABLE Reservation (
	ReserveID INTEGER NOT NULL AUTO_INCREMENT,
	ReserveDate DATE NOT NULL,
	MemberID VARCHAR(10) NOT NULL,
	BookNumber VARCHAR(5) NOT NULL,
	PRIMARY KEY (ReserveID),
	FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
		ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (BookNumber) REFERENCES Book(AccessionNumber)
		ON DELETE CASCADE ON UPDATE CASCADE);
-- If member or book deleted, the reservation is canceled

CREATE TABLE Fine (
	FineID INTEGER AUTO_INCREMENT,
	PayDate DATE,
	-- Amount DECIMAL(6,1) NOT NULL DEFAULT 0, can have 6 numbers with 1 dp;
	Amount INTEGER DEFAULT 0,
	MemberID VARCHAR(10) NOT NULL,
	PRIMARY KEY (FineID),
	FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
		ON DELETE NO ACTION ON UPDATE CASCADE);
-- This table is problematic. Supposed to store ALL fine information (Not just active ones)
-- So HOW to restrict membership deletion if he has active fine?
	
	
	