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
from sql_queries import systemParameter, nationalityQuery, sexQuery, studentQuery, teacherQuery, professionQuery, facultyQuery, publicationQuery, scaleQuery, studentRelationship, gradeQuery, teacherFacultyRelationship, teacherPublicationRelationship
from constants import LOAD_INITIAL_UPDATE, ENDPOINT_LOAD_STUDENTS, ENDPOINT_LOAD_TEACHERS, ENDPOINT_LOAD_GRADUATES, CONTENT_TYPE
from constants import DIMENSION, FACT, ITEMS, STUDENT, PROFESSION, FACULTY, STUDENT_PROFESSION_FACULTY, TEACHER, SCALE, GRADE, PUBLICATION, TEACHER_PUBLICATION, TEACHER_FACULTY
from constants import NACIONALITY_ATTRIBUTE, SEX_ATTRIBUTE, IDENTIFICATION_CARD, FIRST_NAME_ATRIBUTE, LAST_NAME_ATRIBUTE, BIRTH_DATE_ATTRIBUTE, PHONE_ONE_ATTRIBUTE, PHONE_TWO_ATTRIBUTE, EMAIL_ATTRIBUTE, STATE_PROVENANCE_ATTRIBUTE, WORK_AREA_ATTRIBUTE, CITE_ATTRIBUTE
from constants import MALE, FEMALE, NATIONAL, INTERNACIONAL
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
	row = target_cursor.fetchone(systemParameter.get_query)

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
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	print(row)
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			dataList = requestUpdate(target_cnx, row[6].strftime('%Y-%m-%d %H:%M:%S'))
			
			for data in dataList:
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
			dataList = requestCargaInitial(target_cnx)
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

		target_cursor.execute(systemParameter.update_query, [False, row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")
	
	target_cursor.close()

def requestCargaInitial(target_cnx):
	
	headers = CONTENT_TYPE
	pathList = []
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	#target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	#endPointGraduated = target_cursor.fetchone()
	pathList.append(endPointStudent[4])
	pathList.append(endPointTeacher[4])
	print(pathList)
	#pathList.append(endPointGraduated[4])
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

	return result
	

def requestUpdate(target_cnx, lastUpdate):
	headers = CONTENT_TYPE
	pathList = []
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	#target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	#endPointGraduated = target_cursor.fetchone()
	pathList.append(endPointStudent[4]+"/{}".format(lastUpdate))
	pathList.append(endPointTeacher[4]+"/{}".format(lastUpdate))
	#pathList.append(endPointGraduated[4]) 
	print(pathList)
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

	return result


def distributionCargaInitial(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == STUDENT:
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			print(item)
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))
			# aqui iran todas las dimensiones que saldran de estudiantes
			student = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[BIRTH_DATE_ATTRIBUTE],
				item[PHONE_ONE_ATTRIBUTE], 
				item[PHONE_TWO_ATTRIBUTE],
				item[EMAIL_ATTRIBUTE],
				item[STATE_PROVENANCE_ATTRIBUTE]
			]
			target_cursor.execute(studentQuery.load_query, student)
			target_cnx.commit()

			target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idStudent = target_cursor.fetchone()
			print(idStudent)

			# insertar estudiante con sexo y nacionalidad...

			target_cursor.execute(dedent("""\
			INSERT INTO FACT_ESTUDIANTE_FACULTAD 
				(id_estudiante, id_sexo, id_nacionalidad)
			VALUES (%s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0]])
			target_cnx.commit()
	elif table == PROFESSION:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(professionQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			profession = target_cursor.fetchone()
			if profession is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")

	elif table == FACULTY:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(facultyQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			faculty = target_cursor.fetchone()
			if faculty is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")
	elif table == STUDENT_PROFESSION_FACULTY:
		items = content[ITEMS]
		for item in items:
			professionCode = item[PROFESSION]
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()

			studentCode = item[STUDENT]
			target_cursor.execute(studentRelationship.get_query_code, [studentCode])
			idFact = target_cursor.fetchone()
			

			target_cursor.execute(dedent("""\
			UPDATE fact_estudiante_facultad
			SET id_facultad=%s, id_carrera=%s
			WHERE id=%s;"""), [idFaculty[0], idProfession[0], idFact[0]])
			#insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")
	elif table == TEACHER:
		print("DOCENTE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			scaleCode = item[SCALE]
			target_cursor.execute(scaleQuery.get_query_code, [scaleCode])
			idScale = target_cursor.fetchone()
			print("escalafon: {}".format(idScale))

			gradeCode = item[GRADE]
			target_cursor.execute(gradeQuery.get_query_code, [gradeCode])
			idGrade = target_cursor.fetchone()
			print("grado: {}".format(idGrade))

			teacher = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[EMAIL_ATTRIBUTE],
				item[WORK_AREA_ATTRIBUTE]
			]
			target_cursor.execute(teacherQuery.load_query, teacher)
			target_cnx.commit()

			target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idTeacher = target_cursor.fetchone()
			print(idTeacher)

			# insertar estudiante con sexo y nacionalidad...

			target_cursor.execute(dedent("""\
			INSERT INTO FACT_DOCENTE_FACULTAD 
				(id_docente, id_sexo, id_nacionalidad, id_escalafon, id_grado)
			VALUES (%s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idGrade[0]])
			target_cnx.commit()
		print("INSERCION DOCENTE FINALIZADA")

	elif table == SCALE:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(scaleQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			scale = target_cursor.fetchone()
			if scale is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")
	elif table == PUBLICATION:
		items = content[ITEMS]
		for item in items:
			insert(target_cursor, table, item)
			target_cnx.commit()
			print("Insercion finalizada")
	elif table == TEACHER_PUBLICATION:
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(teacherQuery.get_query_code, [item[TEACHER]])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(facultyQuery.get_query_code, [item[FACULTY]])
			idFaculty = target_cursor.fetchone()

			target_cursor.execute(publicationQuery.get_query_code, [item[PUBLICATION]])
			idPublication = target_cursor.fetchone()

			if idTeacher is not None and idFaculty is not None and idPublication is not None: 
				target_cursor.execute(dedent("""\
					INSERT INTO FACT_DOCENTE_PUBLICACION 
						(id_docente, id_publicacion, id_facultad, cantidad_citas)
					VALUES (%s, %s, %s, %s)"""), [idTeacher[0], idPublication[0], idFaculty[0], item[CITE_ATTRIBUTE]])
				target_cnx.commit()
				print("INSERTO DOCENTE, PUBLICACION Y FACULTAD")
	elif table == TEACHER_FACULTY:
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[TEACHER]])
			idFact = target_cursor.fetchone()

			target_cursor.execute(facultyQuery.get_query_code, [item[FACULTY]])
			idFaculty = target_cursor.fetchone()

			if idFact is not None and idFaculty is not None: 
				target_cursor.execute(dedent("""\
					UPDATE fact_docente_facultad
					SET id_facultad=%s
					WHERE id=%s;"""), [idFaculty[0], idFact[0]])
				target_cnx.commit()
				print("INSERTO DOCENTE, PUBLICACION Y FACULTAD")

	
	target_cursor.close()


