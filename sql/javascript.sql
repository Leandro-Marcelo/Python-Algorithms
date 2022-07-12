SELECT * FROM FORMULARIO_POSTULACION;
DROP TABLE DIRECTOR_ENCARGADO;

CREATE TABLE FORMULARIO_POSTULACION (
    id_formulario_postulacion NUMBER(20) NOT NULL,
    director_encargado NUMBER(20) NOT NULL,
    escuela_deportiva NUMBER(20) NOT NULL,
    detalle_inversion NUMBER(20) NOT NULL,
    adjudicacion_recursos NUMBER(20) NOT NULL,
    contrato_trabajo NUMBER(20) NOT NULL,
    CONSTRAINT FORMULARIO_POSTULACION_pk PRIMARY KEY (id_formulario_postulacion)
);

CREATE SEQUENCE serie_FORMULARIO_POSTULACION
START WITH 1
INCREMENT BY 1;

CREATE TABLE COMUNA(
    id_comuna NUMBER(20) NOT NULL,
    nombre_comuna VARCHAR2(50) NOT NULL,
    CONSTRAINT COMUNA_pk PRIMARY KEY (id_comuna)
);

CREATE SEQUENCE serie_COMUNA
START WITH 1
INCREMENT BY 1;

CREATE TABLE REGION(
    id_region NUMBER(20) NOT NULL,
    nombre_region VARCHAR2(50) NOT NULL,
    CONSTRAINT REGION_pk PRIMARY KEY (id_region)
);
  
CREATE SEQUENCE serie_REGION
START WITH 1
INCREMENT BY 1;

CREATE TABLE DIRECTOR_ENCARGADO (
    id_director_encargado NUMBER(20) NOT NULL,
    rut_encargado NUMBER(9) NOT NULL,
    primer_nombre VARCHAR2(20) NOT NULL,
    segundo_nombre VARCHAR2(20) NOT NULL,
    primer_apellido VARCHAR2(20) NOT NULL,
    segundo_apellido VARCHAR2(20) NOT NULL,
    -- cambiado a direccion simplemente, quizas habría que desglosarlo en coso pero bueno
    direccion_encargado VARCHAR2(100),
    -- comuna y region NUMBER meterla como alter table
    comuna NUMBER(20) NOT NULL,
    region NUMBER(20) NOT NULL,
    -- quizas otra tabla con todos los telefonos de este wn
    telefonos NUMBER (9) NOT NULL,
    correo_email VARCHAR2(100) NOT NULL,
    profesion_ocupacion VARCHAR2(20) NOT NULL,
    nacionalidad VARCHAR2(20) NOT NULL,
    -- cuidado con la fecha automatica
    fecha DATE NOT NULL,
    estado_civil VARCHAR2(20),
    CONSTRAINT DIRECTOR_ENCARGADO_pk PRIMARY KEY (id_director_encargado)
);

CREATE SEQUENCE serie_DIRECTOR_ENCARGADO
START WITH 1
INCREMENT BY 1;


CREATE TABLE ESCUELA_DEPORTIVA (
    id_escuela_deportiva NUMBER (20) NOT NULL,
    nombre_escuela VARCHAR2 (20) NOT NULL,
    ubicacion_recinto_deportivo VARCHAR2 (100) NOT NULL,
    -- comuna y region como alter
    comuna NUMBER(20) NOT NULL,
    region NUMBER(20) NOT NULL,
    nombre_club_deportivo VARCHAR2 (25),
    -- tipo de escuela se podría sacar
    tipo_escuela VARCHAR2 (20) NOT NULL,
    sitio_web VARCHAR2 (100),
    numero_inscripcion_comunal NUMBER(20),
    fecha_resolucion DATE NOT NULL,
    CONSTRAINT ESCUELA_DEPORTIVA_pk PRIMARY KEY (id_escuela_deportiva)
);

CREATE SEQUENCE serie_ESCUELA_DEPORTIVA
START WITH 1
INCREMENT BY 1;


