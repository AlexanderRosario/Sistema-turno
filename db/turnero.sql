

CREATE TABLE Users (
	"UserID"	INTEGER NOT NULL,
	"UserName"	varchar(50) NOT NULL UNIQUE,
	"Password"	varchar(255) NOT NULL,
	"UserRol"	varchar(25) DEFAULT 'cajero',
	"CreatedAt"	datetime NOT NULL DEFAULT (datetime('now')),
	"DeletedAt"	datetime,
	"IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE Cashiers (
  CashierID INTEGER ,
  Name varchar(20) NOT NULL UNIQUE,
  CreatedAt  DATETIME DEFAULT (datetime('now')) NOT NULL ,
  DeletedAt datetime,
  IsEnabled BOOLEAN NOT NULL DEFAULT(true),
  PRIMARY KEY("CashierID" AUTOINCREMENT)
);

CREATE TABLE CashierUsers (
  CashierUsersID  INTEGER PRIMARY KEY AUTOINCREMENT,
  CashierID INTEGER NOT NULL,
  UserID INTEGER NOT NULL,
  CreatedAt datetime DEFAULT (datetime('now')) NOT NULL ,
  DeletedAt datetime,
  IsEnabled BOOLEAN NOT NULL  DEFAULT(true),
  FOREIGN KEY (CashierID) REFERENCES Cashiers(CashierID),
  FOREIGN KEY (UserID) REFERENCES Users (UserID)
) 


CREATE TABLE Turns (
	"TurnsID"	INTEGER,
	"IdentificationClient"	varchar(15) NOT NULL,
  "UserID"	INTEGER ,
	"ServiceID"	INTEGER,
  "AvailableAt"	datetime NOT NULL DEFAULT (datetime('now')),
	"AttendedAt"	datetime,
	"FinishedAt"	datetime,
	"status"	varchar(15) NOT NULL DEFAULT available,
	"IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
	PRIMARY KEY("TurnsID" AUTOINCREMENT),
  FOREIGN KEY (ServiceID) REFERENCES Service (ServiceID)
);

-- Available
-- Attending
-- Finished
-- --------------------------------------------------------
CREATE TABLE Services (
  "ServiceID" INTEGER,
  "ServiceName" varchar(100) NOT NULL ,
  "CreatedAt" datetime DEFAULT (datetime('now')) NOT NULL ,
  "DeletedAt" datetime,
  "IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
  PRIMARY KEY("ServiceID" AUTOINCREMENT)
);


-- CREATE TABLE "FinishedShift" (
-- 	"FinishedShiftID"	INTEGER,
-- 	"UserID"	INTEGER NOT NULL,
-- 	"TurnsID"	INTEGER NOT NULL,
-- 	"Description"	TEXT,
-- 	"Status"	TEXT NOT NULL DEFAULT 'attending',
-- 	"CreatedAt"	datetime NOT NULL DEFAULT (datetime('now')),
-- 	"DeletedAt"	datetime,
-- 	"IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
-- 	PRIMARY KEY("FinishedShiftID" AUTOINCREMENT)
-- );


SELECT * FROM InfoBusiness

UPDATE InfoBusiness SET Logo = 'images\cash.png'

CREATE TABLE "InfoBusiness" (
  "ID" INTEGER,
  "Logo" varchar(100)   NOT NULL,
  "Name" varchar(100)   NOT NULL,
  "address" varchar(100)   NOT NULL,
  "Phone" varchar(100)   NOT NULL,
  "email" varchar(100)   NOT NULL,
  "UpdateAt"	datetime NOT NULL DEFAULT (datetime('now')),
  	PRIMARY KEY("id" AUTOINCREMENT)
) 

--
-- Estructura de tabla para la tabla 'noticias'
--

CREATE TABLE 'noticias' (
  'id' int(11) NOT NULL,
  'noticia' varchar(255) COLLATE utf8_spanish2_ci NOT NULL,
  'fecha' datetime NOT NULL
) 

-- --------------------------------------------------------
SELECT Users.UserName,Cashiers.Name,COUNT(*),FinishedShift.DeletedAt FROM FinishedShift
INNER JOIN users on users.UserID = FinishedShift.UserID
INNER JOIN CashierUsers on CashierUsers.UserID = Users.UserID
INNER JOIN Cashiers on Cashiers.CashierID = CashierUsers.CashierID 
WHERE status= 'finished' 
	GROUP BY  FinishedShift.UserID
 