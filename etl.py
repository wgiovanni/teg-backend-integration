# modulos python
from flask_restful import abort
import psycopg2
import mysql.connector
from pymysql import DatabaseError
from datetime import datetime
from textwrap import dedent
import simplejson as json
import requests
from common.BD import BD
from db_credentials import datawarehouse_db_config
from sql_queries import systemParameter, nationalityQuery, sexQuery, statusQuery, disabilityQuery, ethnicGroupQuery, studentQuery, typeStudentQuery, teacherQuery, professionQuery, facultyQuery 
from sql_queries import publicationQuery, scaleQuery, studentRelationship, gradeQuery, teacherFacultyRelationship, teacherPublicationRelationship
from sql_queries import graduateQuery, studiosUcQuery, certificationQuery, coursesQuery, educationQuery, educationQuery, patentsQuery
from sql_queries import jobsQuery, volunteeringQuery, graduateJobsRelationship, graduatePatentsRelationship, graduateCertificationRelationship, graduateStudiosUcRelationship 
from sql_queries import graduateCoursesRelationship, graduateEducationRelationship, graduateVolunteeringRelationship, typeTeacherQuery, projectQuery
from sql_queries import otherStudioQuery, titleQuery, prizeQuery, yearQuery
from constants import LOAD_INITIAL_UPDATE, ENDPOINT_LOAD_STUDENTS, ENDPOINT_LOAD_TEACHERS, ENDPOINT_LOAD_GRADUATES, DATE_UPDATE, CONTENT_TYPE
from constants import DIMENSION, FACT, ITEMS, DATE_UPDATE_STUDENS, DATE_UPDATE_TEACHERS, DATE_UPDATE_GRADUATE, LOG_ACTIVITY_MICROSERVICES
from constants import STUDENT, PROFESSION, FACULTY, STUDENT_PROFESSION_FACULTY, TEACHER, SCALE, GRADE, PUBLICATION, TEACHER_PUBLICATION, TEACHER_FACULTY, GRADUATE, STUDIOS_UC
from constants import NACIONALITY_ATTRIBUTE, SEX_ATTRIBUTE, IDENTIFICATION_CARD, FIRST_NAME_ATRIBUTE, LAST_NAME_ATRIBUTE, BIRTH_DATE_ATTRIBUTE, PHONE_ONE_ATTRIBUTE, PHONE_TWO_ATTRIBUTE, EMAIL_ATTRIBUTE, STATE_PROVENANCE_ATTRIBUTE, WORK_AREA_ATTRIBUTE, CITE_ATTRIBUTE, USER_NAME_ATTRIBUTE
from constants import MALE, FEMALE, NATIONAL, INTERNACIONAL, STATUS_ACTIVE, STATUS_INACTIVE, ETNIA_FALSE, ETNIA_TRUE, LIST_SCALE
from constants import DISABILITY_FALSE, DISABILITY_TRUE, UNDERGRADUATE, POSTGRADUATE, FACULTIES, TYPE_TEACHER
# variables
from variables import datawarehouse_name

