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