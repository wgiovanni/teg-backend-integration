from textwrap import dedent
# extracción
postgresql_extract = dedent("""\
	SELECT name, created_date, updated_date 
	FROM PRUEBA
	WHERE updated_date > '2018-09-23 06:05:06-04' 
	""")

# insertar
postgresql_insert = dedent("""\
	INSERT INTO PRUEBA (name, created_date, updated_date)
	VALUES (%s, %s, %s)
	""")
# actualizar
postgresql_update = dedent("""\
	UPDATE PRUEBA
   	SET name=%s, created_date=%s, updated_date=%s
 	WHERE id = %s;
	""")

# buscar 
postgresql_get = dedent("""\
	SELECT id 
	FROM PRUEBA 
	WHERE name = %s
	""")

# exportando consultas
class SqlQuery:
	def __init__(self, extract_query, load_query, update_query, get_query):
		#print(extract_query)
		#print("\n")
		#print(load_query)
		self.extract_query = extract_query
		self.load_query = load_query
		self.update_query = update_query
		self.get_query = get_query

# creando instancias para la clase SqlQuery 
postgresql_query = SqlQuery(postgresql_extract, postgresql_insert, postgresql_update, postgresql_get)

# almacenando como lista para iteraciones
postgresql_queries = [postgresql_query]