CREATE TABLE DETALLE_INVERSION (
    id_detalle_inversion NUMBER(20) NOT NULL,
    monto_solicitado_UF NUMBER(3) NOT NULL,
    nombre_proyecto_inversion VARCHAR2 (20),
    -- crear otra tabla afuera
    tipo_inversion NUMBER(20),
    CONSTRAINT DETALLE_INVERSION_pk PRIMARY KEY (id_detalle_inversion)
);

CREATE SEQUENCE serie_DETALLE_INVERSION
START WITH 1
INCREMENT BY 1;

CREATE TABLE ADJUDICACION_RECURSOS (
    id_adjudicacion_recursos NUMBER(20) NOT NULL,
    puntaje NUMBER(20),
    monto_asignado NUMBER(20),
    cumple_requisitos VARCHAR2(20),
    CONSTRAINT ADJUDICACION_RECURSOS_pk PRIMARY KEY (id_adjudicacion_recursos)
);

CREATE SEQUENCE serie_ADJUDICACION_RECURSOS
START WITH 1
INCREMENT BY 1;


CREATE TABLE CONTRATO_TRABAJO (
    id_contrato_trabajo NUMBER(20) NOT NULL,
    nombre_profesor VARCHAR2(20) NOT NULL,
    run_profesor NUMBER(9) NOT NULL,
    especialidad_titulo VARCHAR2(20),
    universidad_instituto VARCHAR2(20),
    direccion_particular VARCHAR2 (100) NOT NULL,
    tipo_contrato VARCHAR2(20),
    -- no se porque afk e isapre varchar2 pero bueno
    afp VARCHAR2(20),
    isapre VARCHAR2(20),
    sueldo_base NUMBER(20),
    valor_hora NUMBER(20),
    horas_mensuales NUMBER(20),
    CONSTRAINT CONTRATO_TRABAJO_pk PRIMARY KEY (id_contrato_trabajo)
);

CREATE SEQUENCE serie_CONTRATO_TRABAJO
START WITH 1
INCREMENT BY 1;

-- FK


ALTER TABLE DIRECTOR_ENCARGADO
     ADD CONSTRAINT DE_id_comuna_fkey 
     FOREIGN KEY (comuna) 
     REFERENCES COMUNA (id_comuna); 

ALTER TABLE DIRECTOR_ENCARGADO 
     ADD CONSTRAINT DE_id_region_fkey 
     FOREIGN KEY (region)
     REFERENCES REGION (id_region); 

ALTER TABLE ESCUELA_DEPORTIVA 
     ADD CONSTRAINT ED_id_comuna_fkey 
     FOREIGN KEY (comuna) 
     REFERENCES COMUNA (id_comuna); 

ALTER TABLE ESCUELA_DEPORTIVA 
     ADD CONSTRAINT ED_id_region_fkey 
     FOREIGN KEY (region)
     REFERENCES REGION (id_region);

ALTER TABLE FORMULARIO_POSTULACION 
     ADD CONSTRAINT FP_id_director_encargado_fkey 
     FOREIGN KEY (director_encargado)
     REFERENCES DIRECTOR_ENCARGADO (id_director_encargado);

ALTER TABLE ESCUELA_DEPORTIVA 
     ADD CONSTRAINT FP_id_escuela_deportiva_fkey 
     FOREIGN KEY (id_escuela_deportiva)
     REFERENCES ESCUELA_DEPORTIVA (id_escuela_deportiva);

ALTER TABLE DETALLE_INVERSION 
     ADD CONSTRAINT FP_id_detalle_inversion_fkey 
     FOREIGN KEY (id_detalle_inversion)
     REFERENCES DETALLE_INVERSION (id_detalle_inversion);

ALTER TABLE ADJUDICACION_RECURSOS 
     ADD CONSTRAINT FP_adjudicacion_recursos_fkey 
     FOREIGN KEY (id_adjudicacion_recursos)
     REFERENCES ADJUDICACION_RECURSOS (id_adjudicacion_recursos);

ALTER TABLE CONTRATO_TRABAJO 
     ADD CONSTRAINT FP_contrato_trabajo_fkey 
     FOREIGN KEY (id_contrato_trabajo)
     REFERENCES CONTRATO_TRABAJO (id_contrato_trabajo);












