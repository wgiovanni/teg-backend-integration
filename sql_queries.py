from textwrap import dedent
# extracción
postgresql_extract = dedent("""\
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

# exportando consultas
class SqlQuery:
	def __init__(self, extract_query, load_query, update_query, get_query):
		self.extract_query = extract_query
		self.load_query = load_query
		self.update_query = update_query
		self.get_query = get_query

# creando instancias para la clase SqlQuery 
postgresql_query = SqlQuery(postgresql_extract, postgresql_insert, postgresql_update, postgresql_get)

# almacenando como lista para iteraciones
postgresql_queries = [postgresql_query]