def etl_process_students():
	print("ETL estudiantes\n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [DATE_UPDATE])
	systemParameterDate = target_cursor.fetchone()
	dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			print(systemParameterDate[4])
			data = requestCargaInitialStudents(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateStudens(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			data = requestCargaInitialStudents(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			#insercion
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateStudens(target_cnx, table, content)
		
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cursor.execute(systemParameter.update_query, ["0", row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha global")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")

def etl_process_teachers():
	print("ETL docentes\n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [DATE_UPDATE])
	systemParameterDate = target_cursor.fetchone()
	dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			data = requestCargaInitialTeachers(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateTeachers(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			data = requestCargaInitialTeachers(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			#insercion
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateTeachers(target_cnx, table, content)
		
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cursor.execute(systemParameter.update_query, ["0", row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha global")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")


def etl_process_graduates():
	print("ETL egresados\n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [DATE_UPDATE])
	systemParameterDate = target_cursor.fetchone()
	dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			data = requestCargaInitialGraduate(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateGraduate(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			data = requestCargaInitialGraduate(target_cnx)
			keyList= data.keys()
			keyList = sorted(keyList)
			#insercion
			for key in keyList:
				if dimension in key:
					table = key[len(dimension):]
				elif hechos in key:
					table = key[len(hechos):]
				content = data[key]
				distributionCargaInitialUpdateGraduate(target_cnx, table, content)
		
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cursor.execute(systemParameter.update_query, ["0", row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha global")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")


def requestCargaInitialStudents(target_cnx):
	
	headers = CONTENT_TYPE
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	path = endPointStudent[4]
	result = {}
	try:
		r = requests.get(path, headers=headers)
		if r.status_code == requests.codes.ok:
			result = json.loads(r.text)
		buildMessageLog(target_cursor, "Conexión satisfactoria con api de estudiantes", '', path, '')
	except requests.exceptions.HTTPError as errh:
		# print ("Http Error:",errh)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de estudiantes", errh, path, "Error Http")
	except requests.exceptions.ConnectionError as errc:
		# print ("Error Connecting:",errc)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de estudiantes", errc, path, "Error de conexión")
	except requests.exceptions.Timeout as errt:
		# print ("Timeout Error:",errt)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de estudiantes", errt, path, "Error, se acabó el tiempo")
	except requests.exceptions.RequestException as err:
		# print ("OOps: Something Else",err)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de estudiantes", err, path, "Otro error")

	return result
	
def requestCargaInitialTeachers(target_cnx):
	
	headers = CONTENT_TYPE
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	path = endPointTeacher[4]
	result = {}
	try:
		r = requests.get(path, headers=headers)
		if r.status_code == requests.codes.ok:
			result = json.loads(r.text)
		buildMessageLog(target_cursor, "Conexión satisfactoria con api de docentes", '', path, '')
	except requests.exceptions.HTTPError as errh:
		# print ("Http Error:",errh)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de docentes", errh, path, "Error Http")
	except requests.exceptions.ConnectionError as errc:
		# print ("Error Connecting:",errc)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de docentes", errc, path, "Error de conexión")
	except requests.exceptions.Timeout as errt:
		# print ("Timeout Error:",errt)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de docentes", errt, path, "Error, se acabó el tiempo")
	except requests.exceptions.RequestException as err:
		# print ("OOps: Something Else",err)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de docentes", err, path, "Otro error")

	return result

def requestCargaInitialGraduate(target_cnx):
	
	headers = CONTENT_TYPE
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	endPointGraduated = target_cursor.fetchone()
	path = endPointGraduated[4]
	result = {}
	try:
		r = requests.get(path, headers=headers)
		if r.status_code == requests.codes.ok:
			result = json.loads(r.text)
		buildMessageLog(target_cursor, "Conexión satisfactoria con api de egresados", '', path, '')
	except requests.exceptions.HTTPError as errh:
		# print ("Http Error:",errh)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de egresados", errh, path, "Error Http")
	except requests.exceptions.ConnectionError as errc:
		# print ("Error Connecting:",errc)
		buildMessageErrorRequest(target_cursor,"Solicitud para la api de egresados", errc, path, "Error de conexión")
	except requests.exceptions.Timeout as errt:
		# print ("Timeout Error:",errt)
		buildMessageErrorRequest(target_cursor,"Solicitud para la api de egresados", errt, path, "Error, se acabó el tiempo")
	except requests.exceptions.RequestException as err:
		# print ("OOps: Something Else",err)
		buildMessageErrorRequest(target_cursor, "Solicitud para la api de egresados", err, path, "Otro error")

	return result

def buildMessageErrorRequest(target_cursor, activity: str, message: str, path: str, typeError: str):
	message = splitError(str(message))
	entity = {
		"activity": str(activity),
		"message": str(message),
		"endpoint": path,
		"type": str(typeError) 
	}
	insertError(target_cursor, LOG_ACTIVITY_MICROSERVICES, entity)	

def buildMessageLog(target_cursor, activity: str, message: str, path: str, typeError: str):
	entity = {
		"activity": str(activity),
		"message": str(message),
		"endpoint": path,
		"type": str(typeError) 
	}
	insertError(target_cursor, LOG_ACTIVITY_MICROSERVICES, entity)

# def buildMessageLog(target_cursor, activity: str, message: str, path: str, typeError: str):
# 	entity = {
# 		"activity": str(activity),
# 		"message": str(message),
# 		"endpoint": path,
# 		"type": str(typeError) 
# 	}
# 	insertError(target_cursor, LOG_ACTIVITY_MICROSERVICES, entity)

def splitError(message: str):
	message = message.split('] ')
	message = message[-1].split("'")
	message = message[0]
	return message


def distributionCargaInitialUpdateStudens(target_cnx, table: str, content: dict):
	
	target_cursor = target_cnx.cursor(buffered=True)

	if table == STUDENT:
		items = content[ITEMS]
		#print(items)
		print("Cargando estudiantes...")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			# nacionalidad
			print(item)
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v" or nationalityCode == "VENEZUELA":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			else:
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			# print("nacionalidad: {}".format(idNationality))

			# sexo
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			# print("sexo: {}".format(idSex))

			# status
			statusCode = item['estatus']
			if statusCode == 0:
				statusCode = STATUS_ACTIVE
			elif statusCode == 1:
				statusCode = STATUS_INACTIVE
			target_cursor.execute(statusQuery.get_query_code, [statusCode])
			idStatus = target_cursor.fetchone()
			# print("status: {}".format(idStatus))

			# discapacidad
			disabilityCode = item['discapacidad']
			if disabilityCode == DISABILITY_FALSE:
				disabilityCode = DISABILITY_FALSE
			else:
				disabilityCode = DISABILITY_TRUE
			# print(disabilityCode)
			target_cursor.execute(disabilityQuery.get_query_code, [disabilityCode])
			idDisability = target_cursor.fetchone()
			# print("discapacidad: {}".format(idDisability[0]))

			# etnia
			ethnicGroupCode = item['etnia']
			if ethnicGroupCode == ETNIA_FALSE:
				ethnicGroupCode = ETNIA_FALSE
			else:
				ethnicGroupCode = ETNIA_TRUE
			target_cursor.execute(ethnicGroupQuery.get_query_code, [ethnicGroupCode])
			idEthnicGroup = target_cursor.fetchone()
			# print("etnia: {}".format(idEthnicGroup))

			# tipo de estudiante
			typeStudentCode = item['tipo_estudio']
			if typeStudentCode == "0":
				typeStudentCode = UNDERGRADUATE
			elif typeStudentCode == "1":
				typeStudentCode = POSTGRADUATE
			target_cursor.execute(typeStudentQuery.get_query_code, [typeStudentCode])
			idTypeStudent = target_cursor.fetchone()
			# print("tipo: {}".format(idTypeStudent))

			# año
			yearCode = item['anno_entrada']
			target_cursor.execute(yearQuery.get_query_code, [yearCode])
			idYear = target_cursor.fetchone()
			# print("ano: {}".format(idYear))

			# carrera
			professionCode = item[PROFESSION]
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			# facultad
			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()

			student = [
				item[IDENTIFICATION_CARD],  
				item["primer_nombre"], 
				item["primer_apellido"], 
				item[BIRTH_DATE_ATTRIBUTE],
				item[PHONE_ONE_ATTRIBUTE], 
				item[PHONE_TWO_ATTRIBUTE],
				item["email"],
				item[STATE_PROVENANCE_ATTRIBUTE]
			]

			target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idStudentExist = target_cursor.fetchone()

			if idStudentExist is not None:
				# actualizar estudiante
				try:
					student.append(idStudentExist[0])
					target_cursor.execute(studentQuery.update_query, student)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
					buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_estudiante', 'Error de base de datos')
			else:
				# insertar estudiante
				try:
					target_cursor.execute(studentQuery.load_query, student)

					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_estudiante', 'Error de base de datos')

			target_cursor.execute(studentRelationship.get_query_code,[item[IDENTIFICATION_CARD]])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				try:
					target_cursor.execute(dedent("""\
					UPDATE fact_estudiante_facultad
					SET id_estudiante=%s, id_genero=%s, id_nacionalidad=%s, id_status=%s, id_discapacidad=%s, id_etnia=%s, id_tipo_estudiante=%s, id_tiempo=%s, id_facultad=%s, id_carrera=%s
					WHERE id = %s"""), [idStudentExist[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0], idYear[0], idFaculty[0], idProfession[0], idFact[0]])
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					print("Actualizado")

				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
					buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla fact_estudiante_facultad', 'Error de base de datos')
			else:
				# insercion
				print("INSERCION")
				try:			
					target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
					idStudent = target_cursor.fetchone()
					target_cursor.execute(dedent("""\
					INSERT INTO FACT_ESTUDIANTE_FACULTAD 
						(id_estudiante, id_genero, id_nacionalidad, id_status, id_discapacidad, id_etnia, id_tipo_estudiante, id_tiempo, id_facultad, id_carrera)
					VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0], idYear[0], idFaculty[0], idProfession[0]])
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
					
					print("Insertado")
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla fact_estudiante_facultad', 'Error de base de datos')
			target_cnx.commit()
	
	target_cursor.close()

def distributionCargaInitialUpdateTeachers(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor(buffered=True)
	if table == PROFESSION:
		print("Cargando carrera...")
		items = content[ITEMS]
		for item in items:
			#print(item)
			target_cursor.execute(professionQuery.get_query_code, [item["nombre"]])
			row = target_cursor.fetchone()
			#print(row)
			item = {
				"codigo": item['nombre'],
				"nombre": item['nombre']
			}
			try:
				if row is not None:
					#print("entro")
					update(target_cursor, table, item, {"id": row[0]})
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
				else:
					#print("entro2")
					#target_cursor.execute("INSERT INTO DIM_CARRERA (codigo, nombre) VALUES (%s,%s) ON ON DUPLICATE KEY UPDATE codigo=codigo, nombre=nombre", [item["nombre"], i]) 
					insert(target_cursor, table, item)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_STUDENS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
				target_cnx.commit()
			except mysql.connector.Error as e:
				print("Roolback")
				buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_carrera', 'Error de base de datos')
			
		print("Insercion finalizada")

	elif table == TEACHER:
		print("DOCENTE")
		items = content[ITEMS]
		#print(items)
		#print("\n")
		for item in items:
			# nacionalidad
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print("nacionalidad: {}".format(idNationality))

			# sexo
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			#escalafon
			scaleCode = item[SCALE]
			target_cursor.execute(scaleQuery.get_query_code, [scaleCode])
			idScale = target_cursor.fetchone()
			print("escalafon: {}".format(idScale))

			#tipo de docente
			typeTeacherCode = item['tipo']
			target_cursor.execute(typeTeacherQuery.get_query_code, [typeTeacherCode])
			idTypeTeacher = target_cursor.fetchone()

			# facultad
			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()


			teacher = [
				item[IDENTIFICATION_CARD],  
				item['primernombre'],
				item['segundonombre'], 
				item['primerapellido'],
				item['segundoapellido'], 
				item[EMAIL_ATTRIBUTE],
				item[WORK_AREA_ATTRIBUTE]
			]

			target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idTeacherExits = target_cursor.fetchone()
			if idTeacherExits is not None:
				try:
					teacher.append(idTeacherExits[0])
					target_cursor.execute(teacherQuery.update_query, teacher)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
					target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[IDENTIFICATION_CARD]])
					idFact = target_cursor.fetchone()
					if idFact is not None:
							target_cursor.execute(dedent("""\
								UPDATE fact_docente_facultad
								SET id_docente=%s, id_genero=%s, id_nacionalidad=%s, id_escalafon=%s, id_tipo_docente=%s, id_facultad=%s
								WHERE id=%s"""), [idTeacherExits[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0], idFact[0]])
							# actualizar fecha
							target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
							systemParameterDate = target_cursor.fetchone()
							dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

							target_cnx.commit()

							print("Actualizado")
					else:
						print("No existe el registro")
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_docentes', 'Error de base de datos')

			else:
				try:
					target_cursor.execute(teacherQuery.load_query, teacher)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
					target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
					idTeacher = target_cursor.fetchone()
					target_cursor.execute(dedent("""\
					INSERT INTO FACT_DOCENTE_FACULTAD 
						(id_docente, id_genero, id_nacionalidad, id_escalafon, id_tipo_docente, id_facultad)
					VALUES (%s, %s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0]])
					
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
					print("Insertado")
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_docentes', 'Error de base de datos')

		print("ACTUALIZACION DOCENTE FINALIZADA")

	elif table == PUBLICATION:
		items = content[ITEMS]
		print("INSERCION PUBLICACION")
		for item in items:
			item = {
				"codigo": item['codigo'],
				"titulo_publicacion": item['titulopublicacion'],
				"url_citacion": item['urlcitacion'],
				"url_publicacion": item['urlpublicacion'],
			}
			target_cursor.execute(publicationQuery.get_query_code, [item['codigo']])
			publication = target_cursor.fetchone()
			if publication is None:
				try:
					insert(target_cursor, "publicacion", item)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_publicacion', 'Error de base de datos')
					
			else:
				try:
					update(target_cursor, "publicacion", item, {'id':publication[0]})
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_publicacion', 'Error de base de datos')
		print("Insercion finalizada")

	elif table == TEACHER_PUBLICATION:
		items = content[ITEMS]
		if items != []:
			target_cursor.execute("DELETE FROM fact_docente_publicacion")
			target_cnx.commit()
		for item in items:
			#print(item)
			teacherCode = item['docente']
			numberCites = item['numerocitaciones']
			publicationCode = item['publicacion']
			target_cursor.execute(dedent("""\
			SELECT d.id as idTeacher, f.id as idFaculty 
			FROM fact_docente_facultad AS fact 
			INNER JOIN dim_docente AS d 
			ON (fact.id_docente = d.id)
			INNER JOIN dim_facultad AS f 
			ON (fact.id_facultad = f.id) 
			WHERE d.cedula = %s"""), [teacherCode])
			ids = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_publicacion
			WHERE codigo = %s"""), [publicationCode])
			idPublication = target_cursor.fetchone()

			if ids[0] is not None and idPublication[0] is not None and ids[1] is not None:
				try:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_publicacion
					(id_docente, id_facultad, id_publicacion, cantidad_citas)
					VALUES (%s, %s, %s, %s)"""), [ids[0], ids[1], idPublication[0], numberCites])
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla fact_docente_publicacion', 'Error de base de datos')
			else: 
				print("Error")
			print("Insercion finalizada")
		# actualizar fecha
		target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
		systemParameterDate = target_cursor.fetchone()
		dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

		target_cnx.commit()
	
	elif table == "titulo":
		items = content[ITEMS]
		print("INSERCION TITULO")
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre": item['nomtitulo']
			}
			target_cursor.execute(titleQuery.get_query_code, [item['codigo']])
			title = target_cursor.fetchone()
			if title is None:
				try:
					insert(target_cursor, "titulo", item)
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_titulo', 'Error de base de datos')
			else:
				try:
					update(target_cursor, "titulo", item, {'id': title[0]})
					# actualizar fecha
					target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
					systemParameterDate = target_cursor.fetchone()
					dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_titulo', 'Error de base de datos')
		print("Insercion finalizada")

	elif table == "docente-titulo":
		items = content[ITEMS]

		if items != []:
			target_cursor.execute("DELETE FROM fact_docente_titulo")
			target_cnx.commit()
		for item in items:
			print(item)
			teacherCode = item['docente']
			levelCode = item['nivel']
			titleCode = item['titulo']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_nivel
			WHERE codigo = %s"""), [levelCode])
			idLevel = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_titulo
			WHERE codigo = %s"""), [titleCode])
			idTitle = target_cursor.fetchone()

			if idTeacher[0] is not None and idLevel[0] is not None and idTitle[0] is not None:
				try:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_titulo
					(id_docente, id_titulo, id_nivel)
					VALUES (%s, %s, %s)"""), [idTeacher[0], idTitle[0], idLevel[0]])
				except mysql.connector.Error as e:
					print("Roolback")
					buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla fact_docente_titulo', 'Error de base de datos')
			else:
				print("Error")
			print("Insercion finalizada")
		# actualizar fecha
		target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_TEACHERS])
		systemParameterDate = target_cursor.fetchone()
		dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cnx.commit()

	target_cursor.close()

def distributionCargaInitialUpdateGraduate(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor(buffered=True)
	if table == GRADUATE:
		# print("Entro")
		items = content[ITEMS]
		for item in items:
			if validateJson(item):
				graduateCode = item['codigo']
				target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
				idGraduate = target_cursor.fetchone()
				# print("codigo")
				# print(idGraduate)
				item = {
					"cedula": item['identificacion'],
					"nombre": item['primernombre'], 
					"apellido": item['primerapellido'],
					"correo": item['email'],
					"telefono": item['telefono'],
					"codigo": item['codigo']				
				}
				if idGraduate is None:
					print("insertar")
					try:
						insert(target_cursor, table, item)
						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_egresado', 'Error de base de datos')
				else:
					print("actualizar")
					try: 
						update(target_cursor, table, item, {"id": idGraduate[0]})
						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_egresado', 'Error de base de datos')
			else: 
				print("Objeto con valores nulos o vacios")
	
	elif table == STUDIOS_UC:
		print("ESTUDIOSUC")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
				facultyCode = item['facultad']
				graduateCode = item['egresado']
				item = {
					"titulo": item['titulo'],
					"anho_grado": item['anhogrado'],
					"url_certificacion": item['urlcertificacion'],
					"codigo": item['codigo']
				}
				target_cursor.execute(studiosUcQuery.get_query_code, [item['codigo']])
				studiosUc = target_cursor.fetchone()
				if studiosUc is None:
					print("INSERTADO")
					try:
						insert(target_cursor, table, item)
						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_estudiosuc', 'Error de base de datos')
						
				else:
					print("ACTUALIZADO")
					try: 
						update(target_cursor, table, item, {"id": studiosUc[0]})
						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_estudiosuc', 'Error de base de datos')
				
				target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
				idFaculty = target_cursor.fetchone()

				target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
				idGraduate = target_cursor.fetchone()

				studiosUcCode = item['codigo']
				target_cursor.execute(studiosUcQuery.get_query_code, [studiosUcCode])
				idStudiosUc = target_cursor.fetchone()
				idYear = None
				
				if idStudiosUc is not None:
					anhoCode = idStudiosUc[1].strftime('%Y-%m-%d').split("-")
					target_cursor.execute(yearQuery.get_query_code, [anhoCode[0]])
					idYear = target_cursor.fetchone()

				target_cursor.execute(graduateStudiosUcRelationship.get_query_code, [studiosUcCode])
				idFact = target_cursor.fetchone()

				if idStudiosUc is not None and idFaculty is not None and idYear is not None and idGraduate is not None:
					if idFact is not None:
						print("ACTUALIZADO")
						try:
							target_cursor.execute(dedent("""\
							UPDATE fact_egresado_estudiosuc
							SET id_egresado=%s, id_estudiosuc=%s, id_facultad=%s, id_tiempo=%s 
							WHERE id=%s;"""), [idGraduate[0], idStudiosUc[0], idFaculty[0], idYear[0], idFact[0]])
							# actualizar fecha
							target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
							systemParameterDate = target_cursor.fetchone()
							dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

							target_cnx.commit()
							print("Registro actualizado")
						except mysql.connector.Error as e:
							print("Roolback {}".format(e))
							buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla fact_egresado_estudiosuc', 'Error de base de datos')
					else:
						print("INSERTADO")
						try:
							target_cursor.execute(dedent("""\
							INSERT INTO fact_egresado_estudiosuc 
							(id_egresado, id_estudiosuc, id_facultad, id_tiempo)
							VALUES (%s, %s, %s, %s)"""), [idGraduate[0], idStudiosUc[0], idFaculty[0], idYear[0]])

							# actualizar fecha
							target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
							systemParameterDate = target_cursor.fetchone()
							dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

							target_cnx.commit()
							print("Registro insertado")
						except mysql.connector.Error as e:
							print("Roolback {}".format(e))
							buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla fact_egresado_estudiosuc', 'Error de base de datos')
			else:
				print("Objeto con valores nulos o vacios")

	elif table == "trabajos":
		print("Trabajos\n\n")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
				graduateCode = item['egresado']
				jobCode = item['codigo']
				item = {
					"nombre_empresa": item['nombreempresa'],
					"cargo": item['cargo'],
					"descripcion": item['descripcion'],
					"codigo": item['codigo'],
					"url": item['url'],
					"fecha": item['fecha'],
					"laborando": item['laborando']
				}
				target_cursor.execute(jobsQuery.get_query_code, [item['codigo']])
				job = target_cursor.fetchone()
				if job is None:
					print("INSERTADO")
					try:
						insert(target_cursor, table, item)

						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla dim_trabajos', 'Error de base de datos')
				else:
					print("ACTUALIZADO")
					try: 
						update(target_cursor, table, item, {"id": job[0]})

						# actualizar fecha
						target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
						systemParameterDate = target_cursor.fetchone()
						dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
						buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla dim_trabajos', 'Error de base de datos')

				target_cursor.execute(jobsQuery.get_query_code, [jobCode])
				idJob = target_cursor.fetchone() 

				target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
				idGraduate = target_cursor.fetchone()

				target_cursor.execute(graduateJobsRelationship.get_query_code, [jobCode])
				idFact = target_cursor.fetchone()

				if idJob is not None and idGraduate is not None:
					if idFact is not None:
						print("ACTUALIZADO")
						try:
							target_cursor.execute(dedent("""\
							UPDATE fact_egresado_trabajos
							SET id_egresado=%s, id_trabajo=%s 
							WHERE id=%s;"""), [idGraduate[0], idJob[0], idFact[0]])

							# actualizar fecha
							target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
							systemParameterDate = target_cursor.fetchone()
							dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

							target_cnx.commit()
							print("Registro actualizado")
						except mysql.connector.Error as e:
							print("Roolback {}".format(e))
							buildMessageLog(target_cursor, 'Actualización en base de datos', e, 'Tabla fact_egresado_trabajos', 'Error de base de datos')
					else:
						print("INSERTADO")
						try:
							target_cursor.execute(dedent("""\
							INSERT INTO fact_egresado_trabajos 
							(id_egresado, id_trabajo)
							VALUES (%s, %s)"""), [idGraduate[0], idJob[0]])

							# actualizar fecha
							target_cursor.execute(systemParameter.get_query, [DATE_UPDATE_GRADUATE])
							systemParameterDate = target_cursor.fetchone()
							dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])

							target_cnx.commit()
							print("Registro insertado")
						except mysql.connector.Error as e:
							print("Roolback {}".format(e))
							buildMessageLog(target_cursor, 'Carga en base de datos', e, 'Tabla fact_egresado_trabajos', 'Error de base de datos')
			else:
				print("Objeto con valores nulos o vacios")
	
	target_cursor.close()

def insertTableStatic(target_cnx):
	
	target_cursor = target_cnx.cursor()
	# sexo
	male = MALE
	female = FEMALE
	sexParams = [(male,), (female,)]
	target_cursor.execute(sexQuery.get_verify, [male, female])
	sexList = target_cursor.fetchall()
	print(sexList)
	if len(sexList) != 2:
		target_cursor.executemany(sexQuery.load_query, sexParams)
		target_cnx.commit()
	#nacionalidad
	national = NATIONAL
	international = INTERNACIONAL
	nationalityParams = [(national,), (international,)]
	target_cursor.execute(nationalityQuery.get_verify, [national, international])
	nationalityList = target_cursor.fetchall()
	print(nationalityList)
	if len(nationalityList) != 2:
		target_cursor.executemany(nationalityQuery.load_query, nationalityParams)
		target_cnx.commit()

	# status del estudiante
	active = STATUS_ACTIVE
	inactive = STATUS_INACTIVE
	statusParams = [(active,), (inactive,)]
	target_cursor.execute(statusQuery.get_verify, [active, inactive])
	statusList = target_cursor.fetchall()
	if len(statusList) != 2:
		target_cursor.executemany(statusQuery.load_query, statusParams)
		target_cnx.commit()
	
	# etnia del estudiante
	etniaFalse = ETNIA_FALSE
	etniaTrue = ETNIA_TRUE
	etniaGroupParams = [(etniaTrue,), (etniaFalse,)]
	target_cursor.execute(ethnicGroupQuery.get_verify, [etniaTrue, etniaFalse])
	etniaGroupList = target_cursor.fetchall()
	if len(etniaGroupList) != 2:
		target_cursor.executemany(ethnicGroupQuery.load_query, etniaGroupParams)
		target_cnx.commit()

	# discapacidad del estudiante
	disabilityFalse = DISABILITY_FALSE
	disabilityTrue = DISABILITY_TRUE
	disabilityParams = [(disabilityTrue,), (disabilityFalse,)]
	target_cursor.execute(disabilityQuery.get_verify, [disabilityTrue, disabilityFalse])
	disabilityList = target_cursor.fetchall()
	if len(disabilityList) != 2:
		target_cursor.executemany(disabilityQuery.load_query, disabilityParams)
		target_cnx.commit()

	# tipo de estudiante
	undergraduate = UNDERGRADUATE
	postgraduate = POSTGRADUATE
	typeStudentParams = [(undergraduate,), (postgraduate,)]
	target_cursor.execute(typeStudentQuery.get_verify,[undergraduate, postgraduate])
	typeList = target_cursor.fetchall()
	if len(typeList) != 2:
		target_cursor.execute(typeStudentQuery.load_query,typeStudentParams)
		target_cnx.commit()

	# facultades
	faculties = FACULTIES
	for f in faculties:
		target_cursor.execute(facultyQuery.get_query_code, [f["codigo"]])
		faculty = target_cursor.fetchone()
		table = "facultad"
		if faculty is None:
			insert(target_cursor, table, f)
			target_cnx.commit()
			print("Inserto facultad")
		else: 
			print("Ya existe {}".format(faculty[0]))

	# escalafon 
	list_scale = LIST_SCALE
	for s in list_scale:
		target_cursor.execute(scaleQuery.get_query_code, [s["nombre"]])
		scale = target_cursor.fetchone()
		table = "escalafon"
		if scale is None:
			insert(target_cursor, table, s)
			target_cnx.commit()
			print("Inserto escalafon")
		else:
			print("Ya existe {}".format(scale[0]))

	listTypeTeacher = TYPE_TEACHER
	for s in listTypeTeacher:
		target_cursor.execute(typeTeacherQuery.get_query_code, [s["codigo"]])
		typeTeacher = target_cursor.fetchone()
		table = "tipo_docente"
		if scale is None:
			insert(target_cursor, table, s)
			target_cnx.commit()
			print("Inserto tipo docente")
		else:
			print("Ya existe {}".format(typeTeacher[0]))


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

	sql = f"update dim_{table} set "
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

def validateJson(items: dict):
	validate = True
	for i in items:
		if items[i] == None or items[i] == "" or items[i] == "None":
			validate = False
	
	return validate

def insertError(cursor, table: str, datos: dict=None, columns=None, values: list=None):
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