def distributionUpdate(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == STUDENT:
		items = content[ITEMS]
		print(items)
		print("Cargando estudiantes...")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))
			# aqui iran todas las dimensiones que saldran de estudiantes
			student = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[BIRTH_DATE_ATTRIBUTE],
				item[PHONE_ONE_ATTRIBUTE], 
				item[PHONE_TWO_ATTRIBUTE],
				item[EMAIL_ATTRIBUTE],
				item[STATE_PROVENANCE_ATTRIBUTE]
			]
			target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idStudentExist = target_cursor.fetchone()
			if idStudentExist is not None:
				student.append(idStudentExist[0])
				print(student)
				target_cursor.execute(studentQuery.update_query, student)
				target_cnx.commit()
				target_cursor.execute(studentRelationship.get_query_code,[item[IDENTIFICATION_CARD]])
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
				target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
				idStudent = target_cursor.fetchone()
				target_cursor.execute(dedent("""\
				INSERT INTO FACT_ESTUDIANTE_FACULTAD 
					(id_estudiante, id_sexo, id_nacionalidad)
				VALUES (%s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0]])
			
	elif table == FACULTY:
		print("DEMAS TABLAS")
		print("Cargando facultad...")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(facultyQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
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
	
	elif table == PROFESSION:
		print("DEMAS TABLAS")
		print("Cargando carrera...")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(professionQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			row = target_cursor.fetchone()
			if row is not None:
				update(target_cursor, table, item, {"id": row[0]})
			else: 
				insert(target_cursor, table, item)
			
			target_cnx.commit()
		print("Insercion finalizada")

	elif table == STUDENT_PROFESSION_FACULTY:
		print("Cargando relacion...")
		items = content[ITEMS]
		for item in items:
			professionCode = item[PROFESSION]
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()
			
			studentCode = item[STUDENT]

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

	elif table == TEACHER:
		print("DOCENTE:::::::::::::::::::ACTUALIZACION:::::::::::::::::::::::::::::::::")
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			scaleCode = item[SCALE]
			target_cursor.execute(scaleQuery.get_query_code, [scaleCode])
			idScale = target_cursor.fetchone()
			print("escalafon: {}".format(idScale))

			gradeCode = item[GRADE]
			target_cursor.execute(gradeQuery.get_query_code, [gradeCode])
			idGrade = target_cursor.fetchone()
			print("grado: {}".format(idGrade))

			teacher = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[EMAIL_ATTRIBUTE],
				item[WORK_AREA_ATTRIBUTE]
			]
			target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idTeacherExits = target_cursor.fetchone()
			if idTeacherExits is not None:
				teacher.append(idTeacherExits[0])
				target_cursor.execute(teacherQuery.update_query, teacher)
				target_cnx.commit()
				target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[IDENTIFICATION_CARD]])
				idFact = target_cursor.fetchone()
				if idFact is not None:
					target_cursor.execute(dedent("""\
						UPDATE fact_docente_facultad
						SET id_docente=%s, id_sexo=%s, id_nacionalidad=%s, id_escalafon=%s, id_grado=%s
						WHERE id=%s"""), [idTeacherExits[0], idSex[0], idNationality[0], idScale[0], idGrade[0], idFact[0]])
					target_cnx.commit()
				else:
					print("No existe el registro")
			else:
				target_cursor.execute(teacherQuery.load_query, teacher)
				target_cnx.commit()

				target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
				idTeacher = target_cursor.fetchone()
				target_cursor.execute(dedent("""\
				INSERT INTO FACT_DOCENTE_FACULTAD 
					(id_docente, id_sexo, id_nacionalidad, id_escalafon, id_grado)
				VALUES (%s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idGrade[0]])
				target_cnx.commit()

		print("ACTUALIZACION DOCENTE FINALIZADA")

	elif table == SCALE:
		print("{}".format(table))
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(scaleQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			scale = target_cursor.fetchone()
			if scale is not None:
				update(target_cursor, table, item, {"id": scale[0]})
			else: 
				insert(target_cursor, table, item)
			target_cnx.commit()	
		print("Insercion finalizada")

	elif table == PUBLICATION:
		print("{}".format(table))
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(publicationQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			publicacion = target_cursor.fetchone()
			if publication is not None:
				update(target_cursor, table, item, {"id": publication[0]})
			else: 
				insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")
	elif table == TEACHER_PUBLICATION:
		print("{}".format(table))
		items = content[ITEMS]
		for item in items:
			publicationCode = item[PUBLICATION]
			target_cursor.execute(publicationQuery.get_query_code, [publicationCode])
			idPublication = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()
			
			teacherCode = item[TEACHER]
			target_cursor.execute(teacherQuery.get_query_code, [teacherCode])
			idTeacher = target_cursor.fetchone()

			# pasar dos parametros
			target_cursor.execute(teacherPublicationRelationship.get_query_code, [teacherCode, publicationCode])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				target_cursor.execute(dedent("""\
				UPDATE fact_docente_publicacion
				SET id_docente=%s, id_facultad=%s, id_publicacion=%s, cantidad_citas=%s
				WHERE id=%s;"""), [idTeacher[0], idFaculty[0], idPublication[0], item[CITE_ATTRIBUTE], idFact[0]])
				target_cnx.commit()
				print("Registro actualizado")
			else:
				print("Registro no existe")
		print("ACTUALIZACION finalizada")
	elif table == TEACHER_FACULTY:
		items = content[ITEMS]
		for item in items:
			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()
			
			teacherCode = item[TEACHER]
			target_cursor.execute(teacherFacultyRelationship.get_query_code, [teacherCode])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				target_cursor.execute(dedent("""\
				UPDATE fact_docente_facultad
				SET id_facultad=%s
				WHERE id=%s;"""), [idFaculty[0], idFact[0]])
				target_cnx.commit()
				print("Registro actualizado")
			else:
				print("Registro no existe")
		print("Actualizacion finalizada")

	target_cursor.close()


def insertTableStatic(target_cnx):
	target_cursor = target_cnx.cursor()
	male = MALE
	female = FEMALE
	sexParams = [(male,), (female,)]
	target_cursor.execute(sexQuery.get_verify, [male, female])
	sexList = target_cursor.fetchall()
	print(sexList)
	if len(sexList) != 2:
		target_cursor.executemany(sexQuery.load_query, sexParams)
		target_cnx.commit()
	
	national = NATIONAL
	international = INTERNACIONAL
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