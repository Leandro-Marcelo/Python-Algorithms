-- -------------------------------------------------------PREPRUEBA 3-------------------------------------------------

-- Borrar
DROP TABLE cliente;
DROP TABLE comuna;

-- ---------------------------------------------------------- TABLAS ----------------------------------------------------

-- Tabla DETALLE FACTURA
CREATE TABLE DETALLE_FACTURA (
  id_detalle_factura NUMBER(9) NOT NULL,  
  id_factura NUMBER(9) NOT NULL,
  id_articulo NUMBER(9) NOT NULL,
  cantidad_articulo NUMBER(3) NOT NULL,
  CONSTRAINT pk_DETALLE_FACTURA PRIMARY KEY (id_detalle_factura)
);

CREATE SEQUENCE serie_detalle_factura
START WITH 1
INCREMENT BY 1;

INSERT INTO DETALLE_FACTURA (id_detalle_factura, id_factura,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);


-- Tabla FACTURA
CREATE TABLE FACTURA (
  id_factura NUMBER(9) NOT NULL,  
  id_vendedor NUMBER(3) NOT NULL,
  fecha_factura DATE NOT NULL,
  CONSTRAINT pk_FACTURA PRIMARY KEY (id_factura)
);

CREATE SEQUENCE serie_factura
START WITH 1
INCREMENT BY 1;

INSERT INTO FACTURA (id_factura, id_vendedor,fecha_factura) VALUES (factura.nextval, ,'dd - mon - yyyy');

-- Tabla VENDEDOR
CREATE TABLE VENDEDOR (
  id_vendedor NUMBER(6) NOT NULL,  
  rut_vendedor NUMBER(6) NOT NULL,  
  primer_nombre VARCHAR2 (15) NOT NULL,  
  segundo_nombre VARCHAR2 (15) NOT NULL,  
  apellido_paterno VARCHAR2 (15) NOT NULL,  
  apellido_materno VARCHAR2 (15) NOT NULL,  
  
  id_categoria_vendedor NUMBER (4) NOT NULL, 
  id_zona_de_venta NUMBER(3) NOT NULL,  
  id_contrato NUMBER(6) NOT NULL,
  CONSTRAINT pk_VENDEDOR PRIMARY KEY (id_vendedor)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);


-- Tabla CONTRATO
CREATE TABLE CONTRATO (
    id_contrato NUMBER(6) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    fecha_contrato DATE NOT NULL,
    sueldo NUMBER(6) NOT NULL,  
    id_vendedor NUMBER(6) NOT NULL, 
    CONSTRAINT pk_CONTRATO PRIMARY KEY (id_contrato)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);

-- Tabla CATEGORIA_VENDEDOR
CREATE TABLE CATEGORIA_VENDEDOR (
  id_categoria_vendedor NUMBER (4) NOT NULL,  
  nombre_categoria_vendedor VARCHAR2 (15) NOT NULL,  
  porcentaje_comision_categoria NUMBER (2) NOT NULL,  
  CONSTRAINT pk_CATEGORIA_VENDEDOR PRIMARY KEY (id_categoria_vendedor)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);


-- Tabla ZONA_DE_VENTA
CREATE TABLE ZONA_DE_VENTA (
  id_zona_de_venta NUMBER(3) NOT NULL,  
  nombre_zona_de_venta VARCHAR2 (15) NOT NULL,  
  CONSTRAINT pk_ZONA_DE_VENTA PRIMARY KEY (id_zona_de_venta)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);


-- Tabla ARTICULO
CREATE TABLE ARTICULO (
  id_articulo NUMBER(9) NOT NULL,  
  nombre_articulo VARCHAR2 (15) NOT NULL,
  precio_articulo NUMBER(6) NOT NULL,
  stock_actual NUMBER (3) NOT NULL,
  stock_minimo NUMBER (3) NOT NULL,
  
  id_marca NUMBER (3) NOT NULL,
  CONSTRAINT pk_ARTICULO PRIMARY KEY (id_articulo)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);


-- Tabla MARCA
CREATE TABLE MARCA (
    id_marca NUMBER (3) NOT NULL, 
    nombre_marca VARCHAR2 (15) NOT NULL,
    CONSTRAINT pk_MARCA PRIMARY KEY (id_marca)
);

CREATE SEQUENCE serie_vendedor
START WITH 1
INCREMENT BY 1;

INSERT INTO VENDEDOR (id_vendedor, rut_vendedor,id_articulo,cantidad_articulo) VALUES (serie_detalle_factura.nextval,);

-- --------------------------------------------------MODIFICACIONES A LLAVES PRIMARIAS--------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------------------------------------------
ALTER TABLE FACTURA
     PRIMARY KEY (id_factura)

