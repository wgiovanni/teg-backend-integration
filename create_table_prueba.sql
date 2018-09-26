CREATE TABLE public.prueba
(
  id integer NOT NULL DEFAULT nextval('prueba_id_seq'::regclass),
  name character varying(50) NOT NULL,
  created_date timestamp with time zone NOT NULL,
  updated_date timestamp with time zone NOT NULL,
  email character varying(50) NOT NULL,
  CONSTRAINT id_prueba PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.prueba
  OWNER TO postgres;

-- Table: public.carrera

-- DROP TABLE public.carrera;

CREATE TABLE public.carrera
(
  id integer NOT NULL DEFAULT nextval('carrera_id_seq'::regclass),
  name character varying(100) NOT NULL,
  tipo character varying(100) NOT NULL,
  id_facultad integer NOT NULL,
  created_date timestamp with time zone NOT NULL DEFAULT now(),
  updated_date timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT id_carrera PRIMARY KEY (id),
  CONSTRAINT id_facultad FOREIGN KEY (id_facultad)
      REFERENCES public.facultad (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT nombre_carrera UNIQUE (name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.carrera
  OWNER TO postgres;

-- Index: public.fki_id_facultad

-- DROP INDEX public.fki_id_facultad;

CREATE INDEX fki_id_facultad
  ON public.carrera
  USING btree
  (id_facultad);


-- Table: public.estudiante

-- DROP TABLE public.estudiante;

CREATE TABLE public.estudiante
(
  id integer NOT NULL DEFAULT nextval('estudiante_id_seq'::regclass),
  cedula character varying(100) NOT NULL,
  nacionalidad character varying(50) NOT NULL,
  nombre character varying(100) NOT NULL,
  apellido character varying(100) NOT NULL,
  sexo character varying(50) NOT NULL,
  fecha_nacimiento date NOT NULL,
  telefono1 character varying(50) NOT NULL,
  telefono2 character varying(50),
  email character varying(100) NOT NULL,
  edo_procedencia character varying(100) NOT NULL,
  id_carrera integer NOT NULL,
  created_date time with time zone NOT NULL DEFAULT now(),
  updated_date timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT id_estudiante PRIMARY KEY (id),
  CONSTRAINT id_carrera FOREIGN KEY (id_carrera)
      REFERENCES public.carrera (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT cedula_estudiante UNIQUE (cedula),
  CONSTRAINT email_estudiante UNIQUE (email)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.estudiante
  OWNER TO postgres;

-- Index: public.fki_id_carrera

-- DROP INDEX public.fki_id_carrera;

CREATE INDEX fki_id_carrera
  ON public.estudiante
  USING btree
  (id_carrera);

-- Table: public.facultad

-- DROP TABLE public.facultad;

CREATE TABLE public.facultad
(
  id integer NOT NULL DEFAULT nextval('facultad_id_seq'::regclass),
  nombre character varying(100) NOT NULL,
  created_date timestamp with time zone NOT NULL DEFAULT now(),
  updated_date timestamp with time zone NOT NULL DEFAULT (now())::timestamp without time zone,
  CONSTRAINT id_facultad PRIMARY KEY (id),
  CONSTRAINT nombre_facultad UNIQUE (nombre)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.facultad
  OWNER TO postgres;
