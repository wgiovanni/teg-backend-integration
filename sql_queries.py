from textwrap import dedent
#-------------------------------------------------------------
#TABLA PRUEBA
# extracción de los todos los registros Carga Inicial
postgresql_extract_load_initial = dedent("""\
	SELECT name, email
	FROM PRUEBA
	""")

# extracción de los registros actualizados
postgresql_extract_update = dedent("""\
	SELECT name, email
	FROM PRUEBA
	WHERE updated_date > %s 
	""")

# insertar en el DW
postgresql_insert = dedent("""\
	INSERT INTO PRUEBA (name, email)
	VALUES (%s, %s)
	""")
# actualizar en el DW
postgresql_update = dedent("""\
	UPDATE PRUEBA
   	SET name=%s, email=%s
 	WHERE id=%s;
	""")

# buscar en el DW
# el primer parametro sera el campo unico
postgresql_get = dedent("""\
	SELECT id 
	FROM PRUEBA 
	WHERE name = %s
	""")

#tipo de tabla
postgresql_type_table = "DIM"

#------------------------------------------------------------------------------------------------------
# TABLA FACULTAD: DIMENSION
# extracción de los todos los registros Carga Inicial
postgresql_extract_load_initial_facultad = dedent("""\
	SELECT nombre
	FROM FACULTAD
	""")

# extracción de los registros actualizados
postgresql_extract_update_facultad = dedent("""\
	SELECT nombre
	FROM FACULTAD
	WHERE updated_date > %s 
	""")

# insertar en el DW
postgresql_insert_facultad = dedent("""\
	INSERT INTO DIM_FACULTAD (nombre)
	VALUES (%s)
	""")

# actualizar en el DW
postgresql_update_facultad = dedent("""\
	UPDATE DIM_FACULTAD
   	SET nombre=%s
 	WHERE id=%s;
	""")

# buscar en el DW
# el primer parametro sera el campo unico
postgresql_get_facultad = dedent("""\
	SELECT id 
	FROM DIM_FACULTAD 
	WHERE nombre = %s
	""")
postgresql_type_table_facultad = "DIM"

#------------------------------------------------------------------------------------------------------
# TABLA CARRERA: DIMENSION
# extracción de los todos los registros Carga Inicial
postgresql_extract_load_initial_carrera = dedent("""\
	SELECT nombre, tipo
	FROM CARRERA
	""")

# extracción de los registros actualizados
postgresql_extract_update_carrera = dedent("""\
	SELECT nombre, tipo
	FROM CARRERA
	WHERE updated_date > %s 
	""")

# insertar en el DW
postgresql_insert_carrera = dedent("""\
	INSERT INTO DIM_CARRERA (nombre, tipo)
	VALUES (%s, %s)
	""")

# actualizar en el DW
postgresql_update_carrera = dedent("""\
	UPDATE DIM_CARRERA
   	SET nombre=%s, tipo=%s
 	WHERE id=%s;
	""")

# buscar en el DW
# el primer parametro sera el campo unico
postgresql_get_carrera = dedent("""\
	SELECT id 
	FROM DIM_CARRERA 
	WHERE nombre = %s
	""")

postgresql_type_table_carrera = "DIM"

#------------------------------------------------------------------------------------------------------
# TABLA ESTUDIANTE: DIMENSION
# extracción de los todos los registros Carga Inicial
postgresql_extract_load_initial_estudiante = dedent("""\
	SELECT cedula, nacionalidad, nombre, 
		apellido, sexo, fecha_nacimiento, 
		telefono1, telefono2, email, edo_procedencia
	FROM ESTUDIANTE
	""")

# extracción de los registros actualizados
postgresql_extract_update_estudiante = dedent("""\
	SELECT cedula, nacionalidad, nombre, 
		apellido, sexo, fecha_nacimiento, 
		telefono1, telefono2, email, edo_procedencia
	FROM ESTUDIANTE
	WHERE updated_date > %s 
	""")

# insertar en el DW
postgresql_insert_estudiante = dedent("""\
	INSERT INTO DIM_ESTUDIANTE (
		cedula, nacionalidad, nombre, 
		apellido, sexo, fecha_nacimiento, 
		telefono1, telefono2, email, edo_procedencia)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
	""")