-- ---------------------------------------------------------MODIFICACIONES A LLAVES FORÁNEAS----------------------------------------------
-- TABLA FACTURA
ALTER TABLE FACTURA
     ADD CONSTRAINT fk_id_vendedor
     FOREIGN KEY (id_vendedor)
     REFERENCES VENDEDOR (id_vendedor);

-- TABLA VENDEDOR
ALTER TABLE VENDEDOR
     ADD CONSTRAINT fk_id_categoria_vendedor
     FOREIGN KEY (id_categoria_vendedor)
     REFERENCES CATEGORIA_VENDEDOR (id_categoria_vendedor);
     
ALTER TABLE VENDEDOR
     ADD CONSTRAINT fk_id_zona_de_venta
     FOREIGN KEY (id_zona_de_venta)
     REFERENCES ZONA_DE_VENTA (id_zona_de_venta);
     
ALTER TABLE VENDEDOR
     ADD CONSTRAINT fk_id_contrato
     FOREIGN KEY (id_contrato)
     REFERENCES CONTRATO (id_contrato);

-- TABLA CONTRATO
ALTER TABLE CONTRATO
     ADD CONSTRAINT fk_id_vendedor_1
     FOREIGN KEY (id_vendedor)
     REFERENCES VENDEDOR (id_vendedor);

-- TABLA DETALLE_FACTURA
ALTER TABLE DETALLE_FACTURA
     ADD CONSTRAINT fk_id_factura
     FOREIGN KEY (id_factura)
     REFERENCES FACTURA (id_factura);

ALTER TABLE DETALLE_FACTURA
     ADD CONSTRAINT fk_id_articulo
     FOREIGN KEY (id_articulo)
     REFERENCES ARTICULO (id_articulo);

-- TABLA ARTICULO
ALTER TABLE ARTICULO
     ADD CONSTRAINT fk_id_marca
     FOREIGN KEY (id_marca)
     REFERENCES MARCA (id_marca);


-- ---------------------------------------------------------INSERT----------------------------------------------

INSERT INTO comuna VALUES (100, 'Providencia');

-- ---------------------------------------------------------AUTO INCREMENTAL----------------------------------------------
DROP TABLE Fabricante;

describe FACTURA;
CREATE TABLE Fabricante(
    cod_fabricante number primary key,
    nombre VARCHAR2(25) NOT NULL,
    pais VARCHAR2(25) DEFAULT 'España'
);

CREATE SEQUENCE fabricante_serie
START WITH 1
INCREMENT BY 1;

SELECT * FROM fabricante; 

INSERT INTO Fabricante (cod_fabricante, nombre) VALUES (fabricante_serie.nextval, 'Rama');

-- ---------------------------------------------------------Ejemplo PK y FK-------------------------------------------------
CREATE TABLE supplier(
    supplier_id numeric(10) not null,
    supplier_name varchar2(50) not null,
    contact_name varchar2(50),
    
    CONSTRAINT supplier_pk PRIMARY KEY (supplier_id)
);

CREATE TABLE products(
    product_id numeric(10) not null,
    supplier_id numeric(10) not null,
    
    CONSTRAINT fk_supplier
    FOREIGN KEY (supplier_id)
    REFERENCES supplier(supplier_id)
);

/* ddddddddddddddddddddddddddddddddddddd */

-- --------------------------------------------------MODIFICACIONES --------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------------------------------------------
ALTER TABLE VENDEDOR DROP (rut_vendedor)

ALTER TABLE VENDEDOR ADD (rut_vendedor NUMBER(6) NOT NULL UNIQUE)  

/* *********************************** */

CREATE TABLE equipo 
(
    id_equipo       VARCHAR2(1) NOT NULL,
    nom_equipo      VARCHAR2(10) NOT NULL,
    porc            NUMBER(5,2) NOT NULL
);

ALTER TABLE equipo ADD CONSTRAINT equipo_pk PRIMARY KEY ( id_equipo );

CREATE TABLE categorizacion 
(
    id_categorizacion   CHAR(1) NOT NULL,
    nom_categorizacion  VARCHAR2(10) NOT NULL,
    porcentaje          NUMBER NOT NULL
);

ALTER TABLE categorizacion ADD CONSTRAINT categorizacion_pk PRIMARY KEY ( id_categorizacion );

