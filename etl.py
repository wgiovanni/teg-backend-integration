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
	print(query.extract_query)
	#dateCurrent = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
	# buscar ultima fecha de actualizacion
	target_cursor = target_cnx.cursor()
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute("SELECT * FROM LAST_UPDATE")
	dateUpdated = target_cursor.fetchone()
	print(dateUpdated)
	if dateUpdated is None:
		dateUpdated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		lastUpdate = [dateUpdated]
		target_cursor.execute("INSERT INTO LAST_UPDATE (last_update) VALUES (NOW())")
		target_cnx.commit()
	else:  
		lastUpdate = [dateUpdated[1]]

	print(lastUpdate)
	source_cursor.execute(query.extract_query, lastUpdate)
	data = source_cursor.fetchall()
	print(data)
	source_cursor.close()

	# cargar datos en el data warehouse db
	if data:
		print("Si tiene data")
		# modo actualizacion
		for d in data:
			params = list(d)
			print(params)
			#print("\n")
			if(params[0] is not None):
				print("Entro")
				print(params[0])
	
				#buscar registro
				target_cursor.execute(query.get_query, [params[0]])
				rowExists = target_cursor.fetchone() #se obtiene el registro

				#print(row)
				print(rowExists)


				if rowExists is not None:
					#row.insert(0,rowExists[0]) #se obtiene el id del registro
					#row = tuple(row)
					print(params)
					print("\n")
					#print(row)
					#row = ['Wilkel', 'w@gmail.com', 17]
					params.append(rowExists[0])
					print(params)
					target_cursor.execute(query.update_query, params)
					print("Actualizo...")
				else:
					print(params)
					#row = tuple(row)
					target_cursor.execute(query.load_query, params)
					print("Inserto...")
				
				target_cnx.commit()


				target_cursor.execute("UPDATE LAST_UPDATE SET last_update=NOW() WHERE id = %s", [dateUpdated[0]])
				target_cnx.commit()
				#target_cursor.execute("INSERT INTO LAST_UPDATE (last_update) VALUES ()")

		#print(query.load_query)
		#print("\n")

		# modo carga inicial

		#target_cursor.executemany(query.load_query, data)
		#target_cnx.commit()
		print('Cargando datos al data warehouse')
		#target_cursor.close()
	else:
		print('Los datos estan vacios')
		

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
