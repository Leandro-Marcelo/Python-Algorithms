
-- -------------------------------------------------------------------------------------------------TABLAS ------------------------------------------------------------------------------------------------------

-- TABLA FORMULARIO_POSTULACION
CREATE TABLE FORMULARIO_POSTULACION (
    id_formulario_postulacion NUMBER (6) NOT NULL,
    CONSTRAINT pk_FORMULARIO_POSTULACION PRIMARY KEY ( id_formulario_postulacion)
);

CREATE SEQUENCE serie_FORMULARIO_POSTULACION
START WITH 1
INCREMENT BY 1;

-- TABLA DIRECTOR_ENCARGADO
CREATE TABLE DIRECTOR_ENCARGADO (
    id_director_encargado NUMBER (4) NOT NULL,
    rut_director NUMBER (8) NOT NULL,
    nombres VARCHAR2 (30) NOT NULL,
    apellidos VARCHAR2 (30) NOT NULL,
    direccion_encargado VARCHAR2 (50),
    comuna VARCHAR2 (15) NOT NULL,
    region VARCHAR2 (25) NOT NULL,
    telefonos NUMBER (9) NOT NULL,
    correo_email VARCHAR2 (50) NOT NULL,
    profesion_ocupacion VARCHAR2 (25) NOT NULL,
    nacionalidad VARCHAR2 (15) NOT NULL,
    fecha DATE NOT NULL,
    estado_civil VARCHAR2 (10),
    CONSTRAINT pk_DIRECTOR_ENCARGADO PRIMARY KEY ( id_director_encargado)
);

CREATE SEQUENCE serie_DIRECTOR_ENCARGADO
START WITH 1
INCREMENT BY 1;

-- TABLA ESCUELA_DEPORTIVA
CREATE TABLE ESCUELA_DEPORTIVA (
    id_escuela_deportiva NUMBER (4) NOT NULL,
    nombre_escuela VARCHAR2 (25) NOT NULL,
    ubicacion_recinto_deportivo VARCHAR2 (50) NOT NULL,
    comuna VARCHAR2 (15) NOT NULL,
    region VARCHAR2 (25) NOT NULL,
    nombre_club_deportivo VARCHAR2 (25),
    tipo_escuela VARCHAR2 (15) NOT NULL,
    sitio_web VARCHAR2 (50),
    numero_inscripcion_comunal NUMBER (10),
    fecha_resolucion DATE NOT NULL,
    CONSTRAINT pk_ESCUELA_DEPORTIVA PRIMARY KEY ( id_escuela_deportiva)
);

CREATE SEQUENCE serie_ESCUELA_DEPORTIVA
START WITH 1
INCREMENT BY 1;

-- TABLA DETALLE_INVERSION
CREATE TABLE DETALLE_INVERSION (
    id_detalle_inversion NUMBER (6) NOT NULL,
    monto_solicitado_UF NUMBER (3) NOT NULL,
    nombre_proyecto_inversion VARCHAR2 (15),
    tipo_inversion VARCHAR2 (15),
    CONSTRAINT pk_DETALLE_INVERSION PRIMARY KEY (id_detalle_inversion)
);

CREATE SEQUENCE serie_DETALLE_INVERSION
START WITH 1
INCREMENT BY 1;

-- TABLA ADJUDICACION_RECURSOS
CREATE TABLE ADJUDICACION_RECURSOS (
    id_adjudicacion_recursos NUMBER (2) NOT NULL,
    puntaje NUMBER (5),
    monto_asignado NUMBER (8),
    cumple_requisitos VARCHAR2 (2),
    CONSTRAINT pk_ADJUDICACION_RECURSOS PRIMARY KEY ( id_adjudicacion_recursos)
);

CREATE SEQUENCE serie_ADJUDICACION_RECURSOS
START WITH 1
INCREMENT BY 1;

-- TABLA CONTRATO_TRABAJO
CREATE TABLE CONTRATO_TRABAJO (
    id_contrato_trabajo NUMBER (8) NOT NULL,
    nombre_profesor VARCHAR2 (15) NOT NULL,
    run_profesor NUMBER (8) NOT NULL,
    especialidad_titulo VARCHAR2 (15),
    universidad_instituto VARCHAR2 (25),
    direccion_particular VARCHAR2 (50) NOT NULL,
    tipo_contrato VARCHAR2 (1),
    afp VARCHAR2 (15),
    isapre VARCHAR2 (15),
    sueldo_base NUMBER (8),
    valor_hora NUMBER (5),
    horas_mensuales NUMBER (3),
    CONSTRAINT pk_CONTRATO_TRABAJO PRIMARY KEY ( id_contrato_trabajo)
);