CREATE TABLE empleado 
(
    id_empleado     NUMBER(6) NOT NULL,
    rut_empleado    VARCHAR2(10) NOT NULL,
    nombres         VARCHAR2(25) NOT NULL,
    paterno         VARCHAR2(15) NOT NULL,
    materno         VARCHAR2(15) NOT NULL,
    fecnac          DATE NOT NULL,
    feccontrato     DATE NOT NULL,
    sueldo          NUMBER NOT NULL,
    comision        NUMBER NOT NULL,
    id_equipo       VARCHAR2(1) NOT NULL,
    id_categorizacion   CHAR(1) NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( id_empleado );
ALTER TABLE empleado ADD CONSTRAINT empleado_equipo_fk FOREIGN KEY ( id_equipo ) REFERENCES equipo ( id_equipo );
ALTER TABLE empleado ADD CONSTRAINT empleado_categorizacion_fk FOREIGN KEY ( id_categorizacion ) REFERENCES categorizacion ( id_categorizacion );

CREATE TABLE fabrica 
(
    id_fabrica     NUMBER(4) NOT NULL,
    nom_fabrica    VARCHAR2(60) NOT NULL
);

ALTER TABLE fabrica ADD CONSTRAINT fabrica_pk PRIMARY KEY ( id_fabrica );

CREATE TABLE producto 
(
    id_poducto      NUMBER NOT NULL,
    nom_producto    VARCHAR2(25) NOT NULL,
    precio          NUMBER NOT NULL,
    stock_actual    NUMBER(4) NOT NULL,
    stock_minimo    NUMBER(4) NOT NULL,
    id_fabrica      NUMBER(4) NOT NULL
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );
ALTER TABLE producto ADD CONSTRAINT producto_fabrica_fk FOREIGN KEY ( id_fabrica ) REFERENCES fabrica ( id_fabrica );

CREATE TABLE detalleBoleta
(
  id_boleta     NUMBER NOT NULL,
  id_producto   NUMBER NOT NULL,
  cantidad      NUMBER NOT NULL
);

ALTER TABLE detalleBoleta ADD CONSTRAINT detalleBoleta_pk PRIMARY KEY ( id_boleta, id_producto );

ALTER TABLE boleta ADD CONSTRAINT boleta_empleado FOREIGN KEY ( id_empleado ) REFERENCES empleado ( id_empleado );

CREATE TABLE comuna 
(
    id_comuna      NUMBER NOT NULL,
    nom_comuna     VARCHAR2(60) NOT NULL
);

ALTER TABLE comuna ADD CONSTRAINT comuna_pk PRIMARY KEY ( id_comuna );

ALTER TABLE cliente ADD CONSTRAINT cliente_comuna_fk FOREIGN KEY ( id_comuna ) REFERENCES comuna ( id_comuna );

CREATE SEQUENCE idfab
START WITH 5
INCREMENT BY 5;

CREATE SEQUENCE idcomuna
START WITH 100
INCREMENT BY 2;

CREATE SEQUENCE idboleta
START WITH 1010
INCREMENT BY 10;

CREATE SEQUENCE idcliente
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE idempleado
START WITH 1
INCREMENT BY 1;

INSERT INTO fabrica (id_fabrica,nom_fabrica) VALUES (IDFAB.nextval,'COSTA');
INSERT INTO fabrica (id_fabrica,nom_fabrica) VALUES (IDFAB.nextval,'AMBROSOLI');
INSERT INTO fabrica (id_fabrica,nom_fabrica) VALUES (IDFAB.nextval,'NESTLE');
INSERT INTO fabrica (id_fabrica,nom_fabrica) VALUES (IDFAB.nextval,'DOS EN UNO');
INSERT INTO fabrica (id_fabrica,nom_fabrica) VALUES (IDFAB.nextval,'ARCOR');

INSERT INTO boleta (id_boleta,id_cliente,id_empleado,fecha_boleta) VALUES (IDBOLETA.nextval,'1','2','17/01/22');
INSERT INTO boleta (id_boleta,id_cliente,id_empleado,fecha_boleta) VALUES (IDBOLETA.nextval,'2','4','17/01/22');
INSERT INTO boleta (id_boleta,id_cliente,id_empleado,fecha_boleta) VALUES (IDBOLETA.nextval,'4','3','17/01/22');
INSERT INTO boleta (id_boleta,id_cliente,id_empleado,fecha_boleta) VALUES (IDBOLETA.nextval,'3','5','17/01/22');
INSERT INTO boleta (id_boleta,id_cliente,id_empleado,fecha_boleta) VALUES (IDBOLETA.nextval,'2','2','17/01/22');

INSERT INTO categorizacion (id_categorizacion,nom_categorizacion,porcentaje) VALUES ('A','LISTA A',17.5);
INSERT INTO categorizacion (id_categorizacion,nom_categorizacion,porcentaje) VALUES ('B','LISTA B',12.6);
INSERT INTO categorizacion (id_categorizacion,nom_categorizacion,porcentaje) VALUES ('C','LISTA C',9.4);
INSERT INTO categorizacion (id_categorizacion,nom_categorizacion,porcentaje) VALUES ('D','LISTA D',7.2);
INSERT INTO categorizacion (id_categorizacion,nom_categorizacion,porcentaje) VALUES ('E','LISTA E',5.4);

INSERT INTO equipo (id_equipo,nom_equipo,porc) VALUES ('A','Equipo A',8.56);
INSERT INTO equipo (id_equipo,nom_equipo,porc) VALUES ('B','Equipo B',10.48);
INSERT INTO equipo (id_equipo,nom_equipo,porc) VALUES ('C','Equipo C',11.27);
INSERT INTO equipo (id_equipo,nom_equipo,porc) VALUES ('D','Equipo D',7.24);

INSERT INTO cliente (id_cliente,nombre_cliente,direccion,telefono,id_comuna) VALUES (IDCLIENTE.nextval,'ALCARAZ NOVOA MONSERRAT','RUBEN  BARRALES 1630','564522114','106');
INSERT INTO cliente (id_cliente,nombre_cliente,direccion,telefono,id_comuna) VALUES (IDCLIENTE.nextval,'JIMENEZ LORCA ELENA','AV. BUSTAMANTES 529 DPTO. K','566665443','100');
INSERT INTO cliente (id_cliente,nombre_cliente,direccion,telefono,id_comuna) VALUES (IDCLIENTE.nextval,'TORRES ROCA MARIA','DONATELLO 7421','565626134','102');
INSERT INTO cliente (id_cliente,nombre_cliente,direccion,telefono,id_comuna) VALUES (IDCLIENTE.nextval,'LOPEZ ROJAS THOMAS','LORCA 2007','562989233','110');

INSERT INTO empleado (id_empleado,rut_empleado,nombres,paterno,materno,fecnac,feccontrato,sueldo,comision,id_equipo,id_caterogirazcion) VALUES (IDEMPLEADO.nextval,'11111112-6','MARY','CULVERT','RIVERA','22/05/63','16/04/85',350000,0.25,'A','C');
INSERT INTO empleado (id_empleado,rut_empleado,nombres,paterno,materno,fecnac,feccontrato,sueldo,comision,id_equipo,id_caterogirazcion) VALUES (IDEMPLEADO.nextval,'12222222-3','JEROME','WOODS','','07/08/78','02/07/00',345000,0.17,'B','B');
INSERT INTO empleado (id_empleado,rut_empleado,nombres,paterno,materno,fecnac,feccontrato,sueldo,comision,id_equipo,id_caterogirazcion) VALUES (IDEMPLEADO.nextval,'13333333-K','NORA','BROMESLER','OGAZ','09/10/79','03/09/01',367400,0.25,'A','A');
INSERT INTO empleado (id_empleado,rut_empleado,nombres,paterno,materno,fecnac,feccontrato,sueldo,comision,id_equipo,id_caterogirazcion) VALUES (IDEMPLEADO.nextval,'14444444-5','FREDERICK','MALLON','PAREDES','08/12/77','03/11/99',373620,0.12,'C','C');
INSERT INTO empleado (id_empleado,rut_empleado,nombres,paterno,materno,fecnac,feccontrato,sueldo,comision,id_equipo,id_caterogirazcion) VALUES (IDEMPLEADO.nextval,'15555555-6','PAZ','GUERRA','','08/12/88','03/11/15',373620,0.21,'','C');

INSERT INTO producto (id_producto,nom_producto,precio,stock_actual,stock_minimo,id_fabrica) VALUES (1,'BARRITAS',250,150,110,5);
INSERT INTO producto (id_producto,nom_producto,precio,stock_actual,stock_minimo,id_fabrica) VALUES (2,'LECHEROS',325,50,30,5);
INSERT INTO producto (id_producto,nom_producto,precio,stock_actual,stock_minimo,id_fabrica) VALUES (3,'ROSENDOS',100,200,50,10);
INSERT INTO producto (id_producto,nom_producto,precio,stock_actual,stock_minimo,id_fabrica) VALUES (4,'ZIG ZAGS',375,50,20,15);
INSERT INTO producto (id_producto,nom_producto,precio,stock_actual,stock_minimo,id_fabrica) VALUES (5,'PECADOS',400,80,20,20);

INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'PROVIDENCIA');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'SANTIAGO');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'ÑUÑOA');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'LA FLORIDA');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'MAIPU');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'LO BARNECHEA');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'MACUL');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'SAN MIGUEL');
INSERT INTO comuna (id_comuna,nom_comuna) VALUES (IDCOMUNA.nextval,'RECOLETA');

INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1010,1,10);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1010,5,33);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1020,3,88);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1020,4,33);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1020,1,90);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1030,4,200);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1030,2,500);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1040,5,500);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1040,2,250);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1040,3,300);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1050,4,196);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1050,5,128);
INSERT INTO detalleboleta (id_boleta,id_producto,cantidad) VALUES (1050,2,181);