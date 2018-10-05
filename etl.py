# modulos python
from flask_restful import abort
import psycopg2
import mysql.connector
from datetime import datetime
from textwrap import dedent
import simplejson as json
import requests
from common.BD import BD
from db_credentials import datawarehouse_db_config
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
	print("ETL \n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor()
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute("SELECT * FROM LAST_UPDATE")
	row = target_cursor.fetchone()
	print(row)
	if row is not None:
		if row[1] == False:
			#actualizacion
			print("Actualizacion")
		else:
			print("Insercion")
			# insercion de tablas estaticas
			insertTableStatic()
			data = request()
			# ordenamiento: ESTO ES RELEVANTE
			
			keyList= data.keys()
			keyList = sorted(keyList)
			#print(keyList)
			#insercion
			dimension = "dim-"
			hechos = "hechos-"
			for key in keyList:
				print("KEY:{}".format(key))
				if dimension in key:
					print("Dimension")
					#picar string
					table = key[len(dimension):]
				elif hechos in key:
					print("Hechos")
					#picar string
					table = key[len(hechos):]
				content = data[key]
				print("\n\n")
				print(table)
				print(content)
				distribution(target_cursor,table, content)
				#insert(target_cnx, table, content)
				#target_cnx.commit()
				#insert(table, content['']) 

def request():
	base_url = "http://127.0.0.1:8082"
	path = "/estudiantes"
	headers = {'content-type': 'application/json'}

	try:
		result = ''
		r = requests.get(base_url + path, headers=headers)
		if r.status_code == requests.codes.ok:
			result = json.loads(r.text)
			#
			#student = result["estudiante"]
			#for row in student:
			#	print(row)
	except Exception as e:
		abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
	except r.raise_for_status() as e:
		abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

	return result
	
	#payload ="2018-09-26 11:01:00"
	#path = f"/estudiantes/{payload}"
	#r = requests.get(base_url + path, headers=headers)
	#if r.status_code == requests.codes.ok:
	#result = json.loads(r.text)
	#print("\n")
	#print("\n")
	#student = result["estudiante"]
	#for row in student:
	#	print(row)

#def process()
def distribution(target_cursor, table: str, content: dict):
	if table == "estudiante":
		nacionalidad = [content['nacionalidad']]
		sexo = {"codigo": content['sexo']}
		#status = {"codigo": content['status']}
		target_cursor.execute("SELECT * FROM DIM_NACIONALIDAD")
		row = target_cursor.fetchAll()
		if row is not None:
			target_cursor.execute("SELECT * FROM DIM_NACIONALIDAD WHERE codigo = %s", nacionalidad)
			target_cursor.fetchone()
		else:
			target_cursor.execute("INSERT INTO DIM_NACIONALIDAD codigo VALUES (%s)", nacionalidad)	
	else:
		#todo normal	

def insertTableStatic(target_cursor):
	sexParams = ["Masculino", "Femenino"]
	target_cursor.executemany("INSERT INTO DIM_SEXO codigo VALUES (%s)", sexParams)
	target_cursor.commit()


def insert(cursor, table: str, datos: dict=None, columns=None, values: list=None):
		"""
		Inserta uno o varios registros en una tabla.

		:param table: Nombre de la tabla.
		:param datos: Diccionario con las keys para los nombres de columnas y los valores para insertar.\n
			Ej. {"id": 1, "first_name": "Jose", ...}\n
			Este diccionario sobreescribe los valores de los parámetros columns y values.
		:param columns: Columnas de la tabla donde se van a insertar los datos.\n
			Puede ser un string separado por comas. ej. 'id, first_name, ...'\n
			Puede ser una lista de string. ej. ['id', 'first_name', ...]\n
		:param values: Lista de valores a insertar en la tabla.\n
			Puede ser una lista de valores simples para un solo registro. ej. [1, 'Jose', ...]\n
			Puede ser una lista de tuplas para insertar varios registros. ej. [(1, 'Jose', ...), (2, 'Jesus', ...), ...]
		"""
		#self.connect()
		cursor = cursor.cursor()

		if datos is not None:
			columns = []
			values = []
			for col, val in datos.items():
				columns.append(col)
				values.append(val)

		if isinstance(columns, str):
			columns = "("+columns+")"
		elif isinstance(columns, list):
			columns = "("+", ".join(columns)+")"


		if isinstance(values[0], (list, tuple)):
			marks = "(%s" + (",%s" * (len(values[0]) - 1)) + ")"
			sql = f"insert into {table} {columns} values {marks}", values
			cursor.execute(sql, values)
		else:
			marks = "(%s" + (",%s" * (len(values) - 1)) + ")"
			sql = f"insert into {table} {columns} values {marks}"
			cursor.execute(sql, values)	

		cursor.close()