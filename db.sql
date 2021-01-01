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
VALUES('1111111111', '1111111111', 'DIEGO FERNANDO', 'CORTEZ LOPEZ', '05/06/1985'),
      ('2222222222', '2222222222', 'KARINA NOHEMI', 'RAMIREZ ORELLANA', '05/06/1985'),
      ('3333333333', '3333333333', 'ANGEL GEOVANY', 'ARAGON PEREZ', '05/06/1985'),
      ('4444444444', '4444444444', 'CARLOS ROBERTO', 'QUIXTAN PEREZ', '05/06/1985'),
      ('5555555555', '5555555555', 'ERICK IVAN', 'MAYORGA RODRIGUEZ', '05/06/1985'),
      ('6666666666', '6666666666', 'BYRON ESTUARDO', 'CAAL CATUN', '05/06/1985'),
	  ('7777777777', '7777777777', 'RONALD RODRIGO', 'MARIN SALAS', '05/06/1985'),
      ('8888888888', '8888888888', 'OSCAR DANIEL', 'OLIVA', '05/06/1985'),
      ('9999999999', '9999999999', 'EDUARDO ABRAHAM', 'BARILLAS', '05/06/1985'),
      ('1010101010', '1010101010', 'CARLOS ESTUARDO', 'MONTERROSO SANTOS', '05/06/1985');
      
SELECT * FROM Usuario;
INSERT INTO Usuario(nombre, contrasena, intentos, cui) 
VALUES('usuario1', '1234', '0', '1111111111'),
      ('usuario2', '1234', '0', '2222222222'),
      ('usuario3', '1234', '0', '3333333333'),
      ('usuario4', '1234', '0', '4444444444'),
      ('usuario5', '1234', '0', '5555555555'),
      ('usuario6', '1234', '0', '6666666666'),
      ('usuario7', '1234', '0', '7777777777'),
      ('usuario8', '1234', '0', '8888888888'),
      ('usuario9', '1234', '0', '9999999999'),
      ('usuario10', '1234', '0', '1010101010');
      
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
      
SELECT * FROM Cuenta;
INSERT INTO Cuenta(id_cuenta, monto, tipo_cuenta, tipo_moneda, id_usuario, estado)
VALUES('541234', '500', 'MONETARIA', 'QUETZAL', '1', 'ACTIVA'),
	  ('263769', '500', 'MONETARIA', 'QUETZAL', '2', 'ACTIVA'),
      ('481366', '500', 'MONETARIA', 'QUETZAL', '3', 'ACTIVA'),
      ('152352', '500', 'MONETARIA', 'QUETZAL', '4', 'ACTIVA'),
      ('358054', '500', 'MONETARIA', 'DOLLAR', '5', 'ACTIVA'),
      ('503944', '500', 'MONETARIA', 'DOLLAR', '6', 'ACTIVA'),
      ('316167', '500', 'MONETARIA', 'DOLLAR', '7', 'ACTIVA'),
      ('374296', '500', 'MONETARIA', 'DOLLAR', '8', 'ACTIVA'),
      ('556658', '500', 'MONETARIA', 'DOLLAR', '9', 'ACTIVA'),
      ('462978', '500', 'MONETARIA', 'DOLLAR', '10', 'ACTIVA');
      
INSERT INTO Cuenta(monto, tipo_cuenta, tipo_moneda, id_usuario, estado)
VALUES('50000', 'MONETARIA', 'QUETZAL', '11', 'ACTIVA'),
	  ('70000', 'MONETARIA', 'QUETZAL', '12', 'ACTIVA'),
      ('50000', 'MONETARIA', 'QUETZAL', '13', 'ACTIVA'),
      ('80000', 'MONETARIA', 'QUETZAL', '11', 'ACTIVA'),
      ('50000', 'MONETARIA', 'DOLLAR', '12', 'ACTIVA'),
      ('90000', 'MONETARIA', 'DOLLAR', '13', 'ACTIVA'),
      ('10000', 'MONETARIA', 'DOLLAR', '11', 'ACTIVA'),
      ('50000', 'MONETARIA', 'DOLLAR', '12', 'ACTIVA'),
      ('60000', 'MONETARIA', 'DOLLAR', '13', 'ACTIVA'),
      ('40000', 'MONETARIA', 'DOLLAR', '11', 'ACTIVA');