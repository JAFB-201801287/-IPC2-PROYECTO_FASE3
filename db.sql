DROP DATABASE banca_virtual;
CREATE DATABASE banca_virtual;
USE banca_virtual;

CREATE TABLE Cliente (
	cui BIGINT PRIMARY KEY NOT NULL,
    nit BIGINT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento VARCHAR(30) NOT NULL
);

CREATE TABLE Empresa (
	id_empresa INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    nombre_comercial VARCHAR(100) NOT NULL,
	nombre_representante VARCHAR(150) NOT NULL,
    tipo_empresa VARCHAR(150) NOT NULL
);

CREATE TABLE Usuario (
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
	contrasena VARCHAR(25) NOT NULL,
    intentos INT NOT NULL,
    cui BIGINT,
    id_empresa INT,
    FOREIGN KEY (cui) REFERENCES Cliente(cui),
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);

CREATE TABLE Cuenta (
	id_cuenta INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    tipo_cuenta VARCHAR(50) NOT NULL,
	tipo_moneda VARCHAR(50) NOT NULL,
    id_usuario INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Transaccion (
	id_transaccion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    monto_anterior FLOAT(15,2) NOT NULL,
    monto_despues FLOAT(15,2) NOT NULL,
	tipo_moneda VARCHAR(50) NOT NULL,
    tipo_transaccion VARCHAR(50) NOT NULL,
    id_cuenta INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE Planilla (
	id_planilla INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    monto_anterior FLOAT(15,2) NOT NULL,
    monto_despues FLOAT(15,2) NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE Prestamo (
	id_prestamo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    monto_anterior FLOAT(15,2) NOT NULL,
    monto_despues FLOAT(15,2) NOT NULL,
    tipo_prestamo VARCHAR(50) NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE Chequera (
	id_chequera INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    acabada VARCHAR(20) NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE Cheque (
	id_cheque INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    autorizado VARCHAR(20) NOT NULL,
    disponible VARCHAR(20) NOT NULL,
    id_chequera INT NOT NULL,
    nombre VARCHAR(100),
    FOREIGN KEY (id_chequera) REFERENCES Chequera(id_chequera)
);

SELECT * FROM Cliente;
INSERT INTO Cliente(cui, nit, nombre, apellido, fecha_nacimiento) VALUES('3007153150101', '544554545454', 'Jose Andres', 'Flores Barco', '21/12/2020');
SELECT * FROM Usuario;
INSERT INTO Usuario(nombre, contrasena, cui, intentos) VALUES('', '', '');
UPDATE Usuario SET intentos = '', contrasena = '' WHERE id_usuario = '';
SELECT * FROM Empresa;
INSERT INTO Empresa(nombre, nombre_comercial, nombre_representante) VALUES('', '', '');
SELECT * FROM Cuenta;
INSERT INTO Cuenta(monto, tipo_cuenta, tipo_moneda, id_usuario) VALUES('', '', '', '');
UPDATE Cuenta SET monto = '' WHERE id_cuenta = '';
SELECT * FROM Transaccion;
INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('', '', '', '', '', '');
SELECT * FROM Chequera;
INSERT INTO Transaccion(acabada, id_cuenta) VALUES('', '');
DELETE FROM Chequera WHERE id_chequera = '3';
SELECT * FROM Cheque;
INSERT INTO Cheque(monto, autorizado, disponible, id_chequera) VALUES('0', 'NO', 'SI', '');
UPDATE Cheque SET monto = '0', autorizado = 'NO' WHERE id_cheque = '1';
UPDATE Cheque SET disponible = 'NO' WHERE id_cheque = '1';

