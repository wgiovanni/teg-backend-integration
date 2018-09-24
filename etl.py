# modulos python
import psycopg2
import mysql.connector

# variables
from variables import datawarehouse_name

def etl(query, source_cnx, target_cnx):
	# extraer datos de la fuente db
	source_cursor = source_cnx.cursor()
	print("ETL \n")
	print(query.extract_query)
	source_cursor.execute(query.extract_query)
	data = source_cursor.fetchall()
	print(data)
	source_cursor.close()

	# cargar datos en el data warehouse db
	if data:
		print("Si tiene data")
		target_cursor = target_cnx.cursor()
		#target_cursor.execute("USE {}".format(datawarehouse_name))
		for d in data:
			aux = list(d)
			print(aux)
			print("\n")
			if(aux[0] is not None):
				print("Entro")
				print(aux[0])
				print(query.get_query)
				aux2 = [aux[0]]
				target_cursor.execute(query.get_query, aux2)
				rowExists = target_cursor.fetchone()
				rowUpdate = [rowExists[0]]
				rowUpdate.append(aux[1:len(aux)])
				print(rowExists)
				print(rowUpdate)

				#target_cursor.execute(query.update_query, rowExists)
		print(query.load_query)
		print("\n")
		#target_cursor.executemany(query.load_query, data)
		#target_cnx.commit()
		print('Cargando datos al data warehouse')
		target_cursor.close()
	else:
		print('Los datos estan vacios')

def etl_process(queries, target_cnx, source_db_config, db_platform):
	# establecer la conexion de fuentes de db
	if db_platform == 'mysql':
		source_cnx = mysql.connector.connect(**source_db_config)
	elif db_platform == 'postgresql':
		print("Entro postgresql")
		print(source_db_config)
		#print(source_db_config.user)
		source_cnx = psycopg2.connect(**source_db_config)
		print("conecto")
	else:
		return 'Error! plataforma db no reconocida'

	# ciclo a traves de consultas sql
	for query in queries:
		print(query)
		etl(query, source_cnx, target_cnx)

	# cerra la conexion de fuente de db
	source_cnx.close()
