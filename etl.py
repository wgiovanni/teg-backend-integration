# modulos python
import psycopg2
import mysql.connector
from datetime import datetime
from textwrap import dedent
import simplejson as json
import requests
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

	if query.type_table == "DIM":

		if row is not None:

			if row[1] == False: 
				# si es actualizacion
				lastUpdate = [row[2]]
				#print(lastUpdate)
				source_cursor.execute(query.extract_update_query, lastUpdate)
				data = source_cursor.fetchall()
				print("Actualizacion")
				#print(data)
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
					#target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
					#target_cnx.commit()
					print("Actualizando fecha actualizacion")
				else:
					print('Los datos estan vacios')
			else:
				# modo carga inicial
				source_cursor.execute(query.extract_initial_query)
				data = source_cursor.fetchall()
				print("Carga inicial")
				#print(data)
				if data:
					target_cursor.executemany(query.load_query, data)
					target_cnx.commit()
					print('Carga Inicial Lista...')
					#target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
					#target_cnx.commit()
					print("Actualizando fecha actualizacion")
				else: 
					print('Los datos estan vacios')
		else:
			print("Debe llenar un registro en la Tabla 'last_update'")		
	else:
		source_cursor.execute(query.extract_initial_query)
		data = source_cursor.fetchall()
		print("Tabla de hechos...")
		#print(query.type_table)
		#print(data)
		if data:
			for d in data:
				if len(d) == len(query.tables):
					print("Longitudes iguales")
					#print(d)
					ids = []
					for i in range(len(d)):
						#print(query.tables[i])
						#print(d[i])
						id = select_query(query.tables[i], d[i], target_cursor)
						if id is not None:
							ids.append(id[0])
						else: 
							ids.append(None)
						#print(ids)
					target_cursor.execute(query.verificate_query, ids)
					foundRegister = target_cursor.fetchone()
					#print(foundRegister)
					if foundRegister is None:
						target_cursor.execute(query.load_query, ids)
						target_cnx.commit()
						print("Llenando tablas de hechos...")
					else:
						print("Ya existen los registros") 	
				else:	
					print("Longitudes diferentes")
	target_cursor.close()	


def etl_process(queries, target_cnx, source_db_config, db_platform):
	# establecer la conexion de fuentes de db
	if db_platform == 'mysql':
		source_cnx = mysql.connector.connect(**source_db_config)
	elif db_platform == 'postgresql':
		#print("Entro postgresql")
		#print(source_db_config)
		#print(source_db_config.user)
		source_cnx = psycopg2.connect(**source_db_config)
		#print("conecto")
	else:
		return 'Error! plataforma db no reconocida'

	
	# ciclo a traves de consultas sql
	for query in queries:
		#print(query)
		etl(query, source_cnx, target_cnx)

	target_cursor = target_cnx.cursor()
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute("SELECT * FROM LAST_UPDATE")
	row = target_cursor.fetchone()
	#print(row)
	# Despues de del proceso ETL de cada tabla se actualiza la fecha de actualizacion
	if row is not None:
		#if row[1]:
		target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
		#else:
		#	target_cursor.execute("UPDATE LAST_UPDATE SET is_load_initial=%s, last_update=NOW() WHERE id = %s", [False, row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha")
			
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")

	# cerra la conexion de fuente de db
	target_cursor.close()
	source_cnx.close()

def select_query(table: str, param: str, target_cursor):
	sql = dedent(f"""\
	SELECT COLUMN_NAME 
	FROM INFORMATION_SCHEMA.COLUMNS 
	WHERE TABLE_SCHEMA = 'PRUEBA' AND TABLE_NAME = '{table}' AND COLUMN_KEY = 'UNI'""")
	#print(sql)
	target_cursor.execute(sql)
	col = target_cursor.fetchone()
	#print(col)

	query = dedent(f"""\
		SELECT id 
		FROM {table} 
		WHERE {col[0]}  = '{param}'""")
	#print(query)
	target_cursor.execute(query)
	row = target_cursor.fetchone()
	#print(row)
	return row

def etl_process2():
	base_url = "http://127.0.0.1:8082"
	path = "/estudiantes"
	headers = {'content-type': 'application/json'}
	r = requests.get(base_url + path, headers=headers)
	#print(r.text)
	#if r.status_code == requests.codes.ok:
	result = json.loads(r.text)
	#print(student)
	student = result["estudiante"]
	for row in student:
		print(row)

	
	payload ="2018-09-26 11:01:00"
	path = f"/estudiantes/{payload}"
	r = requests.get(base_url + path, headers=headers)
	#if r.status_code == requests.codes.ok:
	result = json.loads(r.text)
	print("\n")
	print("\n")
	student = result["estudiante"]
	for row in student:
		print(row)