-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-02-2020 a las 23:11:43
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: 'turnero'
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'atencion'
--

--
-- Volcado de datos para la tabla 'atencion'
--


-- Estructura de tabla para la tabla 'cajas'
--

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


CREATE TABLE "turns" (
	"TurnsID"	INTEGER,
	"Identification"	varchar(15) NOT NULL,
	"Description"	TEXT,
	"CreatedAt"	datetime NOT NULL DEFAULT (datetime('now')),
	"UpdateAt"	datetime,
	"DeletedAt"	datetime,
	"status"	varchar(15) NOT NULL DEFAULT available,
	"IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
	PRIMARY KEY("TurnsID" AUTOINCREMENT)
);

CREATE TABLE "FinishedShift" (
	"FinishedShiftID"	INTEGER,
	"UserID"	INTEGER NOT NULL,
	"TurnsID"	INTEGER NOT NULL,
	"Description"	TEXT,
	"Status"	TEXT NOT NULL DEFAULT 'attending',
	"CreatedAt"	datetime NOT NULL DEFAULT (datetime('now')),
	"DeletedAt"	datetime,
	"IsEnabled"	BOOLEAN NOT NULL DEFAULT (true),
	PRIMARY KEY("FinishedShiftID" AUTOINCREMENT)
);


-- Available
-- Attending
-- Finished
-- --------------------------------------------------------

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
-- Volcado de datos para la tabla 'info_empresa'
--

-- --------------------------------------------------------

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
 
--
-- Estructura de tabla para la tabla 'turnos'
--



--
-- Volcado de datos para la tabla 'turnos'
--

--
-- Estructura de tabla para la tabla 'usuarios'
--


    --   'idCaja' int(11) NOT NULL,
    --   'fecha_alta' datetime NOT NULL,
    --   'fecha_actualizacion' datetime NOT NULL


--
-- Volcado de datos para la tabla 'usuarios'
--


-- Índices para tablas volcadas
--

--
-- Indices de la tabla 'atencion'
--
ALTER TABLE 'atencion'
  ADD PRIMARY KEY ('id');

--
-- Indices de la tabla 'cajas'
--
ALTER TABLE 'cajas'
  ADD PRIMARY KEY ('id');

--
-- Indices de la tabla 'info_empresa'
--
ALTER TABLE 'info_empresa'
  ADD PRIMARY KEY ('id');

--
-- Indices de la tabla 'noticias'
--
ALTER TABLE 'noticias'
  ADD PRIMARY KEY ('id');

--
-- Indices de la tabla 'turnos'
--
ALTER TABLE 'turnos'
  ADD PRIMARY KEY ('id');

--
-- Indices de la tabla 'usuarios'
--
ALTER TABLE 'usuarios'
  ADD PRIMARY KEY ('id');

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla 'atencion'
--
ALTER TABLE 'atencion'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=405;

--
-- AUTO_INCREMENT de la tabla 'cajas'
--
ALTER TABLE 'cajas'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla 'info_empresa'
--
ALTER TABLE 'info_empresa'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla 'noticias'
--
ALTER TABLE 'noticias'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla 'turnos'
--
ALTER TABLE 'turnos'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=442;

--
-- AUTO_INCREMENT de la tabla 'usuarios'
--
ALTER TABLE 'usuarios'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
