# modulos python
import psycopg2
import mysql.connector
from datetime import datetime
# variables
from variables import datawarehouse_name

def etl(query, source_cnx, target_cnx):
	# extraer datos de la fuente db
	source_cursor = source_cnx.cursor()
	print("ETL \n")
	#dateCurrent = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
	# buscar ultima fecha de actualizacion
	target_cursor = target_cnx.cursor()
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute("SELECT * FROM LAST_UPDATE")
	row = target_cursor.fetchone()

	if row is not None:

		if row[1] == False: 
			# si es actualizacion
			lastUpdate = [row[2]]
			print(lastUpdate)
			source_cursor.execute(query.extract_update_query, lastUpdate)
			data = source_cursor.fetchall()
			print(data)
			source_cursor.close()

			if data:
				for d in data:
					params = list(d)
					if params[0] is not None:
						# buscar registro
						target_cursor.execute(query.get_query, [params[0]])
						# se obtiene el registro
						rowExists = target_cursor.fetchone()

						if rowExists is not None:
							params.append(rowExists[0])
							target_cursor.execute(query.update_query, params)
							print("Actualizo...")
						else:
							target_cursor.execute(query.load_query, params)
							print("Inserto...")

						target_cnx.commit()

				print('Cargando datos al data warehouse')
				target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
				target_cnx.commit()
				print("Actualizando fecha actualizacion")
			else:
				print('Los datos estan vacios')
		else:
			# modo carga inicial
			source_cursor.execute(query.extract_initial_query)
			data = source_cursor.fetchall()
			if data:
				target_cursor.executemany(query.load_query, data)
				target_cnx.commit()
				print('Carga Inicial Lista...')
				target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
				target_cnx.commit()
				print("Actualizando fecha actualizacion")
			else: 
				print('Los datos estan vacios')
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")		
	target_cursor.close() 

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
		#print(query)
		etl(query, source_cnx, target_cnx)

	# cerra la conexion de fuente de db
	source_cnx.close()
