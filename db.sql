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

CREATE TABLE Prestamo (
	id_prestamo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    tipo_prestamo VARCHAR(30) NOT NULL,
    id_usuario INT NOT NULL,
    aprobado VARCHAR(5) DEFAULT 'NO',
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE PrestamoAutomatico (
	id_prestamoAuto INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    id_prestamo INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_prestamo) REFERENCES Prestamo(id_prestamo),
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE PagoPrestamo (
	id_pagoPrestamo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    interes FLOAT(3,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_pago VARCHAR(30) NOT NULL,
    id_prestamo INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_prestamo) REFERENCES Prestamo(id_prestamo),
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
);

CREATE TABLE Tarjeta (
	id_tarjeta INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    marca VARCHAR(30) NOT NULL,
    puntos INT,
    cashback INT,
    limiteCredito FLOAT(15,2) NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE DetalleTarjeta (
	id_detalleTarjeta INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descripcion VARCHAR(200) NOT NULL,
    monto FLOAT(15,2) NOT NULL,
	tipo_moneda VARCHAR(50) NOT NULL,
    id_tarjeta INT NOT NULL,
    FOREIGN KEY (id_tarjeta) REFERENCES Tarjeta(id_tarjeta)
);

CREATE TABLE Planilla (
	id_planilla INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    nombre_empleado VARCHAR(100) NOT NULL,
	tipo_pago VARCHAR(30) NOT NULL,
    id_empresa INT NOT NULL,
	id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);

CREATE TABLE Proveedor (
	id_proveedor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    monto FLOAT(15,2) NOT NULL,
	tipo_pago VARCHAR(30) NOT NULL,
    id_empresa INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);

CREATE TABLE PagoPlanilla (
	id_pagoPlanilla INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    monto_anterior FLOAT(15,2) NOT NULL,
    monto_despues FLOAT(15,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_planilla INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_planilla) REFERENCES Planilla(id_planilla)
);

CREATE TABLE PagoProveedor (
	id_pagoProveedor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    monto_anterior FLOAT(15,2) NOT NULL,
    monto_despues FLOAT(15,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_proveedor INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor)
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
DELETE FROM Chequera WHERE id_chequera = '3';
SELECT * FROM Cheque;
INSERT INTO Cheque(monto, autorizado, disponible, id_chequera) VALUES('0', 'NO', 'SI', '');
UPDATE Cheque SET monto = '0', autorizado = 'NO' WHERE id_cheque = '1';
UPDATE Cheque SET disponible = 'NO' WHERE id_cheque = '1';

SELECT * FROM Prestamo;
INSERT INTO Prestamo(monto, descripcion, tipo_prestamo, id_usuario) VALUES('0', '', '', '0');
UPDATE Prestamo SET aprobado = 'SI' WHERE id_prestamo = '';

SELECT * FROM PrestamoAutomatico;
INSERT INTO PrestamoAutomatico(monto, id_prestamo, id_cuenta) VALUES('0', '', '');

SELECT * FROM PagoPrestamo;
INSERT INTO PagoPrestamo(monto, interes, tipo_pago, id_prestamo, id_cuenta) VALUES('', '0', 'PAGO AUTOMATICO', '', '');

SELECT * FROM Tarjeta;
INSERT INTO Tarjeta(monto, marca, puntos, cashback, limiteCredito, id_usuario) VALUES('0', '', '0', '0', '0', '');

SELECT * FROM PagoPrestamo;

SELECT * FROM Proveedor;
INSERT INTO Tarjeta(nombre, monto, tipo_pago, id_empresa, id_cuenta) VALUES('0', '', '0', '0', '0', '');