# actualizar en el DW
postgresql_update_estudiante = dedent("""\
	UPDATE DIM_ESTUDIANTE
   	SET cedula=%s, nacionalidad=%s, nombre=%s, 
		apellido=%s, sexo=%s, fecha_nacimiento=%s, 
		telefono1=%s, telefono2=%s, email=%s, edo_procedencia=%s
 	WHERE id=%s;
	""")

# buscar en el DW
# el primer parametro sera el campo unico
postgresql_get_estudiante = dedent("""\
	SELECT id 
	FROM DIM_ESTUDIANTE
	WHERE cedula = %s
	""")

postgresql_type_table_estudiante = "DIM"

#------------------------------------------------------------------------------------------------------
# RELACION ESTUDIANTE_FACULTAD: HECHOS
# extracción de los todos los registros Carga Inicial
postgresql_extract_load_initial_estudiante_facultad = dedent("""\
	select e.cedula, f.nombre 
	FROM estudiante as e 
	INNER JOIN carrera as c ON (e.id_carrera = c.id)
	INNER JOIN facultad as f ON (c.id_facultad = f.id)
	""")

# extracción de los registros actualizados
#postgresql_extract_update_estudiante_facultad = ""
#dedent("""\
#	SELECT cedula, nacionalidad, nombre, 
#		apellido, sexo, fecha_nacimiento, 
#		telefono1, telefono2, email, edo_procedencia
#	FROM ESTUDIANTE
#	WHERE updated_date > %s 
#	""")

# insertar en el DW
postgresql_insert_estudiante_facultad = dedent("""\
	INSERT INTO FACT_ESTUDIANTE_FACULTAD (id_estudiante, id_facultad)
	VALUES (%s, %s)
	""")

# actualizar en el DW
#postgresql_update_estudiante = dedent("""\
#	UPDATE DIM_ESTUDIANTE
#   	SET cedula=%s, nacionalidad=%s, nombre=%s, 
#		apellido=%s, sexo=%s, fecha_nacimiento=%s, 
#		telefono1=%s, telefono2=%s, email=%s, edo_procedenciatipo=%s
# 	WHERE id=%s;
#	""")

# buscar en el DW
# el primer parametro sera el campo unico
postgresql_get_estudiante_facultad = dedent("""\
	SELECT id 
	FROM %s
	WHERE  id = %s
	""")

postgresql_verificate_estudiante_facultad = dedent("""\
	SELECT * 
	FROM FACT_ESTUDIANTE_FACULTAD
	WHERE id_estudiante = %s AND id_facultad = %s
	""")

postgresql_type_table_estudiante_facultad = "FACT"

postgresql_tables_estudiante_facultad = ["DIM_ESTUDIANTE", "DIM_FACULTAD"]

# exportando consultas para las tablas de dimensiones
class SqlQuery:
	def __init__(self, extract_initial_query, extract_update_query, load_query, update_query, get_query, type_table):
		self.extract_initial_query = extract_initial_query
		self.extract_update_query = extract_update_query
		self.load_query = load_query
		self.update_query = update_query
		self.get_query = get_query
		self.type_table = type_table

# exportando consultas para tablas de hechos
class SqlQueryFact:
	def __init__(self, extract_initial_query, load_query, get_query, verificate_query, type_table, tables):
		self.extract_initial_query = extract_initial_query
		self.load_query = load_query
		self.get_query = get_query
		self.verificate_query = verificate_query
		self.type_table = type_table
		self.tables = tables

class SqlLastUpdate:
	def __init__(self, get_query, update_query):
		self.get_query = get_query
		self.update_query = update_query

class SqlTableStatic:
	def __init__(self, get_query_code, load_query):
		self.get_query_code = get_query_code
		self.load_query = load_query

class SqlStudent:
	def __init__(self, get_query_code, load_query, update_query):
		self.get_query_code = get_query_code
		self.load_query = load_query
		self.update_query = update_query

class SqlTableSameParse:
	def __init__(self, get_query_code):
		self.get_query_code = get_query_code

class SqlFactRelationship:
	def __init__(self, get_query_code):
		self.get_query_code = get_query_code