CREATE SEQUENCE serie_CONTRATO_TRABAJO
START WITH 1
INCREMENT BY 1;

-- ------------------------------------------------------------------------------VALIDACIONES y MODIFICACIONES ------------------------------------------------------------------------------------
-- Agregar check
ALTER TABLE DETALLE_INVERSION ADD CHECK (monto_solicitado_UF <= 150);

-- Este alter table es para generar una fecha por default. IMPORTANTE: para modificar el tipo de dato la tabla debe estar vacía.
ALTER TABLE BOLETA 
MODIFY (fecha_boleta DATE DEFAULT sysdate);

-- Agregar columna
ALTER TABLE CONTRATO_TRABAJO
ADD firma VARCHAR2 (7) null;

-- Agregar columna NOT NULL sin vaciar tabla
ALTER TABLE CONTRATO_TRABAJO
ADD firma VARCHAR2 (7) DEFAULT 0 NOT NULL;

-- Eliminar columna
ALTER TABLE CONTRATO_TRABAJO
DROP COLUMN firma;

-- Eliminar tabla completa
DROP TABLE nombre_tabla;

-- Mostrar Tabla
SELECT * FROM CONTRATO_TRABAJO;

-- Borrar fila
DELETE FROM CONTRATO_TRABAJO WHERE  id_contrato_trabajo = 365324;

-- Borrar todas las filas
DELETE FROM CONTRATO_TRABAJO;

-- Borrar filas sin recuperacion
TRUNCATE TABLE CONTRATO_TRABAJO;

-- Insertar una fila
INSERT INTO CONTRATO_TRABAJO VALUES (365324,'jirafales', 17554634,'profe','uss','los berrinches 2332', 'P','modelo','fonasa',300000,15000,70);

-- Actualizar un registro
UPDATE CONTRATO_TRABAJO SET firma = 'manu.f' WHERE firma = 0;

-- Recuperar filas borradas
ROLLBACK;


-- ---------------------------------------------------------------- RESTRICCIONES DE FOREIGN KEYS ------------------------------------------------------------------------------------

-- RESTRICCION BOLETA
ALTER TABLE BOLETA -- tabla donde se hará la restriccion
     ADD CONSTRAINT fk_id_cliente -- nombre de la restriccion
     FOREIGN KEY (id_cliente) -- clave foranea dentro de la tabla
     REFERENCES CLIENTE (id_cliente); -- tabla de donde viene la pk y la pk que se transformará en fk
         



-- -------------------------------------------------------------------------------------INSERT REGISTROS-----------------------------------------------------------------------------------------------------------------------


-- INSERT sin valor automático
INSERT INTO CATEGORIZACION VALUES ('A','lista A', 17.5);

-- INSERT con valor automático
INSERT INTO FABRICA VALUES (serie_FABRICA.nextval,'Costa');

-- INSERT con fechas y datos null
INSERT INTO EMPLEADO VALUES (serie_EMPLEADO.nextval,'11111112-6','Mary','Culvert','Rivera',to_date('22/05/63','dd/mm/yy'),to_date('16/04/85','dd/mm/yy'),350000,24,'A','C');
INSERT INTO EMPLEADO VALUES (serie_EMPLEADO.nextval,'12222222-3','Jerome','Woods',NULL,to_date('07/08/78','dd/mm/yy'),to_date('02/07/00','dd/mm/yy'),345000,17,'B','B');

-- INSERT a tabla para generar fecha por default (fecha del ingreso al sistema)  gracias al default que se hizo en validaciones y modificaciones.
-- Para que funcione es necesario ingresar todo menos la misma información de la fecha.
INSERT INTO BOLETA (id_boleta, id_cliente, id_empleado) VALUES (serie_BOLETA.nextval,5,7);


-- ------------------------------------------------------------------------------------------------ OTROS COMANDOS -----------------------------------------------------------------------------------------------------------

SELECT * FROM BOLETA;
DELETE FROM BOLETA;



