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
from constants import DIMENSION, FACT, ITEMS
from constants import STUDENT, PROFESSION, FACULTY, STUDENT_PROFESSION_FACULTY, TEACHER, SCALE, GRADE, PUBLICATION, TEACHER_PUBLICATION, TEACHER_FACULTY, GRADUATE, STUDIOS_UC
from constants import NACIONALITY_ATTRIBUTE, SEX_ATTRIBUTE, IDENTIFICATION_CARD, FIRST_NAME_ATRIBUTE, LAST_NAME_ATRIBUTE, BIRTH_DATE_ATTRIBUTE, PHONE_ONE_ATTRIBUTE, PHONE_TWO_ATTRIBUTE, EMAIL_ATTRIBUTE, STATE_PROVENANCE_ATTRIBUTE, WORK_AREA_ATTRIBUTE, CITE_ATTRIBUTE, USER_NAME_ATTRIBUTE
from constants import MALE, FEMALE, NATIONAL, INTERNACIONAL, STATUS_ACTIVE, STATUS_INACTIVE, ETNIA_FALSE, ETNIA_TRUE, LIST_SCALE
from constants import DISABILITY_FALSE, DISABILITY_TRUE, UNDERGRADUATE, POSTGRADUATE, FACULTIES, TYPE_TEACHER
# variables
from variables import datawarehouse_name


