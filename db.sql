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
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)
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
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_planilla INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_planilla) REFERENCES Planilla(id_planilla)
);

CREATE TABLE PagoProveedor (
	id_pagoProveedor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    monto FLOAT(15,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_proveedor INT NOT NULL,
    id_cuenta INT NOT NULL,
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor)
);

SELECT * FROM Cliente;
INSERT INTO Cliente(cui, nit, nombre, apellido, fecha_nacimiento) 
VALUES('123456789', '123456789', 'Alfredo', 'De Leon', '05/06/1985'),
	  ('987654321', '987654321', 'Antonio', 'De La Cruz', '06/07/1986'),
      ('963258741', '963258741', 'Pamela', 'Fernandez', '07/08/1987');
      
SELECT * FROM Usuario;
INSERT INTO Usuario(nombre, contrasena, intentos, cui) 
VALUES('usuario1', '1234', '0', '123456789'),
      ('usuario2', '1234', '0', '987654321'),
      ('usuario3', '1234', '0', '963258741');
      
SELECT * FROM Empresa;
INSERT INTO Empresa(nombre, nombre_comercial, nombre_representante, tipo_empresa) 
VALUES('EMPRESA 1', 'EMPRESA 1 S.A', 'Sara', 'COMERCIAL'),
      ('EMPRESA 2', 'EMPRESA 2 S.A', 'Kevin', 'COMERCIAL'),
      ('EMPRESA 3', 'EMPRESA 3 S.A', 'Antonio', 'COMERCIAL');
      
SELECT * FROM Usuario;
INSERT INTO Usuario(nombre, contrasena, intentos, id_empresa) 
VALUES('empresa1', '1234', '0', '1'),
      ('empresa2', '1234', '0', '2'),
      ('empresa3', '1234', '0', '3');

SELECT * FROM Prestamo;
INSERT INTO Prestamo(monto, descripcion, tipo_prestamo, id_usuario) VALUES('0', '', '', '0');
UPDATE Prestamo SET aprobado = 'SI' WHERE id_prestamo = '';

SELECT * FROM PrestamoAutomatico;
INSERT INTO PrestamoAutomatico(monto, id_prestamo, id_cuenta) VALUES('0', '', '');

SELECT * FROM PagoPrestamo;
INSERT INTO PagoPrestamo(monto, interes, tipo_pago, id_prestamo, id_cuenta) VALUES('', '0', 'PAGO AUTOMATICO', '', '');

SELECT * FROM Tarjeta;
DELETE  FROM Tarjeta WHERE id_tarjeta != 10;
INSERT INTO Tarjeta(monto, marca, puntos, cashback, limiteCredito, id_usuario) VALUES('0', '', '0', '0', '0', '');

SELECT * FROM PagoPrestamo;

SELECT * FROM Proveedor;
INSERT INTO Tarjeta(nombre, monto, tipo_pago, id_empresa, id_cuenta) VALUES('0', '', '0', '0', '');

SELECT * FROM PagoProveedor;
INSERT INTO PagoProveedor(monto, monto_anterior, monto_despues, id_proveedor, id_cuenta) VALUES('', '0', '0', '', '');

SELECT * FROM Planilla;
DELETE FROM Planilla WHERE id_planilla = '';
INSERT INTO Planilla(nombre_empleado, monto, tipo_pago, id_empresa, id_cuenta) VALUES('', '', '', '', '');
UPDATE Planilla SET nombre_empleado = '', tipo_pago = '', id_cuenta = ''  WHERE id_planilla = '';

SELECT * FROM PagoPlanilla;
INSERT INTO PagoPlanilla(monto, monto_anterior, monto_despues, id_planilla, id_cuenta) VALUES('', '0', '0', '', '');

SELECT * FROM Cuenta;