# creando instancias para la clase SqlQuery 
postgresql_query = SqlQuery(
	postgresql_extract_load_initial, 
	postgresql_extract_update, 
	postgresql_insert, 
	postgresql_update, 
	postgresql_get, 
	postgresql_type_table)

# FACULTAD
postgresql_query_facultad = SqlQuery(
	postgresql_extract_load_initial_facultad, 
	postgresql_extract_update_facultad, 
	postgresql_insert_facultad, 
	postgresql_update_facultad,
	postgresql_get_facultad,
	postgresql_type_table_facultad)

# CARRERA
postgresql_query_carrera = SqlQuery(
	postgresql_extract_load_initial_carrera, 
	postgresql_extract_update_carrera, 
	postgresql_insert_carrera, 
	postgresql_update_carrera,
	postgresql_get_carrera,
	postgresql_type_table_carrera)

# ESTUDIANTE
postgresql_query_estudiante = SqlQuery(
	postgresql_extract_load_initial_estudiante, 
	postgresql_extract_update_estudiante, 
	postgresql_insert_estudiante, 
	postgresql_update_estudiante,
	postgresql_get_estudiante,
	postgresql_type_table_estudiante)

# ESTUDIANTE_FACULTAD
postgresql_query_estudiante_facultad = SqlQueryFact(
	postgresql_extract_load_initial_estudiante_facultad, 
	postgresql_insert_estudiante_facultad,
	postgresql_get_estudiante_facultad,
	postgresql_verificate_estudiante_facultad,
	postgresql_type_table_estudiante_facultad,
	postgresql_tables_estudiante_facultad)


# almacenando como lista para iteraciones
postgresql_queries = [
	postgresql_query, 
	postgresql_query_facultad, 
	postgresql_query_carrera, 
	postgresql_query_estudiante, 
	postgresql_query_estudiante_facultad]



# Querys para tablas donde se almacena la informacion de los estudiantes 
# consultas para la actualizacion
get_last_update = dedent("""\
	SELECT * FROM last_update""")

update_last_update = dedent("""\
	UPDATE last_update SET is_load_initial=%s, last_update=NOW() WHERE id = %s""")

last_update = SqlLastUpdate(get_last_update, update_last_update)

# consultas para tablas estaticas

get_nationality_code = dedent("""\
	SELECT id FROM dim_nacionalidad WHERE codigo = %s""") 

insert_nationality = dedent("""\
	INSERT INTO dim_nacionalidad (codigo) VALUES (%s)""")

get_sex_code = dedent("""\
	SELECT id FROM dim_sexo WHERE codigo = %s""") 

insert_sex = dedent("""\
	INSERT INTO dim_sexo (codigo) VALUES (%s)""")

# consultas para estudiante
get_student_code = dedent("""\
	SELECT id FROM dim_estudiante WHERE cedula = %s""")

insert_student = dedent("""\
	INSERT INTO dim_estudiante
		(cedula, nombre, apellido, fecha_nacimiento, telefono1, telefono2, email, edo_procedencia)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

update_student = dedent("""\
	UPDATE dim_estudiante
	SET cedula = %s, nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono1=%s, telefono2=%s, email=%s, edo_procedencia=%s
	WHERE id=%s""")

# consultas para carrera
get_profession_code = dedent("""\
	SELECT id FROM dim_carrera WHERE nombre = %s""")

# consultas para faculty
get_faculty_code = dedent("""\
	SELECT id FROM dim_facultad WHERE nombre = %s""")

# consulta para verificar
get_relationship_student = dedent("""\
	SELECT fact.id 
	FROM fact_estudiante_facultad AS fact 
	INNER JOIN dim_estudiante AS e 
	ON (fact.id_estudiante = e.id) WHERE cedula = %s""") 

nationalityQuery = SqlTableStatic(get_nationality_code, insert_nationality)
sexQuery = SqlTableStatic(get_sex_code, insert_sex)
studentQuery = SqlStudent(get_student_code, insert_student, update_student)
professionQuery = SqlTableSameParse(get_profession_code)
facultyQuery = SqlTableSameParse(get_faculty_code)
studentRelationship = SqlFactRelationship(get_relationship_student)