def etl_process():
	print("ETL \n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [DATE_UPDATE])
	systemParameterDate = target_cursor.fetchone()
	dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(row)
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			print(systemParameterDate[4])
			dataList = requestCargaInitial(target_cnx)
			
			for data in dataList:
				#print(data)
				keyList= data.keys()
				keyList = sorted(keyList)
				for key in keyList:
					#print("KEY:{}".format(key))
					if dimension in key:
						#print("Dimension")
						#picar string
						table = key[len(dimension):]
					elif hechos in key:
						#print("Hechos")
						#picar string
						table = key[len(hechos):]
					content = data[key]
					#print("\n\n")
					#print(table)
					#print(content)
					distributionCargaInitialUpdate(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			dataList = requestCargaInitial(target_cnx)
			#print(dataList)
			#print("\n\n")
			for data in dataList:
				#print(data)
				#print("\n")
				# ordenamiento: ESTO ES RELEVANTE
				keyList= data.keys()
				keyList = sorted(keyList)
				#insercion
				for key in keyList:
					#print("KEY:{}".format(key))
					if dimension in key:
						#print("Dimension")
						#picar string
						table = key[len(dimension):]
					elif hechos in key:
						#print("Hechos")
						#picar string
						table = key[len(hechos):]
					content = data[key]
					#print("\n\n")
					#print(table)
					#print(content)
					distributionCargaInitialUpdate(target_cnx, table, content)
		
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cursor.execute(systemParameter.update_query, ["0", row[0]])
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
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	endPointGraduated = target_cursor.fetchone()
	#pathList.append(endPointStudent[4])
	#pathList.append(endPointTeacher[4])
	pathList.append(endPointGraduated[4])
	print(pathList)
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			print("Path no encontrado " + path)
			continue
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		continue		

	return result
	

def requestUpdate(target_cnx, lastUpdate):
	headers = CONTENT_TYPE
	pathList = []
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	endPointGraduated = target_cursor.fetchone()
	#pathList.append(endPointStudent[4]+"/{}".format(lastUpdate))
	#pathList.append(endPointTeacher[4]+"/{}".format(lastUpdate))
	#pathList.append(endPointGraduated[4]+"{}".format(lastUpdate)) 
	print(pathList)
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			print("Path no encontrado " + path)
			continue
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		continue

	return result



def distributionCargaInitialUpdate(target_cnx, table: str, content: dict):
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

			# status
			statusCode = item['estatus']
			if statusCode == 0:
				statusCode = STATUS_ACTIVE
			elif statusCode == 1:
				statusCode = STATUS_INACTIVE
			target_cursor.execute(statusQuery.get_query_code, [statusCode])
			idStatus = target_cursor.fetchone()
			print("status: {}".format(idStatus))

			# discapacidad
			disabilityCode = item['discapacidad']
			if disabilityCode == DISABILITY_FALSE:
				disabilityCode = DISABILITY_FALSE
			else:
				disabilityCode = DISABILITY_TRUE
			print(disabilityCode)
			target_cursor.execute(disabilityQuery.get_query_code, [disabilityCode])
			idDisability = target_cursor.fetchone()
			print("discapacidad: {}".format(idDisability[0]))

			# etnia
			ethnicGroupCode = item['etnia']
			if ethnicGroupCode == ETNIA_FALSE:
				ethnicGroupCode = ETNIA_FALSE
			else:
				ethnicGroupCode = ETNIA_TRUE
			target_cursor.execute(ethnicGroupQuery.get_query_code, [ethnicGroupCode])
			idEthnicGroup = target_cursor.fetchone()
			print("etnia: {}".format(idEthnicGroup))

			# tipo de estudiante
			typeStudentCode = item['tipo_estudio']
			if typeStudentCode == "0":
				typeStudentCode = UNDERGRADUATE
			elif typeStudentCode == "1":
				typeStudentCode = POSTGRADUATE
			target_cursor.execute(typeStudentQuery.get_query_code, [typeStudentCode])
			idTypeStudent = target_cursor.fetchone()
			print("tipo: {}".format(idTypeStudent))

			# año
			yearCode = item['anno_entrada']
			target_cursor.execute(yearQuery.get_query_code, [yearCode])
			idYear = target_cursor.fetchone()
			print("ano: {}".format(idYear))

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
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
			else:
				# insertar estudiante
				try:
					target_cursor.execute(studentQuery.load_query, student)
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()

			target_cursor.execute(studentRelationship.get_query_code,[item[IDENTIFICATION_CARD]])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				try:
					target_cursor.execute(dedent("""\
					UPDATE fact_estudiante_facultad
					SET id_estudiante=%s, id_genero=%s, id_nacionalidad=%s, id_status=%s, id_discapacidad=%s, id_etnia=%s, id_tipo_estudiante=%s, id_tiempo=%s, id_facultad=%s, id_carrera=%s
					WHERE id = %s"""), [idStudentExist[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0], idYear[0], idFaculty[0], idProfession[0], idFact[0]])
					print("Actualizado")
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
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
					print("Insertado")
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
			target_cnx.commit()

	elif table == PROFESSION:
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
				else:
					#print("entro2")
					#target_cursor.execute("INSERT INTO DIM_CARRERA (codigo, nombre) VALUES (%s,%s) ON ON DUPLICATE KEY UPDATE codigo=codigo, nombre=nombre", [item["nombre"], i]) 
					insert(target_cursor, table, item)
				target_cnx.commit()
			except mysql.connector.Error as e:
				print("Roolback")
			
		print("Insercion finalizada")

	elif table == STUDENT_PROFESSION_FACULTY:
		'''
		print("Cargando Hechos Estudiante...")
		items = content[ITEMS]
		for item in items:
			print(item)
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
			print(idStudent[0])
			print(idFaculty[0])
			print(idProfession[0])
			#print(idFact[0])

			if idFact is not None:
				try:
					target_cursor.execute(dedent("""\
					UPDATE fact_estudiante_facultad
					SET id_estudiante=%s, id_facultad=%s, id_carrera=%s
					WHERE id=%s"""), [idStudent[0], idFaculty[0], idProfession[0], idFact[0]])
					target_cnx.commit()
					print("Registro actualizado")
				except mysql.connector.Error as e:
					print("error")
					target_cnx.rollback()
			else:
				print("Registro no existe")
		#target_cnx.commit()
		print("Insercion finalizada")
		'''

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
					target_cnx.commit()
					target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[IDENTIFICATION_CARD]])
					idFact = target_cursor.fetchone()
					if idFact is not None:
							target_cursor.execute(dedent("""\
								UPDATE fact_docente_facultad
								SET id_docente=%s, id_genero=%s, id_nacionalidad=%s, id_escalafon=%s, id_tipo_docente=%s, id_facultad=%s
								WHERE id=%s"""), [idTeacherExits[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0], idFact[0]])
							target_cnx.commit()
							print("Actualizado")
					else:
						print("No existe el registro")
				except mysql.connector.Error as e:
					print("Roolback")

			else:
				try:
					target_cursor.execute(teacherQuery.load_query, teacher)
					target_cnx.commit()
					target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
					idTeacher = target_cursor.fetchone()
					target_cursor.execute(dedent("""\
					INSERT INTO FACT_DOCENTE_FACULTAD 
						(id_docente, id_genero, id_nacionalidad, id_escalafon, id_tipo_docente, id_facultad)
					VALUES (%s, %s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0]])
					target_cnx.commit()
					print("Insertado")
				except mysql.connector.Error as e:
					print("Roolback")

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
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
			else:
				try:
					update(target_cursor, "publicacion", item, {'id':publication[0]})
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
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
			else: 
				print("Error")
			print("Insercion finalizada")
		target_cnx.commit()

	elif table == "proyecto":
		items = content[ITEMS]
		print("INSERCION PROYECTO")
		for item in items:
			item = {
				"codigo": item['codigo'],
				"titulo": item['titulo']
			}
			target_cursor.execute(projectQuery.get_query_code, [item['codigo']])
			project = target_cursor.fetchone()
			if project is None:
				try:
					insert(target_cursor, "proyecto", item)
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
			else:
				try:
					update(target_cursor, "proyecto", item, {'id': project[0]})
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
		print("Insercion finalizada")

	elif table == "docente-proyecto":
		items = content[ITEMS]
		if items != []:
			target_cursor.execute("DELETE FROM fact_docente_proyecto")
			target_cnx.commit()
		for item in items:
			teacherCode = item['docente']
			projectCode = item['proyecto']
			target_cursor.execute(teacherQuery.get_query_code, [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_proyecto
			WHERE codigo = %s"""), [projectCode])
			idProyect = target_cursor.fetchone()

			if idTeacher[0] is not None and idProyect[0] is not None:
				try:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_proyecto
					(id_docente, id_proyecto)
					VALUES (%s, %s)"""), [idTeacher[0], idProyect[0]])
				except mysql.connector.Error as e:
					print("Roolback")
			else: 
				print("Error")
			print("Insercion finalizada")
		target_cnx.commit()
		

	elif table == "otroestudio":
		items = content[ITEMS]
		print("INSERCION OTRO ESTUDIO")
		'''
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre_titulo": item['nomtitulo']
			}
			target_cursor.execute(otherStudioQuery.get_query_code, [item['codigo']])
			project = target_cursor.fetchone()
			if project is None:
				insert(target_cursor, "otroestudio", item)
				target_cnx.commit()
			else:
				print("Ya existe {}".format(item['codigo']))
		print("Insercion finalizada")
		'''

	elif table == "docente-otro-estudio":
		items = content[ITEMS]
		'''
		if items != []:
			target_cursor.execute("DELETE FROM fact_docente_otroestudio")
			target_cnx.commit()
		for item in items:
			teacherCode = item['docente']
			otherStudioCode = item['codigo']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_otroestudio
			WHERE codigo = %s"""), [otherStudioCode])
			idOtherStudio = target_cursor.fetchone()

			if idTeacher[0] is not None and idOtherStudio[0] is not None:
				target_cursor.execute(dedent("""\
				INSERT INTO fact_docente_otroestudio
				(id_docente, id_otroestudio)
				VALUES (%s, %s)"""), [idTeacher[0], idOtherStudio[0]])
			else:
				print("Error")
			print("Insercion finalizada")
		'''
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
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
			else:
				try:
					update(target_cursor, "titulo", item, {'id': title[0]})
					target_cnx.commit()
				except mysql.connector.Error as e:
					print("Roolback")
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
			else:
				print("Error")
			print("Insercion finalizada")
		target_cnx.commit()

	elif table == "premio":
		items = content[ITEMS]
		print("INSERCION PREMIO")
		for item in items:
			target_cursor.execute(prizeQuery.get_query_code, [item['codigo']])
			prize = target_cursor.fetchone()
			if prize is None:
				try:
					insert(target_cursor, "premio", item)
				except mysql.connector.Error as e:
					print("Roolback")
			else:
				try:
					update(target_cursor, "premio", item, {'id': prize[0]})
				except mysql.connector.Error as e:
					print("Roolback")
		target_cnx.commit()
		print("Insercion finalizada")

	elif table == "docente-premio":
		items = content[ITEMS]
		if items != []:
			target_cursor.execute("DELETE FROM fact_docente_premio")
			target_cnx.commit()
		for item in items:
			teacherCode = item['docente']
			target_cursor.execute(teacherQuery.get_query_code, [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_premio
			WHERE codigo = %s"""), [item['premio']])
			idPrize = target_cursor.fetchone()

			if idTeacher[0] is not None and idPrize[0] is not None:
				try:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_premio
					(id_docente, id_premio)
					VALUES (%s, %s)"""), [idTeacher[0], idPrize[0]])
				except mysql.connector.Error as e:
					print("Roolback")
			else:
				print("Error")
			print("Insercion finalizada")
		target_cnx.commit()

	elif table == GRADUATE:
		print("Entro")
		items = content[ITEMS]
		for item in items:
			if validateJson(item):
				graduateCode = item['identificacion']
				target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
				idGraduate = target_cursor.fetchone()
				item = {
					"cedula": item['identificacion'],
					"primer_nombre": item['primernombre'], 
					"segundo_nombre": item['segundonombre'], 
					"primer_apellido": item['primerapellido'],
					"segundo_apellido": item['segundoapellido'],
					"correo": item['email'],
					"telefono": item['telefono']				
				}
				if idGraduate is None:
					try:
						insert(target_cursor, table, item)
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
				else:
					try: 
						update(target_cursor, table, item, {"id": idGraduate[0]})
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
			else: 
				print("Objeto con valores nulos o vacios")
	
	elif table == STUDIOS_UC:
		print("ESTUDIOSUC")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
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
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
				else:
					print("ACTUALIZADO")
					try: 
						update(target_cursor, table, item, {"id": studiosUc[0]})
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
			else:
				print("Objeto con valores nulos o vacios")
	
	elif table == "egresado-estudiosuc":
		print("EGRESADO ESTUDIOSUC")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
				target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
				idGraduate = target_cursor.fetchone()

				studiosUcList = item["estudiosuc"]

				if studiosUcList is not None and idGraduate is not None:
					for i in studiosUcList:
						if validateJson(i):
							studiosUcCode = i['codigo']
							facultyCode = i['facultad']
							professionCode = i['carrera']

							target_cursor.execute(studiosUcQuery.get_query_code, [studiosUcCode])
							idStudiosUc = target_cursor.fetchone()
							idYear = None
							if idStudiosUc is not None:
								anhoCode = idStudiosUc[1].strftime('%Y-%m-%d').split("-")
								target_cursor.execute(yearQuery.get_query_code, [anhoCode[0]])
								idYear = target_cursor.fetchone()

							target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
							idFaculty = target_cursor.fetchone()

							target_cursor.execute(professionQuery.get_query_code, [professionCode])
							idProfession = target_cursor.fetchone()

							target_cursor.execute(graduateStudiosUcRelationship.get_query_code, [studiosUcCode])
							idFact = target_cursor.fetchone()

							if idStudiosUc is not None and idFaculty is not None and idProfession is not None and idYear is not None and idGraduate is not None:
								if idFact is not None:
									print("ACTUALIZADO")
									try:
										target_cursor.execute(dedent("""\
										UPDATE fact_egresado_estudiosuc
										SET id_egresado=%s, id_estudiosuc=%s, id_facultad=%s, id_carrera=%s, id_tiempo=%s 
										WHERE id=%s;"""), [idGraduate[0], idStudiosUc[0], idFaculty[0], idProfession[0], idYear[0], idFact[0]])
										target_cnx.commit()
										print("Registro actualizado")
									except mysql.connector.Error as e:
										print("Roolback {}".format(e))
								else:
									print("INSERTADO")
									try:
										target_cursor.execute(dedent("""\
										INSERT INTO fact_egresado_estudiosuc 
										(id_egresado, id_estudiosuc, id_facultad, id_carrera, id_tiempo)
										VALUES (%s, %s, %s, %s, %s)"""), [idGraduate[0], idStudiosUc[0], idFaculty[0], idProfession[0], idYear[0]])
										target_cnx.commit()
										print("Registro insertado")
									except mysql.connector.Error as e:
										print("Roolback {}".format(e))
						else:
							print("Objeto con valores nulos o vacios")
			else:
				print("Objeto con valores nulos o vacios")
		print("Actualizacion finalizada")
	
	elif table == "trabajos":
		print("Trabajos\n\n")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
				item = {
					"nombre_empresa": item['nombreempresa'],
					"cargo": item['cargo'],
					"descripcion": item['descripcion'],
					"codigo": item['codigo']
				}
				target_cursor.execute(jobsQuery.get_query_code, [item['codigo']])
				job = target_cursor.fetchone()
				if job is None:
					print("INSERTADO")
					try:
						insert(target_cursor, table, item)
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
				else:
					print("ACTUALIZADO")
					try: 
						update(target_cursor, table, item, {"id": job[0]})
						target_cnx.commit()
					except mysql.connector.Error as e:
						print("Roolback")
			else:
				print("Objeto con valores nulos o vacios")

	elif table == "egresado-trabajos":
		print("EGRESADO TRABAJOS")
		items = content[ITEMS]
		for item in items:
			print(item)
			if validateJson(item):
				target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
				idGraduate = target_cursor.fetchone()
				print(item['egresado'])
				jobsList = item["trabajos"]

				if jobsList is not None and idGraduate is not None:
					for i in jobsList:
						if validateJson(i):
							jobCode = i['codigo']
							print(jobCode)
							target_cursor.execute(jobsQuery.get_query_code, [jobCode])
							idJob = target_cursor.fetchone()

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
										target_cnx.commit()
										print("Registro actualizado")
									except mysql.connector.Error as e:
										print("Roolback {}".format(e))
								else:
									print("INSERTADO")
									try:
										target_cursor.execute(dedent("""\
										INSERT INTO fact_egresado_trabajos 
										(id_egresado, id_trabajo)
										VALUES (%s, %s)"""), [idGraduate[0], idJob[0]])
										target_cnx.commit()
										print("Registro insertado")
									except mysql.connector.Error as e:
										print("Roolback {}".format(e))
						else:
							print("Objeto con valores nulos o vacios")
			else:
				print("Objeto con valores nulos o vacios")
		print("Actualizacion finalizada")

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

