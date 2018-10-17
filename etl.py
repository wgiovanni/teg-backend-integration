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
from sql_queries import last_update, nationalityQuery, sexQuery, studentQuery, professionQuery, facultyQuery, studentRelationship
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
	target_cursor.execute()
	row = target_cursor.fetchone(last_update.get_query)

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
	target_cursor.execute(last_update.get_query)
	row = target_cursor.fetchone()
	print(row)
	dimension = "dim-"
	hechos = "hechos-"
	table = ''
	if row is not None:
		if row[1] == False:
			#actualizacion
			print("Actualizacion")
			data = requestUpdate(row[2])
			print(data)
			keyList= data.keys()
			keyList = sorted(keyList)
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
				distributionUpdate(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			dataList = requestCargaInitial()
			print(dataList)
			print("\n\n")
			for data in dataList:
				print(data)
				print("\n")
				# ordenamiento: ESTO ES RELEVANTE
				keyList= data.keys()
				keyList = sorted(keyList)
				#insercion
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
					distributionCargaInitial(target_cnx, table, content)

		target_cursor.execute(last_update.update_query, [False, row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")
	
	target_cursor.close()

def requestCargaInitial():
	base_url = "http://127.0.0.1:"
	headers = {'content-type': 'application/json'}
	pathList = []
	pathList.append("8082/estudiantes")
	pathList.append("8082/profesores")
	result = []
	for path in pathList:
		try:
			r = requests.get(base_url + path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

	return result
	

def requestUpdate(lastUpdate):
	base_url = "http://127.0.0.1:8082"
	path = "/estudiantes"
	headers = {'content-type': 'application/json'} 

	path = f"/estudiantes/{lastUpdate}"
	try:
		result = ''
		r = requests.get(base_url + path, headers=headers)
		if r.status_code == requests.codes.ok:
			result = json.loads(r.text)
	except Exception as e:
		abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
	except r.raise_for_status() as e:
		abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

	return result


def distributionCargaInitial(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == "estudiante":
		items = content['items']
		print(items)
		print("\n")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			print(item)
			nationalityCode = item['nacionalidad']
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item['sexo']
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))
			# aqui iran todas las dimensiones que saldran de estudiantes
			student = [
				item['cedula'],  
				item['nombre'], 
				item['apellido'], 
				item['fecha_nacimiento'],
				item['telefono1'], 
				item['telefono2'],
				item['email'],
				item['edo_procedencia']
			]
			target_cursor.execute(studentQuery.load_query, student)
			target_cnx.commit()
			target_cursor.execute(studentQuery.get_query_code, [item['cedula']])
			idStudent = target_cursor.fetchone()
			print(idStudent)

			# insertar estudiante con sexo y nacionalidad...

			target_cursor.execute(dedent("""\
			INSERT INTO FACT_ESTUDIANTE_FACULTAD 
				(id_estudiante, id_sexo, id_nacionalidad)
			VALUES (%s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0]])
			target_cnx.commit()
	elif table == "carrera":
		print("DEMAS TABLAS")
		items = content['items']
		for item in items:
			insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")

	elif table == "facultad":
		print("DEMAS TABLAS")
		items = content['items']
		for item in items:
			insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")
	elif table == "estudiante-carrera-facultad":
		items = content['items']
		for item in items:
			professionCode = item['carrera']
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item['facultad']
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()

			studentCode = item['estudiante']
			target_cursor.execute(studentRelationship.get_query_code, [studentCode])
			idFact = target_cursor.fetchone()
			

			target_cursor.execute(dedent("""\
			UPDATE fact_estudiante_facultad
			SET id_facultad=%s, id_carrera=%s
			WHERE id=%s;"""), [idFaculty[0], idProfession[0], idFact[0]])
			#insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")
	elif table == "docente":
		print("DOCENTE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

	target_cursor.close()


def distributionUpdate(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == "estudiante":
		items = content['items']
		print(items)
		print("Cargando estudiantes...")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			nationalityCode = item['nacionalidad']
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print("nacionalidad: {}".format(idNationality))
			sexCode = item['sexo']
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))
			# aqui iran todas las dimensiones que saldran de estudiantes
			student = [
				item['cedula'],  
				item['nombre'], 
				item['apellido'], 
				item['fecha_nacimiento'],
				item['telefono1'], 
				item['telefono2'],
				item['email'],
				item['edo_procedencia']
			]
			target_cursor.execute(studentQuery.get_query_code, [item['cedula']])
			idStudentExist = target_cursor.fetchone()
			if idStudentExist is not None:
				student.append(idStudentExist[0])
				print(student)
				target_cursor.execute(studentQuery.update_query, student)
				target_cnx.commit()
				target_cursor.execute(studentRelationship.get_query_code,[item['cedula']])
				idFact = target_cursor.fetchone()
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_estudiante_facultad
					SET id_estudiante=%s, id_sexo=%s, id_nacionalidad=%s
					WHERE id = %s"""), [idStudentExist[0], idSex[0], idNationality[0], idFact[0]])
					target_cnx.commit()
				else: 
					print("No existe el registro")
				
			else:			
				target_cursor.execute(studentQuery.load_query, student)
				target_cnx.commit()
				target_cursor.execute(studentQuery.get_query_code, [item['cedula']])
				idStudent = target_cursor.fetchone()
				target_cursor.execute(dedent("""\
				INSERT INTO FACT_ESTUDIANTE_FACULTAD 
					(id_estudiante, id_sexo, id_nacionalidad)
				VALUES (%s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0]])
			
	elif table == "facultad":
		print("DEMAS TABLAS")
		print("Cargando facultad...")
		items = content['items']
		for item in items:
			target_cursor.execute(facultyQuery.get_query_code, [item['nombre']])
			row = target_cursor.fetchone()
			if row is not None:
				#params = list(item)
				#params.append(row[0])
				#target_cursor.execute(f"UPDATE DIM_{table} SET nombre = %s WHERE id = %s", params)
				update(target_cursor, table, item, {"id": row[0]})
			else: 
				insert(target_cursor, table, item)
			
			target_cnx.commit()
		print("Insercion finalizada")
	
	elif table == "carrera":
		print("DEMAS TABLAS")
		print("Cargando carrera...")
		items = content['items']
		for item in items:
			target_cursor.execute(professionQuery.get_query_code, [item['nombre']])
			row = target_cursor.fetchone()
			if row is not None:
				#params = list(item)
				#params.append(row[0])
				#target_cursor.execute(f"UPDATE DIM_{table} SET nombre = %s, tipo = %s WHERE id = %s", params)
				update(target_cursor, table, item, {"id": row[0]})
			else: 
				insert(target_cursor, table, item)
			
			target_cnx.commit()
		print("Insercion finalizada")

	elif table == "estudiante-carrera-facultad":
		print("Cargando relacion...")
		items = content['items']
		for item in items:
			professionCode = item['carrera']
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item['facultad']
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()
			
			studentCode = item['estudiante']

			target_cursor.execute(studentQuery.get_query_code, [studentCode])
			idStudent = target_cursor.fetchone()

			target_cursor.execute(studentRelationship.get_query_code, [studentCode])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				target_cursor.execute(dedent("""\
				UPDATE fact_estudiante_facultad
				SET id_estudiante=%s, id_facultad=%s, id_carrera=%s
				WHERE id=%s;"""), [idStudent[0], idFaculty[0], idProfession[0], idFact[0]])
				target_cnx.commit()
				print("Registro actualizado")
			else:
				print("Registro no existe")
		print("Insercion finalizada")
	target_cursor.close()


def insertTableStatic(target_cnx):
	target_cursor = target_cnx.cursor()
	male = "Masculino"
	female = "Femenino"
	sexParams = [(male,), (female,)]
	target_cursor.execute(sexQuery.get_verify, [male, female])
	sexList = target_cursor.fetchall()
	print(sexList)
	if len(sexList) != 2:
		target_cursor.executemany(sexQuery.load_query, sexParams)
		target_cnx.commit()
	
	national = "Venezolano"
	international = "Extranjero"
	nationalityParams = [(national,), (international,)]
	target_cursor.execute(nationalityQuery.get_verify, [national, international])
	nationalityList = target_cursor.fetchall()
	print(nationalityList)
	if len(nationalityList) != 2:
		target_cursor.executemany(nationalityQuery.load_query, nationalityParams)
		target_cnx.commit()
	#statusParams = [("Activo1",), ("Inactivo1",)]
	#target_cursor.executemany("INSERT INTO DIM_STATUS (codigo) VALUES (%s)", statusParams)
	#target_cnx.commit()
	


def insert(cursor, table: str, datos: dict=None, columns=None, values: list=None):
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
		sql = f"insert into dim_{table} {columns} values {marks}", values
		cursor.execute(sql, values)
	else:
		marks = "(%s" + (",%s" * (len(values) - 1)) + ")"
		sql = f"insert into dim_{table} {columns} values {marks}"
		cursor.execute(sql, values)	

def update(cursor, table: str, datos: dict, where: dict):

	sql = f"update {table} set "
	values = []
	for col, val in datos.items():
		if val is not None:
			sql += f"{col} = %s, "
			values.append(val)

	sql = sql.rstrip(', ')
	sql += " where "
	for col, val in where.items():
		sql += f"{col} = %s and "
		values.append(val)

	sql = sql.rstrip(' and ')
	cursor.execute(sql, values)