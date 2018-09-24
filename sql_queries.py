from textwrap import dedent
# extracción
postgresql_extract = dedent("""\
	SELECT name, created_date, updated_date 
	FROM PRUEBA
	WHERE updated_date > '2018-09-22' 
	""")

# insertar
postgresql_insert = dedent("""\
	INSERT INTO PRUEBA (name, created_date, updated_date)
	VALUES (%s, %s, %s) 
	""")

# exportando consultas
class SqlQuery:
	def __init__(self, extract_query, load_query):
		print(extract_query)
		print("\n")
		print(load_query)
		self.extract_query = extract_query
		self.load_query = load_query

# creando instancias para la clase SqlQuery 
postgresql_query = SqlQuery(postgresql_extract, postgresql_insert)

# almacenando como lista para iteraciones
postgresql_queries = [postgresql_query]